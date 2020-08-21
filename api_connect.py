# Check-out: Akhil_08-05; Poom_08-06; Colleen_08-16; Sathvik_08-16T2100; 
# Colleen_08_17_21:30 added functions to split timestamps

import json
import requests
from heapq import nlargest
from heapq import nsmallest
import datetime

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


class API_Connect():
    simplified = '1'
    token = "WJe_wI2r9-dtJsR83i77yQgKo3bsnqStOP6Xf604Y6JRTzd3D0jLsg0ZaGSwUeCaUBMFR1MWHgGwGjXN"
    all_direction = ['ne', 'ns', 'nw', 'es', 'ew', 'en', 'sw', 'sn', 'se', 'wn', 'we', 'ws']
    lane_direction_UDID1 = {'n1':['ns','nw'],'n2':['ne'],'n3':['wn','sn','en'],'s1':['sn','se'],'s2':['sw'],'s3':['es','ns','ws'],'e1':['ew','en'],'e2':['es'],'e3':['ne','we','se'],'w1':['we','ws'],'w2':['wn'],'w3':['sw','ew','nw']}
    lane_direction_UDID2 = {'n1':['ne','nw','ns'],'n2':['sn','en','wn'],'s1':['ws','es','ns'],'s2':['sw','se','sn'],'e1':['en','ew'],'e2':['es'],'e3':['ne','we','se'],'w1':['we','ws'],'w2':['wn'],'w3':['nw','ew','sw']}
    ped_direction = ['nrl','nlr','erl','elr','srl','slr','wrl','wlr']
    approach_direction = {'north':['ns','nw','ne'],'south':['sn','se','sw'],'east':['ew','en','es'],'west':['we','ws','wn']}
    side_walk_approach = ['n','s','e','w']

   #initiates all the attributes that belong to the object "self"
    def __init__(self, UDID, fdate, tdate, fields, aggregation):
        self.UDID = UDID
        self.fdate = fdate
        self.tdate = tdate
        self.fields = fields
        self.aggregation = aggregation

    def api_request(self):
        parameters = {"UDID": self.UDID, "fdate": self.fdate, "tdate": self.tdate, "f": self.fields, "a": self.aggregation, "simplified": self.simplified}
        response = requests.get('https://api.bluecitytechnology.com/s/ad', params=parameters, auth=BearerAuth(self.token))
        dictionay_response = json.loads(response.text) #extracts the response in "text" format

        return dictionay_response['values'] #the responses contains other info, but 'values' contains the date and the flows

    #constructs date type objects from the "YYYY-MM-DD" input strings
    def time_pharse(self):
        start_date = datetime.datetime.fromisoformat(self.fdate)
        end_date = datetime.datetime.fromisoformat(self.tdate)
        difference = end_date - start_date
        count = 0

        time_skip = []

        for increment in range(difference.days + 2): #difference is an object with class datetime   
            temp = start_date.date() + datetime.timedelta(days=count)
            date_string = temp.strftime('%Y-%m-%d')
            ret_val = date_string + 'T00:00:00' #comebines the date string and time string to make a timestamp string
            time_skip.append(ret_val) #adds the newly generated timestamp string to the list
            count += 1
        return time_skip #generate a list of timestamps for 0:00 on each day in the range
    
    #outputs a date list from a timestamp list (both are strings)
    def extract_date(self, result):
        key = list(result.keys())[0]
        date_only = key.split(' ', 1)[0]
        return date_only

    #outputs a time list from a timestamp list (both are strings)
    def extract_time(self, result):
        key = list(result.keys())[0]
        time_only = key.split(' ', 1)[1]
        return time_only

    #Functions to output analytics 
    #Simplified Mode Item No.1 / 7 a - Daily Sum
    def sim_daily_sum(self,result,ped_xing=False): #default value of ped_xing is False; an example of result is 'values'
        daily_sum = {}
        if ped_xing:
            isPed_xing = self.ped_direction
        else:
            isPed_xing = self.all_direction

        for date in result:
            total = 0
            for direction in isPed_xing:
                # check for missing key(s)
                if direction in result[date]:
                    temp = result[date][direction]
                    total += temp
            daily_sum[date] = total

        return daily_sum

    #Simpliefied Mode Item No.1 / 7 b-g, top 3 peak hour names & values
    def sim_peak_hours(self,result,ped_xing_peak=False):
        all_hours = {}
        ret_val = {}
        count = 0

        if ped_xing_peak:
            isPed_xing_peak = self.ped_direction
        else:
            isPed_xing_peak = self.all_direction

        for hour in result:
            total = 0
            for direction in isPed_xing_peak: #this loop adds up all directions' flow for one hour
                # check for missing key(s)
                if direction in result[hour]:
                    temp = result[hour][direction] #extracts flow for one particular direction for one hour
                    total += temp #add flow for one particular direction for that hour to the hourly total

            if count < 24:
                all_hours[hour] = total #stores one hourly flow in the dictionary
            elif count == 24: #stop when 24 hourly flows have been stored
                three_daily_peaks = nlargest(3, all_hours, key=all_hours.get) #three_daily_peaks is a list that contains the name of the 3 peak hours

                for timestamp in three_daily_peaks: #goes through each entry in the list three_daily_peaks
                    ret_val[timestamp] = all_hours[timestamp] #assigning values for the 3 peak hours using the all_hours dictionary

                all_hours.clear() #this happens when the loop has been executed for 24 times in a day and the 3 peaks have been stored
                all_hours[hour] = total
                count = 0 #so that we can move onto the next day with count initialized

            count += 1

        return ret_val

    #Simplified Mode Item No.2 - Approach Flows
    def sim_peak_approach(self,result):
        all_approach = {}
        most_approach = {}
        least_approach = {}
        count = 0

        for date in result:
            temp_dict = {}

            for approach in self.approach_direction.keys():
                total = 0
                for field in self.approach_direction[approach]:
                    # check for missing key(s)
                    if field in result[date]:
                        temp = result[date][field]
                        total += temp
                
                temp_dict[approach] = total
            most_used = nlargest(1, temp_dict, key=temp_dict.get)
            least_used = nsmallest(1, temp_dict, key=temp_dict.get)

            all_approach[date] = temp_dict
            most_approach[date] = most_used
            least_approach[date] = least_used     

        return (all_approach,most_approach,least_approach)

    #Simplified Mode Item No.3 - Lane Flows
    def sim_lane_sum(self,result):
        all_lane = {}
        most_used_lane = {}
        least_used_lane = {}

        if self.UDID == "BCT_3D_5G_0101001":
            lane_sum = self.lane_direction_UDID1
        else:
            lane_sum = self.lane_direction_UDID2

        for date in result:
            temp_dict = {}
            for lanes in lane_sum.keys():
                total = 0
                for index in lane_sum[lanes]:
                    if index in result[date]:
                        temp = result[date][index]
                        total += temp
                temp_dict[lanes] = total
            most_used = nlargest(1, temp_dict, key=temp_dict.get)
            least_used = nsmallest(1, temp_dict, key=temp_dict.get)

            all_lane[date] = temp_dict
            most_used_lane[date] = most_used
            least_used_lane[date] = least_used

        return (all_lane,most_used_lane,least_used_lane)

    #Simplified Mode Item No.4
    def sim_avg_daily_traffic_flow(self,result,ped_xing_avg=False):
        daily_average=0
        total=0
        no_of_days=0
        for date in result:
            sum+=1
            total+=self.sim_daily_sum(result,ped_xing_avg)
        daily_average=total/no_of_days
        return daily_average

    #Simplified Mode Item No.5
    def sim_weekday_flow(self,result):
        for date in result:
            temp_dict = {}
            if (date.weekday()<5):
                for approach in self.approach_direction.keys():
                    total = 0
                    for field in self.approach_direction[approach]:
                        # check for missing key(s)
                        if field in result[date]:
                            temp = result[date][field]
                            total += temp
                
                    temp_dict[approach] = total
        return temp_dict
        
    #Simplified Mode Item No.6
    def sim_count_hour_above_threshold(self,result,threshold,ped_xing_peak=False):
        all_hours = {}
        count = 0
        tally = 0

        if ped_xing_peak:
            isPed_xing_peak = self.ped_direction
        else:
            isPed_xing_peak = self.all_direction

        for hour in result:
            total = 0
            for direction in isPed_xing_peak: #this loop adds up all directions' flow for one hour
                # check for missing key(s)
                if direction in result[hour]:
                    temp = result[hour][direction] #extracts flow for one particular direction for one hour
                    total += temp #add flow for one particular direction for that hour to the hourly total

            if count < 24:
                all_hours[hour] = total #stores one hourly flow in the dictionary
                if total > threshold:
                  tally += 1
            elif count == 24: #stop when 24 hourly flows have been stored in the all_hours dictionary
                hour_above_threshold = tally
                
                all_hours.clear() #this happens when the loop has been executed for 24 times in a day and the 3 peaks have been stored
                all_hours[hour] = total #a dictionary with only one key being the midnight of the second day and the value for midnight e.g. {"2020-06-30 00:00:00": 32}
                count = 0 #so that we can move onto the next day with count initialized

            count += 1

        return hour_above_threshold  #returns an integer for one day

    #Simplified Mode Item No. 8 - 11
    def ped_xing_approaches(self, result):
        all_approach_sum = {}
        most_used_approach = {}
        least_used_approach = {}
        ped_direction = ['nrl','nlr','srl','slr','erl','elr','wrl','wlr']

        for date in result:
            temp_dict = {}
            for approaches in self.side_walk_approach:
                total = 0
                for index in ped_direction:
                    if index.startswith(approaches):
                        temp = result[date][index]
                        total += temp
                temp_dict[approaches] = total
            most_used = nlargest(1, temp_dict, key=temp_dict.get)
            least_used = nsmallest(1, temp_dict, key=temp_dict.get)

            all_approach_sum[date] = temp_dict
            most_used_approach[date] = most_used
            least_used_approach[date] = least_used

        return(all_approach_sum,most_used_approach, least_used_approach)
        
    def convertToCSV(self, data, export_file_path):
            r = pd.DataFrame.from_dict(data)
            r.to_csv(export_file_path)



