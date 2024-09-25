import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_dataframe(df):
           # Create a Treeview widget
    tree = ttk.Treeview(app)
    
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
    