import random
import csv
from datetime import datetime, timedelta

# Generate random employee IDs in the range 1600 to 1641
employee_ids = list(range(1600, 1641))

# Define the month of May and the time range
may_days = [datetime(2025, 5, day) for day in range(1, 32)]  # Adjust year as needed
time_range_start = datetime.strptime("07:15:00", "%H:%M:%S")
time_range_end = datetime.strptime("09:00:00", "%H:%M:%S")

# Generate work arrival times for each employee for all days in May
data = []
for employee_id in employee_ids:
    for day in may_days:
        # Generate a random arrival time between 07:15:00 and 09:00:00
        random_seconds = random.randint(0, int((time_range_end - time_range_start).total_seconds()))
        arrival_time = (time_range_start + timedelta(seconds=random_seconds)).time()
        
        # Expected arrival time is always 07:15:00
        expected_arrival = time_range_start.time()
        
        # Append the data
        data.append({
            "employee_id": employee_id,
            "date": day.date(),
            "work_arrival_time": arrival_time,
            "expected_arrival": expected_arrival
        })

# Save the data to a CSV file
csv_file_path = "/home/araz/projects/python/HR-Analysis/work_arrival_times.csv"
with open(csv_file_path, mode="w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["employee_id", "date", "work_arrival_time", "expected_arrival"])
    writer.writeheader()
    for entry in data:
        writer.writerow({
            "employee_id": entry["employee_id"],
            "date": entry["date"],
            "work_arrival_time": entry["work_arrival_time"],
            "expected_arrival": entry["expected_arrival"]
        })

print(f"Data saved to {csv_file_path}")