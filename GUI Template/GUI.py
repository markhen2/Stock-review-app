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


data = fetch_basic_data

#DCF Class logic

#News Class logic (SOURCE FROM PROXY DATABASE)

#ARI Suggestions and past buys import

#Fundamentals Class logic


#technical analysis class logic


#def preprocess(ticker,report_question):



def close_report():
    app.destroy()

def search_ticker():
    ticker = ticker_input.get()
    ticker_info_window = Toplevel(app)
    ticker_info_window.title('Ticker Information')
    ticker_info_window.geometry('800x600')

    # Basic stock information
    fetch_class = fetch_basic_data.StockData(ticker)
    info = fetch_class.get_stockinfo()
    customtkinter.CTkLabel(ticker_info_window, text=info, text_color='black').grid(row=1, column=0)
    customtkinter.CTkLabel(ticker_info_window, text='Ticker Information', text_color='black').grid(row=0, column=0)

    # Pricing data retrieval
    pricing = fetch_class.get_daily_stock()  # Corrected method call
    y_close_price = round(float(pricing['Close'][-1]), 2)

    pricing_close = round(pricing['Close'], 2)
    min_month = pricing_close.tail(30).min()
    max_month = pricing_close.tail(30).max()

    min_year = pricing_close.tail(255).min()
    max_year = pricing_close.tail(255).max()

    # Plot
    fig, ax = plt.subplots()
    pricing['Close'].plot(ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel(f'Price of {ticker}')
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=ticker_info_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=20, column=4)

    customtkinter.CTkLabel(ticker_info_window, text='Stock Analysis', text_color='black').grid(row=10, column=1)
    customtkinter.CTkLabel(ticker_info_window, text=f'Current Price: {y_close_price}', text_color='black').grid(row=11, column=1)
    customtkinter.CTkLabel(ticker_info_window, text=f'Monthly range: {min_month} - {max_month}', text_color='black').grid(row=12, column=1)
    customtkinter.CTkLabel(ticker_info_window, text=f'Yearly range: {min_year} - {max_year}', text_color='black').grid(row=17, column=1)



customtkinter.set_appearance_mode('dark')
app=customtkinter.CTk()
app.geometry('400*300')
app.title('Stock Analysis')




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



customtkinter.CTkButton(app,text='Open DCF Analysis' , command=run_dcf).grid(row=4,column=2)
customtkinter.CTkButton(app,text='Fetch optimal past buy/sell points',command=run_ARI).grid(row=5,column=2)
customtkinter.CTkButton(app,text='Close application',command=close_report).grid(row=7,column=2)

customtkinter.CTkLabel(app, text='Enter a ticker here please').grid(row=0, column=0)
ticker_input = Entry(app, width=20)
ticker_input.grid(row=0, column=1)
customtkinter.CTkButton(app, text='submit', command=search_ticker).grid(row=0, column=2)

app.mainloop()