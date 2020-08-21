# Check-out: Akhil_08-05; Poom_08-05; Sathvik_08-20T0500
# time format:2020-07-02T00:00:00 2020-06-22T00:00:00

import json
import requests
from tkinter import *
from tkinter import filedialog
from heapq import nlargest
from api_connectAug20 import * #make sure the import file name is updated!

def query():
    print('...LOADING...')
    print('...This will take a while...')

    # user request .csv file path
    # export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')

    # Daily API Request
    daily_request = API_Connect(udid.get(), d1.get(), d2.get(), 'ne,ns,nw,es,ew,en,sw,sn,se,wn,we,ws,nrl,nlr,erl,elr,srl,slr,wrl,wlr,', '3')
    query = daily_request.api_request() # dictionary containing API call for daily aggregation 
    # print(json.dumps(query,indent=2))
    
    # hourly API request
    list_peak_times = daily_request.time_pharse()
    hourly_query_list = [] 

    for i in range(len(list_peak_times) - 1):
        count = i + 1
        call = API_Connect(udid.get(), list_peak_times[i], list_peak_times[count], 'ne,ns,nw,es,ew,en,sw,sn,se,wn,we,ws,nrl,nlr,erl,elr,srl,slr,wrl,wlr,', '2').api_request()
        hourly_query_list.append(call) # list containing hourly aggregation for all the days

    # Daily sum
    daily_total = daily_request.sim_daily_sum(query)
    daily_total_ped = daily_request.sim_daily_sum(query,True)

    # Peak Hours
    #report_peak_hours = [] # A list of maps/ dictionaries
    #report_peak_hours_ped = []
    #report_threshold_hours = {}
    #report_threshold_hours_ped = {}
    #for index in hourly_query_list: # index contains one day's + 1 hr hourly aggregated data
        #date = daily_request.extract_date(index)
        #for vehicles
        #top_peak_hours = daily_request.sim_peak_hours(index)
        #report_peak_hours.append(top_peak_hours)
        #report_threshold_hours[date] = daily_request.sim_count_hour_above_threshold(index,200) #need to change 200 to threshold.get() after it's added to the UI!!
        ##for pedestrians
        # top_ped_peak_hours = daily_request.sim_peak_hours(index,True)
        # report_peak_hours_ped.append(top_ped_peak_hours)
        # report_threshold_hours_ped[date] = daily_request.sim_count_hour_above_threshold(index,threshold.get(), True)

    # Daily Approach Flow
    # (all_approach,most_used_approach,least_used_approach) = daily_request.sim_peak_approach(query)

    # Daily Lane Flow
    # (daily_lane_flow, most_used_lane, least_used_lane) = daily_request.sim_lane_sum(query)

    # Daily Average Lane Flow
    # daily_average=daily_request.sim_avg_daily_traffic_flow(query)

    # Weekday Flow
    # weekday_flow=daily_request.sim_weekday_flow(query)

    ### Test Print Statements ###
    print("daily sum: ")
    print(json.dumps(daily_total, indent=2))
    dict

    # print("daily sum (pedestrian): ")
    # print(json.dumps(daily_total_ped, indent=2))
    # dict

    #print("daily peak hours: ")
    #print(json.dumps(report_peak_hours, indent=2))
    # print(type(report_peak_hours))
    # print(type(report_peak_hours[0]))
    # print(type(report_peak_hours[1]))
    # print(type(report_peak_hours[2]))
    # print(type(report_peak_hours[3]))
    # print(type(report_peak_hours[4]))

    # print("daily peak hours (pedestrian): ")
    # print(json.dumps(report_peak_hours_ped, indent=2))

    # print("daily approach flow: ")
    # print(json.dumps(all_approach, indent=2))
    # print("most used approaches: ")
    # print(json.dumps(most_used_approach, indent=2))
    # print("least used approaches: ")
    # print(json.dumps(least_used_approach, indent=2))

    # print ("Average traffic flow")
    # print(daily_average)

    # Weekday traffic flow
    # print("Weekly traffic flow: ")
    # print(json.dumps(weekday_flow, indent=2))
    # dict

    # print("daily lane flow: ")
    # print(json.dumps(daily_lane_flow, indent=2))
    # print("most used lane: ")
    # print(json.dumps(most_used_lane, indent=2))
    # print("least used lane: ")
    # print(json.dumps(least_used_lane, indent=2))

    #print("daily no. of hour above threshold: ")
    #print(json.dumps(report_threshold_hours, indent=2))

    # csv export
    # analyzed_data = {}
    # analyzed_data['Daily Sum'] = daily_total
    # analyzed_data['Ped Daily Sum'] = daily_total_ped
    # daily_request.convertToCSV(analyzed_data, export_file_path)

# Main GUI window
root = Tk()

udid = StringVar(None, ' ')
mode = StringVar(None, ' ')
#threshold = IntVar()

# Title
Label(root,text= 'Aggregated Data Report').grid(row=0,column=0,columnspan=3,sticky='w')
Label(text='').grid(row=1,column=0)

# UDID selection
uLabel = Label(root, text='Choose Intersection:')
uLabel.grid(row=2, column=0, sticky='w')
u1 = Radiobutton(root, text='Bernard Ave. & Pandosy St.', variable=udid, value='BCT_3D_5G_0101001')
u1.grid(row=3, column=0, sticky='w',padx=10)
u2 = Radiobutton(root, text='Bernard Ave. & Water St.', variable=udid, value='BCT_3D_5G_0101002')
u2.grid(row=4, column=0, sticky='w',padx=10)

# Mode Selection
Label(root, text='Mode Selection:').grid(row=5,column=0,sticky='w')
m1 = Radiobutton(root, text='Simplified', variable=mode, value='simplified')
m1.grid(row=6,column=0,padx=10, sticky='w')
m2 = Radiobutton(root, text='Custom', variable=mode, value='custom')
m2.grid(row=7,column=0,padx=10, sticky='w')


# Date range input

Label(root, text='Enter start and end date').grid(row=8,column=0,sticky='w')
d1 = Entry(root)
d1.grid(row=9,column=0,pady=10, sticky='ew')
d2 = Entry(root)
d2.grid(row=10,column=0,pady=10, sticky='ew')

confirmButton = Button(root, text='Confirm', command=query).grid(row=11,column=0,sticky='w')

root.mainloop()