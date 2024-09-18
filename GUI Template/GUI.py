import customtkinter
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fetch_basic_data
from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel
import plotly.graph_objects as go
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from m_carlo import monte_carlo

data = fetch_basic_data



def close_report():
    app.destroy()

def search_ticker():
    ticker = ticker_input.get()
    ticker_info_window = Toplevel(app)
    ticker_info_window.title('Ticker Information')
    ticker_info_window.geometry('900x700')

    # Basic stock information
    fetch_class = fetch_basic_data.StockData(ticker)
    info = fetch_class.get_stockinfo()
    info_df=pd.DataFrame(info)
    
    address=str(info_df.loc['address1']).split('\n')[0].split('    ')[1], str(info_df.loc['country']).split('\n')[0].split('    ')[1]
    sector=str(info_df.loc['sector']).split('\n')[0].split('    ')[1]
    website=str(info_df.loc['website']).split('\n')[0].split('    ')[1]

    customtkinter.CTkLabel(ticker_info_window, text=f'Company name {ticker}', text_color='black').grid(row=1, column=0,sticky='w')
    customtkinter.CTkLabel(ticker_info_window, text=f'Company address {address}', text_color='black').grid(row=2, column=0,sticky='w')
    customtkinter.CTkLabel(ticker_info_window, text=f'Stock sector {sector}', text_color='black').grid(row=3, column=0,sticky='w')
    customtkinter.CTkLabel(ticker_info_window, text=f'Company website {website}', text_color='black').grid(row=4, column=0,sticky='w')


    # Pricing data retrieval
    pricing = fetch_class.get_daily_stock()  # Corrected method call
    y_close_price = round(float(pricing['Close'][-1]), 2)

    pricing_close = round(pricing['Close'], 2)
    min_month = pricing_close.tail(30).min()
    max_month = pricing_close.tail(30).max()

    min_year = pricing_close.tail(255).min()
    max_year = pricing_close.tail(255).max()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    pricing['Close'].plot(ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel(f'Price of {ticker}')
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=ticker_info_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=10, column=0)

    customtkinter.CTkLabel(ticker_info_window, text=f'Current Price: {y_close_price}', text_color='black').grid(row=5, column=0)
    customtkinter.CTkLabel(ticker_info_window, text=f'Monthly range: {min_month} - {max_month}', text_color='black').grid(row=6, column=0)
    customtkinter.CTkLabel(ticker_info_window, text=f'Yearly range: {min_year} - {max_year}', text_color='black').grid(row=7, column=0)

def run_ARI():
    ARI_window=Toplevel(app)
    ARI_window.title('ARI Analysis')
    ARI_window.geometry('800x600')
    Label(ARI_window,text='ARI Analysis').pack()

def run_dcf():
    dcf_window=Toplevel(app)
    dcf_window.title('DCF Analysis')
    dcf_window.geometry('800x600')

    Label(dcf_window,text='DCF Analysis').pack()

def relevant_news():
    news_window=Toplevel(app)
    news_window.title('Relevant News')
    news_window.geometry('800x600')

    Label(news_window,text='Relevant News').pack()

def mcarlo_sim():
    ticker=ticker_input.get()
    number_simulations = int(number_simulations_input.get())
    prediction_days = int(projection_length_input.get())

    mcarlo_window=Toplevel(app)
    mcarlo_window.title('Monte Carlo Simulation')
    mcarlo_window.geometry('800x600')
    Label(mcarlo_window,text='Monte Carlo Simulation').pack()
    customtkinter.CTkLabel(app, text='# Days to predict').grid(row=0, column=0)
    projection_length_input = Entry(mcarlo_window, width=20) 
    projection_length_input.grid(row=0, column=1)

    customtkinter.CTkLabel(app, text='# Of Simulations to run').grid(row=1, column=0)
    number_simulations_input = Entry(mcarlo_window, width=20) 
    number_simulations_input.grid(row=1, column=1)
    customtkinter.CTkButton(app, text='Submit', command=lambda:monte_carlo(ticker,prediction_days,number_simulations)).grid(row=3, column=1)
 

def interest_rate_tracker():
    interest_window=Toplevel(app)
    interest_window.title('Interest Rate Tracker')
    interest_window.geometry('800x600')

    Label(interest_window,text='Interest Rate Tracker').pack()

def economic_indicators():
    economic_window=Toplevel(app)
    economic_window.title('Economic Indicators')
    economic_window.geometry('800x600')

    Label(economic_window,text='Economic Indicators').pack()


customtkinter.set_appearance_mode('light')
app=customtkinter.CTk()
app.geometry('400*300')
app.title('Stock Analysis')

ticker_input = Entry(app, width=20)
ticker_input.grid(row=0, column=1)



customtkinter.CTkLabel(app, text='Enter a ticker here please').grid(row=0, column=0)
customtkinter.CTkButton(app, text='submit', command=search_ticker).grid(row=0, column=2)

customtkinter.CTkButton(app,text='Open DCF Analysis' , command=run_dcf).grid(row=4,column=2)
customtkinter.CTkButton(app,text='Fetch optimal past buy/sell points',command=run_ARI).grid(row=5,column=2)
customtkinter.CTkButton(app,text='Close application',command=close_report).grid(row=7,column=2)
customtkinter.CTkButton(app,text='Monte Carlo Simulation',command=mcarlo_sim).grid(row=8,column=2)

app.mainloop()