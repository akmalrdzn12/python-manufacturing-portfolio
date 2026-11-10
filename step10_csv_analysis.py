import csv

with open("production.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        line = row["line"]
        produced = int(row["produced"])
        defects = int(row["defects"])

        # Calculate performance
        good_units = produced - defects
        defect_rate = defects / produced * 100
        yield_rate = good_units / produced * 100

        # Display report
        print("--------------------")
        print("Production Line:", line)
        print("Produced:", produced)
        print("Defects:", defects)
        print("Good Units:", good_units)
        print("Defect Rate:", defect_rate, "%")
        print("Yield Rate:", yield_rate, "%")

