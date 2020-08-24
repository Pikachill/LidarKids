# time format example:2020-07-02T00:00:00

import json
import requests
from tkinter import filedialog
from api_connect import *


#####Mode 1 Query######
def mode1_query(udid, d1, d2, threshold, print_only):
    print('...Fetching results from server...')
    print('...This will take a while...')

    # Daily API Request
    start_date = d1 + 'T00:00:00'
    end_date = d2 + 'T00:00:00'
    print(start_date)

    daily_request = API_Connect(udid, start_date, end_date, 'ne,ns,nw,es,ew,en,sw,sn,se,wn,we,ws,nrl,nlr,erl,elr,srl,slr,wrl,wlr,',
                                '3')
    query = daily_request.api_request()  # dictionary containing API call for daily aggregation
    # print(json.dumps(query,indent=2))

    # hourly API request
    list_peak_times = daily_request.time_phrase()
    hourly_query_list = []

    for i in range(len(list_peak_times) - 1):
        count = i + 1
        call = API_Connect(udid.get(), list_peak_times[i], list_peak_times[count],
                           'ne,ns,nw,es,ew,en,sw,sn,se,wn,we,ws,nrl,nlr,erl,elr,srl,slr,wrl,wlr,', '2').api_request()
        hourly_query_list.append(call)  # list containing hourly aggregation for all the days

    # Assigning values to analytics 1-11 #
    # 1 & 7 Daily sum
    daily_total = daily_request.sim_daily_sum(query)
    daily_total_ped = daily_request.sim_daily_sum(query, True)

    # 1 & 6 & 7  Peak Hours + Hours Above Threshold
    report_peak_hours = []  # A list of dictionaries
    report_peak_hours_ped = []
    report_threshold_hours = {}
    report_threshold_hours_ped = {}
    for index in hourly_query_list:  # index contains one day's + 1 hr hourly aggregated data
        date = daily_request.extract_date(index)

        top_peak_hours = daily_request.sim_peak_hours(index)
        report_peak_hours.append(top_peak_hours)
        report_threshold_hours[date] = daily_request.sim_count_hour_above_threshold(index,
                                                                                    200)  # need to change 200 to threshold.get() after it's added to the UI!!

        top_ped_peak_hours = daily_request.sim_peak_hours(index, True)
        report_peak_hours_ped.append(top_ped_peak_hours)
        report_threshold_hours_ped[date] = daily_request.sim_count_hour_above_threshold(index, threshold.get(), True)

    # 2 Daily Approach Flow
    (all_approach, most_used_approach, least_used_approach) = daily_request.sim_peak_approach(query)

    # 3 Daily Lane Flow
    (daily_lane_flow, most_used_lane, least_used_lane) = daily_request.sim_lane_sum(query)

    # 4 Daily Average Total Flow
    daily_average = daily_request.sim_avg_daily_traffic_flow(query)

    # 5 Weekday Average Approach Flow
    weekday_flow = daily_request.sim_weekday_flow(query)

    # 8-11 The Most and Least Used Sidewalks
    (daily_crosswalk_flow, most_used_crosswalk, least_used_crosswalk) = daily_request.sim_ped_xing_approaches(query)

    # Printing Mode 1 Results #
    print("daily sum: ")
    print(json.dumps(daily_total, indent=2))
    print("daily peak hours: ")
    print(json.dumps(report_peak_hours, indent=2))

    print("daily approach flow: ")
    print(json.dumps(all_approach, indent=2))
    print("most used approaches: ")
    print(json.dumps(most_used_approach, indent=2))
    print("least used approaches: ")
    print(json.dumps(least_used_approach, indent=2))

    print("most used lane: ")
    print(json.dumps(most_used_lane, indent=2))
    print("least used lane: ")
    print(json.dumps(least_used_lane, indent=2))

    print("Average daily traffic flow:")
    print(daily_average)

    print("Average weekday daily traffic & pedestrian flow: ")
    print(json.dumps(weekday_flow, indent=2))

    print("No. of hour above threshold for each day: ")
    print(json.dumps(report_threshold_hours, indent=2))

    print("daily sum (pedestrian): ")
    print(json.dumps(daily_total_ped, indent=2))
    print("daily peak hours (pedestrian): ")
    print(json.dumps(report_peak_hours_ped, indent=2))

    print("most used crosswalk: ")
    print(json.dumps(most_used_crosswalk, indent=2))
    print("least used lane: ")
    print(json.dumps(least_used_crosswalk, indent=2))

    # csv export #
    if print_only == False:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        analyzed_data = {}
        analyzed_data['Daily Sum'] = daily_total
        analyzed_data['Ped Daily Sum'] = daily_total_ped
        daily_request.convertToCSV(analyzed_data, export_file_path)


#####Mode 2 Query######
def mode2_query(udid, mode, d1, t1, d2, t2, a, f, print_only):
    print('...Fetching results from server...')
    print('...This will take a while...')  # Daily API Request

    mode_2_request = API_Connect(udid, d1, d2, f, a, t1, t2)

    # Getting unlimited range for all types of aggregation
    list_time = mode_2_request.time_phrase()
    unlimited_query = []

    for index in range(len(list_time) - 1):
        count = index + 1
        queries = API_Connect(udid, list_time[index], list_time[count], f, a).api_request()
        unlimited_query.append(queries)

    # Printing Mode 2 Results #
    print(json.dumps(unlimited_query, indent=2))
    # csv export #
