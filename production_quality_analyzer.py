import csv


# Quality standard
MAX_DEFECT_RATE = 3


# Function to calculate performance
def calculate_performance(produced, defects):

    good_units = produced - defects
    defect_rate = defects / produced * 100
    yield_rate = good_units / produced * 100

    return good_units, defect_rate, yield_rate


# Main program
total_produced = 0
total_defects = 0
total_good_units = 0

print("====================================")
print("       PRODUCTION QUALITY ANALYZER")
print("====================================")

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
        if defect_rate <= MAX_DEFECT_RATE:
            status = "PASS"
        else:
            status = "FAIL"

        # Accumulate totals
        total_produced += produced
        total_defects += defects
        total_good_units += good_units

        # Display individual report
        print("\n------------------------------------")
        print("Production Line:", line)
        print("Produced:", produced)
        print("Defects:", defects)
        print("Good Units:", good_units)
        print("Defect Rate:", round(defect_rate, 2), "%")
        print("Yield Rate:", round(yield_rate, 2), "%")
        print("Quality Status:", status)


# Overall production summary
overall_defect_rate = total_defects / total_produced * 100
overall_yield_rate = total_good_units / total_produced * 100

print("\n====================================")
print("          OVERALL SUMMARY")
print("====================================")

print("Total Produced:", total_produced)
print("Total Defects:", total_defects)
print("Total Good Units:", total_good_units)

print("Overall Defect Rate:",
      round(overall_defect_rate, 2), "%")

print("Overall Yield Rate:",
      round(overall_yield_rate, 2), "%")

print("====================================")
print("          ANALYSIS COMPLETE")
print("====================================")