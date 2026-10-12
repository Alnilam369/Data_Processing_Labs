name = input("Enter student name: ")

a = float(input("course 1: "))
b = float(input("course 2: "))
c = float(input("course 3: "))
d = float(input("course 4: "))
e = float(input("course 5: "))

total = a + b + c + d + e
average = total / 5

highest = max(a, b, c, d, e)
lowest = min(a, b, c, d, e)

passed = 0

if a >= 50:
    passed += 1
if b >= 50:
    passed += 1
if c >= 50:
    passed += 1
if d >= 50:
    passed += 1
if e >= 50:
    passed += 1

if average >= 80:
    performance = "Excellent"
elif average >= 70:
    performance = "Good"
elif average >= 60:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("Student Name:", name, "Total:", total,
      "Average:", average, "Highest Mark:", highest, "Lowest Mark:", lowest,
      "Passed Courses:", passed, "Performance:", performance)