#DCF
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


# Now you can use functions from fetch_basic_data
# Example:
# stock_info = fetch_basic_data.get_stockinfo('AAPL')
class DCF:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def calculate_fcf(self):
        cashflow = self.stock.cashflow
        fcf = cashflow['Free Cash Flow']
        return fcf
    
    def calculate_wacc(self):
        balance_sheet = self.stock.balance_sheet
        income_statement = self.stock.financials
        ebit = income_statement['EBIT']
        interest_expense = income_statement['Interest Expense']
        tax_rate = 0.21
        tax_savings = interest_expense * tax_rate
        cost_of_debt = interest_expense / balance_sheet['Total Debt']
        cost_of_equity = ebit / balance_sheet['Total Equity']
        wacc = (cost_of_debt * (1 - tax_rate) * (balance_sheet['Total Debt'] / (balance_sheet['Total Debt'] + balance_sheet['Total Equity']))) + (cost_of_equity * (balance_sheet['Total Equity'] / (balance_sheet['Total Debt'] + balance_sheet['Total Equity'])))
        return wacc
    
    def calculate_terminal_value(self, fcf, wacc, growth_rate):
        terminal_value = fcf[-1] * (1 + growth_rate) / (wacc - growth_rate)
        return terminal_value
    
    def calculate_dcf(self, fcf, wacc, terminal_value):
        dcf = np.sum(fcf) + terminal_value
        return dcf
    
DCF('MPC').calculate_fcf()