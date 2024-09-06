import yfinance as yf
import numpy as np

class DCF:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def calculate_fcf(self):
        cashflow = self.stock.cashflow
        if 'Free Cash Flow' in cashflow.index:
            fcf = cashflow.loc['Free Cash Flow']
        else:
            print("Free Cash Flow data is not available.")
            fcf = None
        return fcf
    
    def calculate_wacc(self):
        balance_sheet = self.stock.balance_sheet
        income_statement = self.stock.financials
        try:
            ebit = income_statement.loc['EBIT']
            interest_expense = income_statement.loc['Interest Expense']
            tax_rate = 0.21
            tax_savings = interest_expense * tax_rate
            cost_of_debt = interest_expense / balance_sheet.loc['Total Debt']
            cost_of_equity = ebit / balance_sheet.loc['Total Equity Gross Minority Interest']
            wacc = (cost_of_debt * (1 - tax_rate) * (balance_sheet.loc['Total Debt'] / (balance_sheet.loc['Total Debt'] + balance_sheet.loc['Total Equity Gross Minority Interest']))) + (cost_of_equity * (balance_sheet.loc['Total Equity Gross Minority Interest'] / (balance_sheet.loc['Total Debt'] + balance_sheet.loc['Total Equity Gross Minority Interest'])))
        except KeyError as e:
            print(f"KeyError: {e}")
            wacc = None
        return wacc
    
    def calculate_terminal_value(self, fcf, wacc, growth_rate):
        if fcf is not None and wacc is not None:
            terminal_value = fcf[-1] * (1 + growth_rate) / (wacc - growth_rate)
        else:
            print("Cannot calculate terminal value due to missing data.")
            terminal_value = None
        return terminal_value
    
    def calculate_dcf(self, fcf, wacc, terminal_value):
        if fcf is not None and terminal_value is not None:
            dcf_value = np.sum(fcf) + terminal_value
        else:
            print("Cannot calculate DCF due to missing data.")
            dcf_value = None
        return dcf_value
    
    def get_outstanding_shares(self):
        try:
            shares = self.stock.info['sharesOutstanding']
        except KeyError as e:
            print(f"KeyError: {e}")
            shares = None
        return shares
    
    def calculate_projected_share_price(self, dcf_value):
        shares_outstanding = self.get_outstanding_shares()
        if dcf_value is not None and shares_outstanding is not None:
            projected_share_price = dcf_value / shares_outstanding
        else:
            print("Cannot calculate projected share price due to missing data.")
            projected_share_price = None
        return projected_share_price

# Example usage
dcf_model = DCF('AAPL')  # Replace 'AAPL' with the desired ticker symbol
fcf = dcf_model.calculate_fcf()
wacc = dcf_model.calculate_wacc()
terminal_value = dcf_model.calculate_terminal_value(fcf, wacc, 0.02)  # Example growth rate of 2%
dcf_value = dcf_model.calculate_dcf(fcf, wacc, terminal_value)
projected_share_price = dcf_model.calculate_projected_share_price(dcf_value)
print("Projected Share Price:", projected_share_price)