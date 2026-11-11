
import pandas as pd

# Create production data
data = {
    "Line": ["Line A", "Line B", "Line C", "Line D"],
    "Produced": [1000, 2000, 800, 1500],
    "Defects": [50, 40, 24, 75]
}

# Convert data into a Pandas DataFrame
df = pd.DataFrame(data)

# Display production data
print("PRODUCTION DATA")
print(df)

# Calculate good units
df["Good Units"] = df["Produced"] - df["Defects"]

# Calculate defect rate
df["Defect Rate"] = (
    df["Defects"] / df["Produced"] * 100
)

print("\nPRODUCTION ANALYSIS")
print(df)
