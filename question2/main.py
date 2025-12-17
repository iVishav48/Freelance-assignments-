import os
import csv
import math
from collections import defaultdict
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, "temperatures")

season_months = {
    "Summer": [12, 1, 2],
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}

season_data = defaultdict(list)
station_data = defaultdict(list)

for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder, file)

        with open(path, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                temp = row["Temperature"]
                if temp == "" or temp.lower() == "nan":
                    continue

                temp = float(temp)
                station = row["Station"]
                date = datetime.strptime(row["Date"], "%Y-%m-%d")
                month = date.month

                for season, months in season_months.items():
                    if month in months:
                        season_data[season].append(temp)

                station_data[station].append(temp)

with open("average_temp.txt", "w") as f:
    for season, temps in season_data.items():
        avg = sum(temps) / len(temps)
        f.write(f"{season}: {avg:.2f}°C\n")

max_range = -1
range_stations = []

for station, temps in station_data.items():
    high = max(temps)
    low = min(temps)
    r = high - low

    if r > max_range:
        max_range = r
        range_stations = [(station, high, low)]
    elif r == max_range:
        range_stations.append((station, high, low))

with open("largest_temp_range_station.txt", "w") as f:
    for s, hi, lo in range_stations:
        f.write(
            f"Station {s}: Range {hi - lo:.2f}°C "
            f"(Max: {hi:.2f}°C, Min: {lo:.2f}°C)\n"
        )
def std_dev(values):
    mean = sum(values) / len(values)
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))

stability = {s: std_dev(t) for s, t in station_data.items()}

min_std = min(stability.values())
max_std = max(stability.values())

with open("temperature_stability_stations.txt", "w") as f:
    for s, v in stability.items():
        if v == min_std:
            f.write(f"Most Stable: Station {s} StdDev {v:.2f}°C\n")
        if v == max_std:
            f.write(f"Most Variable: Station {s} StdDev {v:.2f}°C\n")
