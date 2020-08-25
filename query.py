# time format example:2020-07-02T00:00:00
#all directions: 'ne,ns,nw,es,ew,en,sw,sn,se,wn,we,ws,nrl,nlr,erl,elr,srl,slr,wrl,wlr,'

import json
import requests
from tkinter import filedialog
from api_connect import *

#####Mode 1 Query######
def mode1_query(udid, d1, d2, threshold, file_path_name):
    print('...Fetching results from server...')
    print('...This will take a while...')

    # Daily API Request
    start_date = d1 + 'T00:00:00'
    end_date = d2 + 'T00:00:00'

    daily_request = API_Connect(udid, start_date, end_date, 'ne,ns,nw,es,ew',
                                '3')
    query = daily_request.api_request()  # dictionary containing API call for daily aggregation
    # print(json.dumps(query,indent=2))

    # hourly API request
    list_peak_times = daily_request.time_phrase(1)
    hourly_query_list = []

    for i in range(len(list_peak_times) - 1):
        count = i + 1
        call = API_Connect(udid, list_peak_times[i], list_peak_times[count],
                           'ne,ns,nw,es,ew', '2').api_request()
        hourly_query_list.append(call)  # list containing hourly aggregation for all the days

    # Assigning values to analytics 1-11 #
    # 1 & 7 Daily sum
    daily_total = daily_request.sim_daily_sum(query)
    daily_total_ped = daily_request.sim_daily_sum(query, True)

    # 1 & 6 & 7  Peak Hours + Hours Above Threshold
    report_peak_hours_one = {}
    report_peak_hours_two = {}
    report_peak_hours_three = {}
    report_peak_hours_val_one = {}
    report_peak_hours_val_two = {}
    report_peak_hours_val_three = {}
    report_peak_hours_ped_one = {}
    report_peak_hours_ped_two = {}
    report_peak_hours_ped_three = {}
    report_peak_hours_ped_val_one = {}
    report_peak_hours_ped_val_two = {}
    report_peak_hours_ped_val_three = {}
    report_threshold_hours = {}
    report_threshold_hours_ped = {}
    for index in hourly_query_list: # index contains one days hourly aggregated data
        date = daily_request.extract_date(index)
        top_peak_hours = daily_request.sim_peak_hours(index)
        report_peak_hours_one.update(top_peak_hours[0])
        report_peak_hours_val_one.update(top_peak_hours[1])
        report_peak_hours_two.update(top_peak_hours[2])
        report_peak_hours_val_two.update(top_peak_hours[3])
        report_peak_hours_three.update(top_peak_hours[4])
        report_peak_hours_val_three.update(top_peak_hours[5])        
        report_threshold_hours[date] = daily_request.sim_count_hour_above_threshold(index,threshold.get())
        top_ped_peak_hours = daily_request.sim_peak_hours(index,True)
        report_peak_hours_ped_one.update(top_ped_peak_hours[0])
        report_peak_hours_ped_val_one.update(top_ped_peak_hours[1])
        report_peak_hours_ped_two.update(top_ped_peak_hours[2])
        report_peak_hours_ped_val_two.update(top_ped_peak_hours[3])
        report_peak_hours_ped_three.update(top_ped_peak_hours[4])
        report_peak_hours_ped_val_three.update(top_ped_peak_hours[5])
        report_threshold_hours_ped[date] = daily_request.sim_count_hour_above_threshold(index,threshold.get(), True)

    # 2 Daily Approach Flow
    (most_in,most_in_val,most_out,most_out_val) = daily_request.sim_peak_approach(query)

    # 3 Daily Lane Flow
    (most_used_lane, least_used_lane) = daily_request.sim_lane_sum(query)

    # 4 Daily Average Total Traffic Flow
    daily_average = daily_request.sim_avg_daily_traffic_flow(daily_total)

    # 5 Weekday Average Approach Flow
    weekday_flow = daily_request.sim_weekday_flow(query)

    # 8-11 The Most and Least Used Sidewalks
    (daily_crosswalk_flow, most_used_crosswalk, least_used_crosswalk) = daily_request.sim_ped_xing_approaches(query)

    # Printing Mode 1 Results #
    print("daily sum: ")
    print(json.dumps(daily_total, indent=2))
    print("1st Peak Hour")
    print(json.dumps(report_peak_hours_one, indent=2))
    print("1st Peak Hour Value")
    print(json.dumps(report_peak_hours_val_one, indent=2))
    print("2nd Peak Hour")
    print(json.dumps(report_peak_hours_two, indent=2))
    print("2nd Peak Hour Value")
    print(json.dumps(report_peak_hours_val_two, indent=2))
    print("3rd Peak Hour")
    print(json.dumps(report_peak_hours_three, indent=2))
    print("3rd Peak Hour Value")
    print(json.dumps(report_peak_hours_val_three, indent=2))

    print("most in flow approach: ")
    print(json.dumps(most_in, indent=2))
    print("most in flow approach values: ")
    print(json.dumps(most_in_val, indent=2))
    print("most out flow approach: ")
    print(json.dumps(most_out, indent=2))
    print("most out flow approach values: ")
    print(json.dumps(most_out_val, indent=2))

    print("most used lane: ")
    print(json.dumps(most_used_lane, indent=2))
    print("least used lane: ")
    print(json.dumps(least_used_lane, indent=2))

    print("Average daily traffic flow:")
    print(daily_average)

    # print("Average weekday daily traffic flow: ")
    print(json.dumps(weekday_flow, indent=2))

    print("No. of hour above threshold for each day: ")
    print(json.dumps(report_threshold_hours, indent=2))

    print("daily sum (pedestrian): ")
    print(json.dumps(daily_total_ped, indent=2))
    print("daily peak hours (pedestrian): ")
    print("1st Pedestrian Peak Hour")
    print(json.dumps(report_peak_hours_ped_one, indent=2))
    print("1st Pedestrian Peak Hour Value")
    print(json.dumps(report_peak_hours_ped_val_one, indent=2))
    print("2nd Pedestrian Peak Hour")
    print(json.dumps(report_peak_hours_ped_two, indent=2))
    print("2nd Pedestrian Peak Hour Value")
    print(json.dumps(report_peak_hours_ped_val_two, indent=2))
    print("3rd Pedestrian Peak Hour")
    print(json.dumps(report_peak_hours_ped_three, indent=2))
    print("3rd Pedestrian Peak Hour Value")
    print(json.dumps(report_peak_hours_ped_val_three, indent=2))

    print("most used crosswalk: ")
    print(json.dumps(most_used_crosswalk, indent=2))
    print("least used lane: ")
    print(json.dumps(least_used_crosswalk, indent=2))

    # CSV Export #
    if file_path_name != "None":
        analyzed_data = {}
        analyzed_data['Daily Sum'] = daily_total
        analyzed_data['Ped Daily Sum'] = daily_total_ped
        analyzed_data['1st Peak Hour'] = report_peak_hours_one
        analyzed_data['1st Peak Hour Value'] = report_peak_hours_val_one
        analyzed_data['2nd Peak Hour'] = report_peak_hours_two
        analyzed_data['2nd Peak Hour Value'] = report_peak_hours_val_two
        analyzed_data['3rd Peak Hour'] = report_peak_hours_three
        analyzed_data['3rd Peak Hour Value'] = report_peak_hours_val_three
        analyzed_data['1st Pedestrian Peak Hour'] = report_peak_hours_ped_one
        analyzed_data['1st Pedestrian Peak Hour Value'] = report_peak_hours_ped_val_one
        analyzed_data['2nd Pedestrian Peak Hour'] = report_peak_hours_ped_two
        analyzed_data['2nd Pedestrian Peak Hour Value'] = report_peak_hours_ped_val_two
        analyzed_data['3rd Pedestrian Peak Hour'] = report_peak_hours_ped_three
        analyzed_data['3rd Pedestrian Peak Hour Value'] = report_peak_hours_ped_val_three
        analyzed_data['Hours Over Threshold'] = report_threshold_hours
        analyzed_data['Hours Over Threshold Pedestrian'] = report_threshold_hours_ped
        analyzed_data['Most In Flow Approach'] = most_in
        analyzed_data['Most In Flow Approach Value'] = most_in_val
        analyzed_data['Most Out Flow Approach'] = most_out
        analyzed_data['Most Out Flow Approach Value'] = most_out_val
        analyzed_data['Most Used Lane'] = most_used_lane
        analyzed_data['Least Used Lane'] = least_used_lane
        analyzed_data['Most Used Crosswalk'] = {}
        analyzed_data['Least Used Crosswalk'] = {}
        # analyzed_data['Approach'] = ["north","south","east","west"]
        # analyzed_data['Weekday Flow'] = [weekday_flow[0],weekday_flow[1],weekday_flow[2],weekday_flow[3]]
        # daily_request.convertToCSV(analyzed_data, file_path_name)


#####Mode 2 Query######
def mode2_query(udid,mode,d1,t1,d2,t2,a,f,file_path_name):
    print('...Fetching results from server...')
    print('...This will take a while...')  # Daily API Request

    mode_2_request = API_Connect(udid, d1, d2, f, a, t1, t2)

    # Getting unlimited range for all types of aggregation
    list_time = mode_2_request.time_phrase(2)
    print(list_time)
    unlimited_query = []

    for index in range(len(list_time) - 1):
        count = index + 1
        queries = API_Connect(udid, list_time[index], list_time[count], f, a).api_request()
        unlimited_query.append(queries)

    # Printing Mode 2 Results #
    print(json.dumps(unlimited_query, indent=2))
    # csv export #
