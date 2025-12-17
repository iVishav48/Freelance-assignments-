# Question 2 - Temperature Data Analysis

This question involves analyzing temperature data from multiple weather stations to extract statistical insights.

## Problem Description
Process CSV files containing temperature readings from various weather stations and perform seasonal analysis, identify temperature ranges, and calculate stability metrics.

## Data Structure
- Input files located in `temperatures/` directory
- CSV format with columns: `Date`, `Station`, `Temperature`
- Seasons defined for Southern Hemisphere:
  - **Summer**: December, January, February
  - **Autumn**: March, April, May
  - **Winter**: June, July, August
  - **Spring**: September, October, November

## Analysis Performed

### 1. Seasonal Temperature Averages
- Calculate average temperature for each season across all stations
- Output: `average_temp.txt`

### 2. Largest Temperature Range
- Find station(s) with maximum temperature difference (max - min)
- Output: `largest_temp_range_station.txt`

### 3. Temperature Stability Analysis
- Calculate standard deviation for each station
- Identify most stable (lowest std dev) and most variable (highest std dev) stations
- Output: `temperature_stability_stations.txt`

## Implementations
- `main.py` - Efficient implementation using defaultdict and built-in functions
- `main2.py` - Detailed implementation with explicit calculations

## Usage
1. Ensure temperature CSV files are in the `temperatures/` directory
2. Run either `main.py` or `main2.py`
3. Results will be written to text files in the current directory

## Output Files
- `average_temp.txt` - Seasonal temperature averages
- `largest_temp_range_station.txt` - Station with largest temperature range
- `temperature_stability_stations.txt` - Most stable and variable stations
