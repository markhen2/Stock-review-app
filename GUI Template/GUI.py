import customtkinter
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import fetch_basic_data
from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel

#stock_data = fetch_basic_data.StockData('AAPL')

#DCF Class logic

#News Class logic (SOURCE FROM PROXY DATABASE)

#ARI Suggestions and past buys import

#Fundamentals Class logic


#technical analysis class logic


#def preprocess(ticker,report_question):



def close_report():
    app.destroy()

def search_ticker():
    global ticker
    ticker=ticker_input.get()
    ticker_info_window=Toplevel(app)
    ticker_info_window.title('Ticker Information')
    ticker_info_window.geometry('800x600')
    
    customtkinter.CTkLabel(ticker_info_window,text='Stock Analysis').grid(row=0,column=1)


customtkinter.set_appearance_mode('dark')
app=customtkinter.CTk()
app.geometry('200*300')
app.title('Stock Analysis')


def run_dcf():
    dcf_window=Toplevel(app)
    dcf_window.title('DCF Analysis')
    dcf_window.geometry('800x600')

    Label(dcf_window,text='DCF Analysis').pack()



customtkinter.CTkButton(app,text='Open DCF Analysis' , command=run_dcf).grid(row=4,column=2)


customtkinter.CTkLabel(app,text='input a ticker here please').grid(row=0,column=0)
ticker_input=tk.Entry(app, width=50)
ticker_input.grid(row=0,column=1)
customtkinter.CTkButton(app,text='submit',command=search_ticker).grid(row=0,column=2)
app.mainloop()