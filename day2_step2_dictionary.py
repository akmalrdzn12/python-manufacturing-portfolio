
production = {
    "line": "Line A",
    "produced": 1000,
    "defects": 50
}

print("PRODUCTION REPORT")
print("-----------------")

print("Production Line:", production["line"])
print("Total Produced:", production["produced"])
print("Total Defects:", production["defects"])

good_units = production["produced"] - production["defects"]

defect_rate = (
    production["defects"] / production["produced"]
) * 100

print("Good Units:", good_units)
print("Defect Rate:", round(defect_rate, 2), "%")

production["defects"] = 30

print(production["defects"])

production["shift"] = "Night Shift"

print(production["shift"])