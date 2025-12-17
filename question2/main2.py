import os
import csv
import math

folder = "temperatures"

seasons = {
    "Summer": [12, 1, 2],
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}

season_temps = {}
season_temps["Summer"] = []
season_temps["Autumn"] = []
season_temps["Winter"] = []
season_temps["Spring"] = []

station_temps = {}

all_files = os.listdir(folder)

for file in all_files:
    if file.endswith(".csv"):
        full_path = folder + "/" + file
        
        f = open(full_path, "r")
        reader = csv.DictReader(f)
        
        for row in reader:
            temp = row["Temperature"]
            
            if temp == "":
                continue
            
            if temp == "nan":
                continue
            
            if temp == "NaN":
                continue
            
            temp = float(temp)
            station = row["Station"]
            date = row["Date"]
            
            parts = date.split("-")
            month = int(parts[1])
            
            if month == 12 or month == 1 or month == 2:
                season_temps["Summer"].append(temp)
            
            if month == 3 or month == 4 or month == 5:
                season_temps["Autumn"].append(temp)
            
            if month == 6 or month == 7 or month == 8:
                season_temps["Winter"].append(temp)
            
            if month == 9 or month == 10 or month == 11:
                season_temps["Spring"].append(temp)
            
            if station not in station_temps:
                station_temps[station] = []
            
            station_temps[station].append(temp)
        
        f.close()

f1 = open("average_temp.txt", "w")

for s in season_temps:
    temps = season_temps[s]
    total = 0
    for t in temps:
        total = total + t
    avg = total / len(temps)
    line = s + ": " + str(round(avg, 2)) + "°C\n"
    f1.write(line)
    print(line)

f1.close()

max_range = 0
best_station = ""
best_max = 0
best_min = 0

for station in station_temps:
    temps = station_temps[station]
    
    highest = temps[0]
    for t in temps:
        if t > highest:
            highest = t
    
    lowest = temps[0]
    for t in temps:
        if t < lowest:
            lowest = t
    
    range_val = highest - lowest
    
    if range_val > max_range:
        max_range = range_val
        best_station = station
        best_max = highest
        best_min = lowest

f2 = open("largest_temp_range_station.txt", "w")
line = "Station " + best_station + ": Range " + str(round(max_range, 2)) + "°C (Max: " + str(round(best_max, 2)) + "°C, Min: " + str(round(best_min, 2)) + "°C)\n"
f2.write(line)
print(line)
f2.close()

station_stddev = {}

for station in station_temps:
    temps = station_temps[station]
    
    total = 0
    for t in temps:
        total = total + t
    mean = total / len(temps)
    
    sum_sq = 0
    for t in temps:
        diff = t - mean
        sq = diff * diff
        sum_sq = sum_sq + sq
    
    variance = sum_sq / len(temps)
    stddev = math.sqrt(variance)
    
    station_stddev[station] = stddev

min_std = 999999
max_std = -1
stable_station = ""
variable_station = ""

for station in station_stddev:
    std = station_stddev[station]
    
    if std < min_std:
        min_std = std
        stable_station = station
    
    if std > max_std:
        max_std = std
        variable_station = station

f3 = open("temperature_stability_stations.txt", "w")
line1 = "Most Stable: Station " + stable_station + " StdDev " + str(round(min_std, 2)) + "°C\n"
line2 = "Most Variable: Station " + variable_station + " StdDev " + str(round(max_std, 2)) + "°C\n"
f3.write(line1)
f3.write(line2)
print(line1)
print(line2)
f3.close()