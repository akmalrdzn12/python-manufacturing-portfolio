def calculate_defect_rate(produced, defects):
    defect_rate = defects / produced * 100
    return defect_rate


line_a = calculate_defect_rate(1000, 50)
line_b = calculate_defect_rate(2000, 40)
line_c = calculate_defect_rate(800, 24)

print("Line A:", line_a, "%")
print("Line B:", line_b, "%")
print("Line C:", line_c, "%")