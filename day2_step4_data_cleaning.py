
import csv

clean_data = []

with open("day2_dirty_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        line = row["line"]
        produced = row["produced"]
        defects = row["defects"]

        # Check empty data
        if produced == "" or defects == "":
            print(line, "- REJECTED: Missing data")
            continue

        produced = int(produced)
        defects = int(defects)

        # Check negative production
        if produced <= 0:
            print(line, "- REJECTED: Invalid production quantity")
            continue

        # Check defects greater than production
        if defects > produced or defects < 0:
            print(line, "- REJECTED: Invalid defect quantity")
            continue

        clean_data.append({
            "line": line,
            "produced": produced,
            "defects": defects
        })

print("\nCLEAN DATA REPORT")
print("-----------------")

for row in clean_data:
    print(row)

print("\nTotal valid records:", len(clean_data))
