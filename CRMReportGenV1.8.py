import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime
from datetime import timedelta
from tkinter import *
import customtkinter
import openpyxl

def wsm(last_week_stand_up, open_main_total, won_last_week_total, won_total,Standup_Date):
    # Process the files
    open_mainpipe_total = pd.read_csv(open_main_total)
    last_week_pipe = pd.read_csv(last_week_stand_up)
    won_last_week_pipe = pd.read_csv(won_last_week_total)
    won_pipeline_total = pd.read_csv(won_total)
    
    # Add your processing logic here
    print("Processing completed.")
    
    Excel_sheet_name=f'Weekly standup {Standup_Date}'
    # Mainpipeline open cases total download:
    open_mainpipe_total=pd.read_csv(open_main_total)
    # Last weeks weekly standup meeting won pipeline tracker
    last_week_pipe=pd.read_csv(last_week_stand_up)
    # Mainpipeline won in previous week:
    won_pipeline_1w=pd.read_csv(won_last_week_total)
    # Mainpipeline won Total:_total
    won_pipeline_total=pd.read_csv(won_total)

    won_last_week_total=pd.read_csv(won_last_week_total)

    # Filter rows where the 'Stage' column value is 'Mcube to advise'
    advise_df = open_mainpipe_total[open_mainpipe_total['Stage'] == 'Mcube to advise']
    #Pipeline Processing
    
    live=won_pipeline_total[won_pipeline_total['Stage']=='Li5000ve']
    live=live[['Deal Name','Deal Value']]
    converted_live=last_week_pipe[last_week_pipe['Deal Name'].isin(live['Deal Name'])]
    converted_live[['Deal Name','Deal Owner','Value','Comment']]
    remaining_rows = last_week_pipe[~last_week_pipe['Deal Name'].isin(converted_live['Deal Name'])]
    if 'Unnamed: 1' in remaining_rows.columns:
        remaining_rows=remaining_rows.drop('Unnamed: 1',axis=1)  
  
    merged_df=pd.merge(won_pipeline_total,remaining_rows,on='Deal Name',how='inner')
    merged_df=merged_df[['Stage','Deal Name','Deal Owner_x','Deal Value','Comment','Contacted','Contacted.1','Contacted.2']]

    one_two_week=merged_df[merged_df['Stage']=='Submitted for account opening [wk 1s-2]']
    three_plus=merged_df[merged_df['Stage']=='Submitted for account opening [wk 3+]']
    five_week=merged_df[merged_df['Stage']=='Submitted for account opening [wk 5+]']
    seven_week=merged_df[merged_df['Stage']=='Submitted for account opening [wk7+]']

    one_two_merged=pd.merge(one_two_week,won_pipeline_total[won_pipeline_total['Stage']=='Submitted for account opening [wk 1s-2]'], on='Deal Name',how='outer')
    one_two_merged=one_two_merged[['Stage_y','Deal Name','Deal Owner','Deal Value_y','Comment','Contacted','Contacted.1','Contacted.2']]
    Early_submit=one_two_merged

    three_plus_merged=pd.merge(three_plus,won_pipeline_total[won_pipeline_total['Stage']=='Submitted for account opening [wk 3+]'], on='Deal Name',how='outer')
    three_plus_merged=three_plus_merged[['Stage_y','Deal Name','Deal Owner','Deal Value_y','Comment','Contacted','Contacted.1','Contacted.2']]
    mid_submit=three_plus_merged

    five_week_merged=pd.merge(five_week,won_pipeline_total[won_pipeline_total['Stage']=='Submitted for account opening [wk 5+]'], on='Deal Name',how='outer')
    five_week_merged=five_week_merged[['Stage_y','Deal Name','Deal Owner','Deal Value_y','Comment','Contacted','Contacted.1','Contacted.2']]
    five_week=five_week_merged

    seven_week_merged=pd.merge(seven_week,won_pipeline_total[won_pipeline_total['Stage']=='Submitted for account opening [wk7+]'], on='Deal Name',how='outer')
    seven_week_merged=seven_week_merged[['Stage_y','Deal Name','Deal Owner','Deal Value_y','Comment','Contacted','Contacted.1','Contacted.2']]
    seven_week=seven_week_merged

    pipeline = pd.concat([seven_week,five_week,mid_submit,Early_submit], axis=0, ignore_index=True)
    pipeline['Stage']=pipeline['Stage_y']
    pipeline['Deal Value']=pipeline['Deal Value_y']
    pipeline=pipeline[['Stage','Deal Name','Deal Owner','Deal Value', 'Comment','Contacted','Contacted.1','Contacted.2']]
    


    # Select the specific columns 'Owner Name', 'Title', and 'Value'
  
    to_advise = advise_df[['Deal Name', 'Deal Owner','Deal Value']]                                 
    TAT=pd.DataFrame({'MoneyCube to Advise':''},
                       index=[0])
    to_advise=pd.concat([TAT, to_advise[:]]).reset_index(drop = True)
    to_advise=to_advise.iloc[1:] 
    

    reviewing_df= open_mainpipe_total[open_mainpipe_total['Stage']=='Reviewing recommendation']
    reviewing_df=reviewing_df[['Deal Name', 'Deal Owner','Deal Value']]   
    RT=pd.DataFrame({'Reviewing Recomendation':''},
                       index=[0])
    reviewing_df=pd.concat([RT, reviewing_df[:]]).reset_index(drop = True)
    reviewing_df=reviewing_df.iloc[1:] 
    

    acc_awaiting_docs=won_pipeline_total[won_pipeline_total['Stage']=='Accepted - await docs']
    acc_awaiting_docs=acc_awaiting_docs[['Deal Name', 'Deal Owner','Deal Value']]                    
    acc_awaiting_docs=acc_awaiting_docs.reset_index().drop('index',axis=1)
    AT=pd.DataFrame({'Accepted - await docs':''},
                       index=[0])
    acc_awaiting_docs=pd.concat([AT, acc_awaiting_docs[:]]).reset_index(drop = True)
    acc_awaiting_docs=acc_awaiting_docs.iloc[1:] 
    

    live=won_pipeline_total[won_pipeline_total['Stage']=='Live']
    live=live[['Deal Name','Deal Value']]
    
                                                                                             


    won_pipeline_total[won_pipeline_total['Stage']=='Fund switches and other tasks']  
    WPTT=pd.DataFrame({'Won Total Pipeline':''},
                       index=[0])
    won_pipeline_total=pd.concat([WPTT, won_pipeline_total[:]]).reset_index(drop = True)
    won_pipeline_total=won_pipeline_total.iloc[1:]     



    won_last_week_total=won_last_week_total[['Deal Name','Deal Owner','Deal Value']]   
    WLWTT=pd.DataFrame({'Won Last Week Total':''},
                       index=[0])
    won_last_week_total=pd.concat([WLWTT, won_last_week_total[:]]).reset_index(drop = True)
    won_last_week_total=won_last_week_total.iloc[1:]                                                                                                                
    


    #Is live
    live=won_pipeline_total[won_pipeline_total['Stage']=='Live']
    live=live[['Deal Name','Deal Value']]
    lwp=last_week_pipe[last_week_pipe['Deal Name'].isin(live['Deal Name'])] 
    lwp=lwp[['Deal Name','Deal Owner','Value']]    
    lwp_title=pd.DataFrame({'Converted to live':''},
                       index=[0])
    lwp=pd.concat([lwp_title, lwp[:]]).reset_index(drop = True)
    lwp=lwp.iloc[1:]
    lwp['Email Confirmed']=""
    


    fund_switches=won_pipeline_total[won_pipeline_total['Stage']=='Fund switches and other tasks']
    fund_switches=fund_switches[['Pipeline','Stage','Deal Name','Deal Owner','Deal Value']]
    fund_switch_title=pd.DataFrame({'Fund Switch/Other Tasks':''},
                       index=[0])
    fund_switches=pd.concat([fund_switch_title, fund_switches]).reset_index(drop = True)
    fund_switches=fund_switches.iloc[1:]

    prospect=(len(open_mainpipe_total[open_mainpipe_total['Stage']=='Prospect']))                                                            
    prospect_df=open_mainpipe_total[open_mainpipe_total['Stage']=='Prospect']
    summary={'Last Week - Cases Won':[len(won_last_week_total)],
             'Last Week - Converted to Live':[len(lwp)],
             'Accepted awaiting docs':[len(acc_awaiting_docs)],
             'Submitted for account opening':[(len(seven_week)+len(five_week)+len(mid_submit)+len(Early_submit))],
             'Reviewing recommendation':[len(reviewing_df)],
             'MoneyCube to Advise':[len(to_advise)],
             'Prospect':[len(prospect_df)]}    

    summary=pd.DataFrame(summary)
    summary=summary.T
    summary['Last Week']=summary[0]
    summary['Prior Week']=""
    summary['6Wk Rolling Average']=""
    summary['Total']=""
    summary=summary.drop(0,axis=1)
    
    # Generate an excel spreadsheet that has one sheet per necessary propogation !!!# 

    with pd.ExcelWriter(f'{Excel_sheet_name}.xlsx') as writer:
        

        lwp.to_excel(writer,sheet_name=Standup_Date, startrow=15+len(won_last_week_total) , startcol=0)
        won_last_week_total.to_excel(writer, sheet_name=Standup_Date, startrow=10, startcol=0)
        acc_awaiting_docs.to_excel(writer,sheet_name=Standup_Date,startrow=1, startcol=8)
        pipeline.to_excel(writer, sheet_name=Standup_Date, startrow=(4+len(acc_awaiting_docs)), startcol=8, header=True) #Keep headers
        reviewing_df.to_excel(writer,sheet_name=Standup_Date,startrow=1,startcol=18)
        to_advise.to_excel(writer, sheet_name=Standup_Date, startrow=3+len(reviewing_df), startcol=18)
        summary.to_excel(writer,sheet_name=Standup_Date,startrow=1,startcol=1,header=True)
        ## Reprocessing pipeline for use in next iteration

    pipeline=pipeline.drop('Stage',axis=1)
    pipeline['Value']=pipeline['Deal Value']
    pipeline=pipeline.drop('Deal Value',axis=1)
    pipeline=pipeline[['Deal Name','Deal Owner','Value','Comment','Contacted','Contacted.1','Contacted.2']]
    pipeline.columns=['Deal Name','Deal Owner','Value','Comment','Contacted','Contacted','Contacted']
    
    
    formatted_date=(datetime.datetime.today()+timedelta(days=7)).strftime('%Y-%m-%d')
    pipeline.to_csv(f'{formatted_date} pipeline.csv',index=False)#

       
        

