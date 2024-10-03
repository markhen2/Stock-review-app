#Heatmap
import datetime
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colormaps

plt.rcParams["figure.figsize"] = (8, 5)


def heatmap(sector,ticker):
    

    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=365*5)

    
    if sector=='Energy':
        ticker_list = [f'{ticker}','MPC', 'EOG', 'PSX', 'VLO.VI', 'TTE', 'BP','cop' ,'CL=F','BZ=F','WTID.MI']

    elif sector=='Utilities':
        ticker_list=[f'{ticker}','DUK', 'NEE', 'SO', 'D']

    elif sector=='Discretionaries':
         ticker_list=[f'{ticker}','AMZN', 'TSLA', 'HD', 'MCD']
    
    elif sector=='Financial':
         ticker_list=[f'{ticker}','JPM', 'BAC', 'WFC', 'C']

    def get_prices(tickers, start):
            prices = pd.DataFrame()
            for ticker in tickers:
                data = yf.download(ticker, start=start, end=end)
                if 'Adj Close' in data:
                    prices[ticker] = data['Adj Close']
                else:
                    print(f"Warning: 'Adj Close' not found for {ticker}. Skipping.")
            return prices

    prices_df = get_prices(ticker_list, start)

    # Define a dictionary mapping old ticker names to new display names
    ticker_name_mapping = {

    'MPC': 'MPC',
    'EOG': 'EOG ',
    'PSX': 'Phillips66',
    'VLO.VI': 'Valero',
    'TTE': 'TotalEnergies',
    'BP': 'BP ',
    'cop': 'Connoco',
    'CL=F': 'Crude Oil ',
    'BZ=F': 'Brent Crude',
    'BZM24.NYM': 'Brent Jun 24 ',
    'WTID.MI': 'WTI Crude'
    }

    # Rename the columns of the DataFrame
    prices_df.rename(columns=ticker_name_mapping, inplace=True)          

    print(prices_df.shape)


    change_df = prices_df.pct_change()
    change_df.dropna(inplace=True)
    fig, ax =plt.subplots(figsize=(10,6))
    sns.heatmap(change_df.corr() ,annot=True,ax=ax)
    return fig