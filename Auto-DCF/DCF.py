import yfinance as yf
import numpy as np

class DCF:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def calculate_fcf(self):
        cashflow = self.stock.cashflow
        if 'Free Cash Flow' in cashflow.index:
            fcf = cashflow.loc['Free Cash Flow'].dropna()  # Ensure no NaN values
            print("Free Cash Flow (FCF) Data:", fcf)
        else:
            print("Free Cash Flow data is not available.")
            fcf = None
        return fcf
    
    def calculate_wacc(self):
        ticker = yf.Ticker(self.ticker)
        income_statement = self.stock.financials
        
        try:
            ebit = income_statement.loc['EBIT'].iloc[0]
            interest_expense = income_statement.loc['Interest Expense'].iloc[0]
        except (KeyError, IndexError):
            print("EBIT or Interest Expense data is not available.")
            return None

        tax_rate = 0.125  # Example tax rate
        risk_free_rate = 0.02  # Example: US 10-year treasury yield
        market_premium = 0.04  # Historical average market premium
        beta =  ticker.info['beta'] # Example beta value for the company

        # Cost of Equity (CAPM)
        cost_of_equity = risk_free_rate + beta * market_premium

        # Cost of Debt (after tax)
        try:
            cost_of_debt = (interest_expense * (1 - tax_rate)) / ebit  # Adjust for taxes
        except ZeroDivisionError:
            print("Error calculating cost of debt.")
            cost_of_debt = None

        # Assume weights (debt/equity ratio) for simplicity
        debt=np.array(ticker.balance_sheet.loc['Total Debt'])
        equity=np.array(ticker.balance_sheet.loc['Total Equity Gross Minority Interest'])
        equity_weight = float((equity/(equity+debt))[0])
        debt_weight = float((debt/(equity+debt))[0])

        if cost_of_debt is not None:
            wacc = (cost_of_equity * equity_weight) + (cost_of_debt * debt_weight)
        else:
            wacc = cost_of_equity * equity_weight  # Use equity WACC if debt info is unavailable
        
        print("Calculated WACC:", wacc)
        return wacc
    
    def terminal_value(self, fcf):
        wacc = self.calculate_wacc()
        if wacc is None:
            return None
        growth_rate = 0.04  # Constant terminal growth rate, example value

        if wacc <= growth_rate:
            print("Error: WACC should be greater than the growth rate.")
            return None

        # Last year FCF is used for terminal value calculation
        try:
            terminal_value = fcf.iloc[-1] * (1 + growth_rate) / (wacc - growth_rate)
        except (IndexError, KeyError, ZeroDivisionError):
            print("Error calculating terminal value due to missing FCF or invalid WACC.")
            terminal_value = None
        return terminal_value

    def calculate_dcf(self):
        fcf = self.calculate_fcf()
        if fcf is None or fcf.empty:
            print("FCF data is missing. Unable to calculate DCF.")
            return None

        wacc = self.calculate_wacc()
        if wacc is None:
            print("WACC calculation failed. Unable to calculate DCF.")
            return None

        terminal_value = self.terminal_value(fcf)
        if terminal_value is None:
            print("Terminal value calculation failed.")
            return None

        dcf = []  # Initialize the list to store discounted cash flows
        n_years = len(fcf)

        # Calculate discounted FCF for each year except the terminal value
        for i in range(n_years):
            try:
                discounted_fcf = fcf.iloc[i] / (1 + wacc) ** (i + 1)  # Correctly access FCF with iloc
                dcf.append(discounted_fcf)
            except (IndexError, KeyError, ZeroDivisionError):
                print(f"Error calculating discounted FCF for year {i+1}.")
                dcf.append(0)  # Append 0 if there's an error

        # Add the terminal value, discounted using the last WACC
        try:
            terminal_value_discounted = terminal_value / (1 + wacc) ** n_years
            dcf.append(terminal_value_discounted)
        except ZeroDivisionError:
            print("Error discounting terminal value.")
            dcf.append(0)  # Append 0 if there's an error

        # Debugging: Print the final DCF list
        print("Final DCF with discounted terminal value:", dcf)
        return np.nansum(dcf)  # Return the sum of discounted cash flows, ignore NaN values
    
    def get_outstanding_shares(self):
        try:
            shares = self.stock.info['sharesOutstanding']
        except KeyError as e:
            print(f"KeyError: {e}")
            shares = None
        return shares
    
    def calculate_projected_share_price(self):
        dcf_value = self.calculate_dcf()
        shares_outstanding = self.get_outstanding_shares()
        
        if dcf_value is not None and shares_outstanding is not None:
            projected_share_price = dcf_value / shares_outstanding
        else:
            print("Cannot calculate projected share price due to missing data.")
            projected_share_price = None
        return projected_share_price


# Example usage
dcf_model = DCF('MSFT')  # Replace 'AAPL' with the desired ticker symbol
projected_share_price = dcf_model.calculate_projected_share_price()
print("Projected Share Price:", projected_share_price)
