import pandas as pd
import csv
from datetime import datetime

cruisesfile="C:/users/bonny/downloads/cruises_names_2023.csv"
datafile="C:/users/bonny/downloads/Endeavor_2022-2023.csv"

cruises=[]
cruise_names=[]
cruise_data=[]
cruise_data_by_cruise={}

#create list of cruises with cruise, start_date, and end_date fields
with open(cruisesfile, "r", encoding='utf-8-sig', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        cruises.append(row)
        print(cruises)

def add_or_append(dictionary, key, data):
    if key in dictionary:
        dictionary[key].append(data)
    else:
        dictionary[key] = [data]

#create list of cruise names
for row in cruises:
    name=row[0]
    cruise_names.append(name)

#create list of data from cruises with date, lat, lon
with open(datafile, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        cruise_data.append(row)

#loop through cruise_data rows
for data in cruise_data:
    #loop through cruises rows
    for cruise in cruises:
        #format dates into datetime objects
        check_date=data[3]
        check_date_year=int(check_date[0:4])
        check_date_month=int(check_date[5:7])
        check_date_day=int(check_date[8:10])
        check_date=datetime(check_date_year,check_date_month,check_date_day)

        start_date=cruise[1]
        start_date_year=int(start_date[0:4])
        start_date_month=int(start_date[5:7])
        start_date_day=int(start_date[8:10])
        start_date=datetime(start_date_year,start_date_month,start_date_day)

        end_date=cruise[2]
        end_date_year=int(end_date[0:4])
        end_date_month=int(end_date[5:7])
        end_date_day=int(end_date[8:10])
        end_date=datetime(end_date_year,end_date_month,end_date_day)

        #determine which cruise a cruise_data row is part of 
        if start_date <= check_date <= end_date:
            print(data[3] + " is part of cruise " + cruise[0])
            add_or_append(cruise_data_by_cruise,cruise[0],data)
        else:
            None

for key, value in cruise_data_by_cruise.items():
    # Create a filename based on the key
    cruise = key
    csv_file = "C:/users/bonny/downloads/cruisedata_2023.csv"
    
    # Write the key-value pair to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        for key, list_of_lists in cruise_data_by_cruise.items():
            for sublist in list_of_lists:
                writer.writerow([key] + sublist)
    
    print(key + " csv dictionary exported to csv successfully")
