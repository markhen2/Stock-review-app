import datetime
import yfinance as yf
import pandas as pd


def run_ARI(ticker):    
    crossover_points = {} #dictionary to store the dataframes for each ticke


    start_date='2020-01-01'
    end_date=datetime.datetime.today().strftime('%Y-%m-%d')
    # Base Moving Average Crossover Inidicator

    crossover_points = pd.DataFrame(columns=['Action', 'Price', 'Date'])
    df=yf.download(ticker,start=start_date,end=end_date)
    df['SMA_50']=df['Close'].rolling(window=50).mean()
    df['SMA_200']=df['Close'].rolling(window=200).mean()
    for i in range(1, len(df['Adj Close']) - 2):
        
        if df['SMA_50'][i-1] > df['SMA_200'][i] and df['SMA_50'][i] < df['SMA_200'][i+2]:
            new_row = pd.DataFrame({'Action': ['SELL'], 'Price': [round(df['Adj Close'][i],2)], 'Date': [df.reset_index()['Date'][i].date()]})
            crossover_points = pd.concat([crossover_points, new_row], ignore_index=True)


        if df['SMA_50'][i-1] < df['SMA_200'][i] and df['SMA_50'][i] > df['SMA_200'][i+2]:
            new_row = pd.DataFrame({'Action': ['BUY'], 'Price': [round(df['Adj Close'][i],2)], 'Date': [df.reset_index()['Date'][i].date()]})
            crossover_points = pd.concat([crossover_points, new_row], ignore_index=True)

    combined=crossover_points
    combined.reset_index(drop=True, inplace=True)

    combined.columns=['Action','Price','Date']
    combined = combined.sort_values(['Date'])

    combined['Date'] = pd.to_datetime(combined['Date'])
    combined = combined.sort_values('Date', ascending=False)

    all_trade_points=[]

    trade_points=combined
    if not trade_points.empty:
        trade_points['Time between Trades'] = -trade_points['Date'].diff()
        trade_points.loc[trade_points['Time between Trades'] < pd.Timedelta(days=7), 'Time between Trades'] = 'No Trade'
        trade_points['Override'] = 'Trade'
        # Ensure the condition is applied correctly

        if trade_points['Action'].iloc[-1] == 'SELL':
            trade_points['Override'].iloc[-1] = 'No Trade'


        for i in range(len(trade_points)-1):
        #Duplicate order rules

            if trade_points['Action'].iloc[i] == 'SELL' and trade_points['Action'].iloc[i+1] == 'SELL':
                trade_points['Override'].iloc[i+1] = 'No Trade'
            
            if trade_points['Action'].iloc[i] == 'BUY' and trade_points['Action'].iloc[i+1] == 'BUY':
                trade_points['Override'].iloc[i+1] = 'No Trade'
        all_trade_points.append(trade_points)

    updated_trade_points = pd.concat(all_trade_points)
    updated_trade_points=updated_trade_points.sort_values('Date', ascending=False)
    updated_trade_points.reset_index()

    return updated_trade_points[['Action','Date','Price','Override']]