produced = 1000
defects = 50

good_units = produced - defects
defect_rate = defects / produced * 100

print("Total Produced:", produced)
print("Total Defects:", defects)
print("Good Units:", good_units)
print("Defect Rate:", defect_rate)