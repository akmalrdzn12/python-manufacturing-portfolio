produced = 1000
defects = 15

defect_rate = defects / produced * 100

if defect_rate <= 2:
    print("PASS - Quality Accepted")
else:
    print("FAIL - Quality Rejected")

print("Defect Rate:", defect_rate, "%")