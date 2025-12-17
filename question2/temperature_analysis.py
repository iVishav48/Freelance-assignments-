import os
import csv
import math

def get_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    if month in [3, 4, 5]:
        return "Autumn"
    if month in [6, 7, 8]:
        return "Winter"
    return "Spring"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(script_dir, "temperatures")
    
    season_temps = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}
    station_temps = {}
    
    if not os.path.exists(folder):
        print(f"Error: {folder} folder not found")
        print(f"Current directory: {script_dir}")
        return
    
    csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"No CSV files found in {folder} folder")
        return
    
    print(f"Processing {len(csv_files)} CSV files...")
    
    for filename in csv_files:
        filepath = os.path.join(folder, filename)
        print(f"Reading {filename}...")
        
        try:
            with open(filepath, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    temp_str = row.get('Temperature', '').strip()
                    
                    if not temp_str or temp_str.lower() == 'nan':
                        continue
                    
                    try:
                        temperature = float(temp_str)
                    except ValueError:
                        continue
                    
                    station = row.get('Station', '').strip()
                    date_str = row.get('Date', '').strip()
                    
                    if not station or not date_str:
                        continue
                    
                    try:
                        month = int(date_str.split('-')[1])
                    except (ValueError, IndexError):
                        continue
                    
                    season = get_season(month)
                    season_temps[season].append(temperature)
                    
                    if station not in station_temps:
                        station_temps[station] = []
                    station_temps[station].append(temperature)
                    
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    output_dir = script_dir
    
    with open(os.path.join(output_dir, "average_temp.txt"), "w") as f:
        for season in ["Summer", "Autumn", "Winter", "Spring"]:
            temps = season_temps[season]
            if temps:
                avg = sum(temps) / len(temps)
                f.write(f"{season}: {avg:.1f}°C\n")
            else:
                f.write(f"{season}: No data\n")
    
    max_range = -1
    range_stations = []
    
    for station, temps in station_temps.items():
        if temps:
            temp_range = max(temps) - min(temps)
            if temp_range > max_range:
                max_range = temp_range
                range_stations = [(station, max(temps), min(temps))]
            elif temp_range == max_range:
                range_stations.append((station, max(temps), min(temps)))
    
    with open(os.path.join(output_dir, "largest_temp_range_station.txt"), "w") as f:
        for station, max_temp, min_temp in range_stations:
            f.write(f"Station {station}: Range {max_range:.1f}°C (Max: {max_temp:.1f}°C, Min: {min_temp:.1f}°C)\n")
    
    def std_dev(values):
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)
    
    station_stability = {}
    for station, temps in station_temps.items():
        if temps:
            station_stability[station] = std_dev(temps)
    
    if station_stability:
        min_std = min(station_stability.values())
        max_std = max(station_stability.values())
        
        most_stable = [s for s, std in station_stability.items() if std == min_std]
        most_variable = [s for s, std in station_stability.items() if std == max_std]
        
        with open(os.path.join(output_dir, "temperature_stability_stations.txt"), "w") as f:
            for station in most_stable:
                f.write(f"Most Stable: Station {station}: StdDev {min_std:.1f}°C\n")
            for station in most_variable:
                f.write(f"Most Variable: Station {station}: StdDev {max_std:.1f}°C\n")
    
    print(f"Temperature analysis complete!")
    print(f"Results saved to:")
    print(f"- {os.path.join(output_dir, 'average_temp.txt')}")
    print(f"- {os.path.join(output_dir, 'largest_temp_range_station.txt')}")
    print(f"- {os.path.join(output_dir, 'temperature_stability_stations.txt')}")

if __name__ == "__main__":
    main()
