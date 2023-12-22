# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 11:35:51 2022

@author: tksac
"""
#timer imports
import time
from os.path import exists
import csv
#plotter imports
# %matplotlib qt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from itertools import count
#plotter settings
# plt.style.use('fivethirtyeight')
# plt.ylim([-3, 3])
plot_data=[]
plot_labels=[]
plt.ion()
fig,ax=plt.subplots()
plt.grid(True)


#set the file name
output_folder=r'C:\Users\tksac\OneDrive\Documents\AppliedExpDes\NewMaterial'
output_file='lap_times.csv'
output_name=output_folder+'/'+output_file

#set the fields for the csv
fields=['model','start_time','end_time','trial_time']

#Create the file if it does not exist
if exists(output_name)==False:
    # open the file in the write mode
    f = open(output_name, 'w',newline='')
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(fields)
    f.close()


first_lap=True
while True:    # infinite loop
    if first_lap==True:
        first_lap=False
    else:
        user_input = input("Continue Y/N?")
        if user_input.lower() == "n":
            break  # stops the loop

    #single lap
    newlist=[]
    model=input("Enter the make/model or the configuration ID:").lower()
    newlist.append(model)
    startevent=input("Press enter when car is in start position:")
    print("Ready to record data...")
    sensor_start=input("Press enter to simulate start line")
    start_time=time.perf_counter()
    newlist.append(start_time)
    sensor_end=input("Press enter to simulate finish line")
    end_time=time.perf_counter()
    newlist.append(end_time)
    track_time=(end_time-start_time)
    newlist.append(track_time)
    #print lap times
    print(f"Start time={start_time}")
    print(f"Finish time={end_time}")
    print(f"Configuration:{model}, trial time:{track_time} seconds")
    print("End of line")
    #write to csv
    with open(output_name, 'a', newline='') as f:  
        writer = csv.writer(f)
        writer.writerow(newlist)  
        f.close()
    
    #----PLOT RESULTS----#
    plot_data.append(track_time)
    plot_labels.append(model)
    df=pd.DataFrame()
    df['trial_time']=plot_data
    df['model']=plot_labels
    labels, levels = pd.factorize(df.model)
    df['xvals']=labels
    ax.scatter(df.xvals,df.trial_time,color='dodgerblue')
    ax.set_xticks(pd.unique(labels))
    ax.set_xticklabels(levels)
    ax.set_ylabel('Time (sec)')
    ax.set_xlabel('Configuration')
    ax.set_title('Character vs. Race Time')
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)
    