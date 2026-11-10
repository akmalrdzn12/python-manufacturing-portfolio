import csv


# Function to calculate production performance
def calculate_performance(produced, defects):

    good_units = produced - defects
    defect_rate = defects / produced * 100
    yield_rate = good_units / produced * 100

    return good_units, defect_rate, yield_rate


# Read production CSV file
with open("production.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        line = row["line"]
        produced = int(row["produced"])
        defects = int(row["defects"])

        # Calculate performance
        good_units, defect_rate, yield_rate = calculate_performance(
            produced, defects
        )

        # Quality decision
        if defect_rate <= 3:
            status = "PASS"
        else:
            status = "FAIL"

        # Display report
        print("==========================")
        print("Production Line:", line)
        print("Produced:", produced)
        print("Defects:", defects)
        print("Good Units:", good_units)
        print("Defect Rate:", round(defect_rate, 2), "%")
        print("Yield Rate:", round(yield_rate, 2), "%")
        print("Quality Status:", status)
   