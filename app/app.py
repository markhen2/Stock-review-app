import customtkinter
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Toplevel, Entry, filedialog
import fetch_basic_data
from tkinter import *
from tkinter.ttk import *
from tkinter import Toplevel
import plotly.graph_objects as go
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from m_carlo import monte_carlo
from DCF import DCF
from ARI import run_ARI
from tkinter import ttk
import pandas as pd
from update_available import is_update_available, start_update_process
from version import __version__
import time
from Heatmap import heatmap

asset_name='app.app'
def main():
    # Create the main window
    root = tk.Tk()
    root.title("Stock Analysis App")

    # Create a text widget to display messages
    text_widget = tk.Text(root, wrap='word', height=10, width=50)
    text_widget.pack(padx=10, pady=10)

    def log_message(message):
        text_widget.insert(tk.END, message + "\n")
        text_widget.see(tk.END)
        root.update_idletasks()

    def on_update_confirm():
        log_message("Starting update process.")
        start_update_process()
        root.destroy()
    
    def on_update_cancel():
        log_message("Update canceled. Exiting application.")
        root.destroy()   
        
    # Check for updates on startup
    log_message("Checking for updates...")
    if is_update_available():
        log_message("New update is available.")
        update_frame = tk.Frame(root)
        update_frame.pack(pady=10)
        tk.Button(update_frame, text="Update Now", command=on_update_confirm).pack(side=tk.LEFT, padx=5)
        tk.Button(update_frame, text="Cancel", command=on_update_cancel).pack(side=tk.LEFT, padx=5)
    else:
        log_message("No updates available.")
        # Continue with the main application logic
        log_message("Running the application as usual.")
        time.sleep(3)
        root.destroy()
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()



def display_dataframe(parent,df):
           # Create a Treeview widget
    tree = ttk.Treeview(parent)
    
    # Define the columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    
    # Set the column headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    
    # Add the data to the Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")
    

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

def display_ARI():
    ARI_window=Toplevel(app)
    ARI_window.title('ARI Analysis')
    ARI_window.geometry('800x600')
    
    ticker=ticker_input.get()

    df=run_ARI(ticker)
    display_dataframe(ARI_window,df)
    
        
def run_dcf():
    dcf_window=Toplevel(app)
    dcf_window.title('DCF Analysis')
    dcf_window.geometry('800x600')

    ticker=ticker_input.get()
    dcf_model = DCF(ticker)
    projected_share_price = dcf_model.calculate_projected_share_price()

    customtkinter.CTkLabel(dcf_window, text=f'Projected Share Price: {projected_share_price}', text_color='black').grid(row=1, column=0)
    customtkinter.CTkLabel(dcf_window, text=f'WACC: {dcf_model.calculate_wacc()}', text_color='black').grid(row=2, column=0)
    customtkinter.CTkLabel(dcf_window, text=f'Free Cash Flow: {dcf_model.calculate_fcf()}', text_color='black').grid(row=3, column=0)
    customtkinter.CTkLabel(dcf_window, text=f'DCF: {dcf_model.calculate_dcf()}', text_color='black').grid(row=4, column=0)
    customtkinter.CTkLabel(dcf_window, text=f'Outstanding Shares: {dcf_model.get_outstanding_shares()}', text_color='black').grid(row=5, column=0)


def relevant_news():
    news_window=Toplevel(app)
    news_window.title('Relevant News')
    news_window.geometry('800x600')

    Label(news_window,text='Relevant News').pack()

def mcarlo_sim():
    ticker=ticker_input.get()
    
    mcarlo_window=Toplevel(app)
    mcarlo_window.title('Monte Carlo Simulation')
    mcarlo_window.geometry('1000x600')
    

    customtkinter.CTkLabel(mcarlo_window, text='# Days to predict').grid(row=1, column=0)
    projection_length_input = Entry(mcarlo_window, width=20) 
    projection_length_input.grid(row=1, column=1)
    
    customtkinter.CTkLabel(mcarlo_window, text='# Of Simulations to run').grid(row=2, column=0)
    number_simulations_input = Entry(mcarlo_window, width=20) 
    number_simulations_input.grid(row=2, column=1)

    def run_mcarlo_sim():
        number_simulations=int(number_simulations_input.get())
        prediction_days=int(projection_length_input.get())
        monte_carlo(ticker, number_simulations, prediction_days)
    
    
    customtkinter.CTkButton(mcarlo_window, text='Run SIM', command=run_mcarlo_sim).grid(row=3, column=0, sticky='w')
    
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=mcarlo_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both') 
    
    #mcarlo_window.grid_rowconfigure(4, weight=1)
    #mcarlo_window.grid_columnconfigure(0, weight=1)
    #mcarlo_window.grid_columnconfigure(1, weight=1)

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

def run_heatmap():
    ticker=ticker_input.get()
    sector=sector_dropdown.get()
    heatmap_window=Toplevel(app)
    heatmap_window.title('Heatmap')
    heatmap_window.geometry('1000x600')
    fig=heatmap(sector,ticker)

    #fig ,ax= plt.subplots(figsize=(10, 6))

    canvas = FigureCanvasTkAgg(fig, master=heatmap_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both') 
    
    def save_plot():
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)

    save_button = customtkinter.CTkButton(heatmap_window, text='Save Heatmap', command=save_plot)
    save_button.pack(pady=5)
 

def optimal_options():
    ticker=ticker_input.get()
    

customtkinter.set_appearance_mode('light')
app=customtkinter.CTk()
app.geometry('400*300')
app.title('Stock Analysis')

ticker_input = Entry(app, width=20)
ticker_input.grid(row=0, column=1)



customtkinter.CTkLabel(app, text='Enter a ticker here please').grid(row=0, column=0)
customtkinter.CTkButton(app, text='Stock data', command=search_ticker).grid(row=0, column=2)

customtkinter.CTkButton(app,text='Open DCF Analysis' , command=run_dcf).grid(row=4,column=2, sticky='w')
customtkinter.CTkButton(app,text='Fetch optimal past buy/sell points',command=run_ARI).grid(row=5,column=2, sticky='w')
customtkinter.CTkButton(app,text='Monte Carlo Simulation',command=mcarlo_sim).grid(row=7,column=2, sticky='w')
customtkinter.CTkButton(app,text='ARI',command=display_ARI).grid(row=9,column=2, sticky='w')
customtkinter.CTkButton(app,text='Close application',command=close_report).grid(row=8,column=2,sticky='w')
customtkinter.CTkButton(app,text='Create heatmap',command=run_heatmap).grid(row=10,column=2,sticky='w')

#Heatmap options:
sector_options=["Utilities","Energy",'Discretionaries']
sector_dropdown=customtkinter.CTkOptionMenu(app,values=sector_options)
sector_dropdown.grid(row=10,column=1, sticky='w')

app.mainloop()