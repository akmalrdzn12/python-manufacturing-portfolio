
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


for number in [10, 20, 30]:
    if number == 20:
        continue

    print(number)

    clean_data = []

clean_data.append("Line A")
clean_data.append("Line B")

print(clean_data)

produced = 100

if produced <= 100:
    print("Production is 100 or below")


    status = "FAIL"

if status != "PASS":
    print("Check production quality")

    production_lines = ["Line A", "Line B", "Line C",'line D']

print(len(production_lines))
