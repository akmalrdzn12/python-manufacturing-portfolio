
production_lines = ["Line A", "Line B", "Line C", "Line D", "Line E"]

defects = [50, 40, 24, 75, 18]

print("PRODUCTION DEFECT REPORT")
print("------------------------")

print("All production lines:", production_lines)
print("All defect quantities:", defects)

print("\nFirst production line:", production_lines[0])
print("First defect quantity:", defects[0])

print("\nLast production line:", production_lines[4])
print("Last defect quantity:", defects[4])

print("\nTotal defects:", sum(defects))
print("Number of production lines:", len(production_lines))
