import yfinance as yf
import pandas as pd

class StockData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_stockinfo(self):
        return pd.Series(self.stock.info).head(20)

    def get_daily_stock_pricing(self, start_date, end_date):
        df = yf.download(self.ticker, start=start_date, end=end_date)
        return df['Adj Close']

    def get_daily_stock(self, start_date, end_date):
        stock_data = self.stock.history(start=start_date, end=end_date)
        return stock_data

    def get_minute_stock_data(self, start_date, end_date):
        stock_data = self.stock.history(start=start_date, end=end_date, interval='1m')
        return stock_data
    
    def get_balance_sheet_annual(self):
        self.ticker.balance_sheet

    def get_balance_sheet_quarterly(self):
        self.ticker.quarterly_balance_sheet

    def get_cashflow_annual(self):
        self.ticker.cashflow

    def get_cashflow_quarterly(self):
        self.ticker.quarterly_cashflow

    def get_earnings_annual(self):
        self.ticker.earnings

    def get_earnings_quarterly(self):
        self.ticker.quarterly_earnings

    def get_calander(self):
        self.ticker.calendar