def select_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def run_wsm():
    last_week_stand_up = last_week_entry.get()
    open_main_total = open_main_entry.get()
    won_last_week_total = won_last_week_entry.get()
    won_total = won_total_entry.get()
    Standup_Date=standup_date_entry.get()
    
    wsm(last_week_stand_up, open_main_total, won_last_week_total, won_total,Standup_Date)
    app.destroy()

customtkinter.set_default_color_theme('green')
customtkinter.set_appearance_mode('dark')
 

app = customtkinter.CTk()
app.geometry('900x200')

app.title("CRM Report Generator")

customtkinter.CTkLabel(app, text="Last weeks standup (Submitedd for acc opening section):").grid(row=0, column=0)
last_week_entry = tk.Entry(app, width=50)
last_week_entry.grid(row=0, column=1)
customtkinter.CTkButton(app, text="Browse", command=lambda: select_file(last_week_entry)).grid(row=0, column=2)

customtkinter.CTkLabel(app, text="Open mainpipline (Total):").grid(row=1, column=0)
open_main_entry = tk.Entry(app, width=50)
open_main_entry.grid(row=1, column=1)
customtkinter.CTkButton(app, text="Browse", command=lambda: select_file(open_main_entry)).grid(row=1, column=2)

customtkinter.CTkLabel(app, text="Won pipeline (Last Week):").grid(row=2, column=0)
won_last_week_entry = tk.Entry(app, width=50)
won_last_week_entry.grid(row=2, column=1)
customtkinter.CTkButton(app, text="Browse", command=lambda: select_file(won_last_week_entry)).grid(row=2, column=2)

customtkinter.CTkLabel(app, text="Won pipeline (Last Year):").grid(row=3, column=0)
won_total_entry = tk.Entry(app, width=50)
won_total_entry.grid(row=3, column=1)
customtkinter.CTkButton(app, text="Browse", command=lambda: select_file(won_total_entry)).grid(row=3, column=2)

customtkinter.CTkLabel(app,text="Stand up meeting date:").grid(row=5,column=0)
standup_date_entry=tk.Entry(app,width=50)
standup_date_entry.grid(row=5,column=1)

customtkinter.CTkButton(app, text="Click here to generate report", command=run_wsm).grid(row=6, columnspan=3)
app.mainloop()
