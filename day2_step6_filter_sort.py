
import pandas as pd

data = {
    "Line": ["Line A", "Line B", "Line C", "Line D", "Line E"],
    "Produced": [1000, 2000, 800, 1500, 900],
    "Defects": [50, 40, 24, 75, 18]
}

df = pd.DataFrame(data)

# Calculate defect rate
df["Defect Rate"] = df["Defects"] / df["Produced"] * 100

print("COMPLETE PRODUCTION DATA")
print(df)

# Filter defect rate above 3%
high_defect = df[df["Defect Rate"] > 3]

print("\nHIGH DEFECT PRODUCTION LINES")
print(high_defect)

# Sort by defect rate, highest first
sorted_data = df.sort_values(
    by="Defect Rate",
    ascending=False
)

print("\nRANKING BY DEFECT RATE")
print(sorted_data)
