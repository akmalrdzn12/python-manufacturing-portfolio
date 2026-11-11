
import pandas as pd

# Production data
data = {
    "Line": ["Line A", "Line B", "Line C", "Line D", "Line E"],
    "Produced": [1000, 2000, 800, 1500, 900],
    "Defects": [50, 40, 24, 75, 18]
}

df = pd.DataFrame(data)

# Calculate Good Units
df["Good Units"] = df["Produced"] - df["Defects"]

# Calculate Defect Rate
df["Defect Rate"] = (
    df["Defects"] / df["Produced"] * 100
)

# Calculate Yield Rate
df["Yield Rate"] = (
    df["Good Units"] / df["Produced"] * 100
)

# Determine Quality Status
df["Quality Status"] = df["Defect Rate"].apply(
    lambda x: "PASS" if x <= 3 else "FAIL"
)

# Display report
print("PRODUCTION PERFORMANCE REPORT")
print("==============================")
print(df.to_string(index=False))

# Overall performance
total_produced = df["Produced"].sum()
total_defects = df["Defects"].sum()
total_good_units = df["Good Units"].sum()

overall_defect_rate = total_defects / total_produced * 100
overall_yield_rate = total_good_units / total_produced * 100

print("\nOVERALL PERFORMANCE")
print("==============================")
print("Total Produced:", total_produced)
print("Total Defects:", total_defects)
print("Total Good Units:", total_good_units)
print("Overall Defect Rate:", round(overall_defect_rate, 2), "%")
print("Overall Yield Rate:", round(overall_yield_rate, 2), "%")
