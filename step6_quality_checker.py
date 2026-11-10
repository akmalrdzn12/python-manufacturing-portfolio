# Production Quality Checker

line = "Production Line A"
produced = 1000
defects = 50
maximum_defect_rate = 3

# Calculate performance
good_units = produced - defects
defect_rate = defects / produced * 100

# Display report
print("===== QUALITY REPORT =====")
print("Production Line:", line)
print("Total Produced:", produced)
print("Total Defects:", defects)
print("Good Units:", good_units)
print("Defect Rate:", defect_rate, "%")

# Quality decision
if defect_rate <= maximum_defect_rate:
    print("Status: PASS")
else:
    print("Status: FAIL")
    