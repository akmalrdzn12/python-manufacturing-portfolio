
import csv

with open("day2_production.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Production Line:", row["line"])
        print("Produced:", row["produced"])
        print("Defects:", row["defects"])
        print("----------------------")


import csv

production_report = [
    {"line": "Line A", "produced": 1000, "defects": 50},
    {"line": "Line B", "produced": 2000, "defects": 40},
    {"line": "Line C", "produced": 800, "defects": 24},
]

with open("production_summary.csv", "w", newline="") as file:
    fieldnames = ["line", "produced", "defects"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(production_report)

print("Production CSV report created successfully!")
