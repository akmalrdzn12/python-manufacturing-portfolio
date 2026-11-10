import csv

with open("production.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)