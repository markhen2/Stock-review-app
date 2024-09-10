import customtkinter
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fetch_basic_data

dcf=""
news=''
fundamentals=''
stock_data = fetch_basic_data.StockData('AAPL')


#def preprocess(ticker,report_question):
    

def run_report():
    ticker=ticker.get()
    #report_question=report.get()

    #preprocess(dcf,news,fundamentals)
    app.destroy()

customtkinter.set_appearance_mode('dark')
app=customtkinter.CTk()
app.geometry('800x600')
app.title('Stock Analysis')

customtkinter.CTkLabel(app,text='input a ticker here please').grid(row=0,column=0)
ticker_input=tk.Entry(app, width=50)
ticker_input.grid(row=0,column=1)
customtkinter.CTkButton(app,text='submit',command=run_report).grid(row=0,column=2)
app.mainloop()