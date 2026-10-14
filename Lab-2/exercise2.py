marks = [75, 82, 68, 91, 55]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

print("Marks:", marks, " Total:", total, " Average:", average,
      " Highest:", highest, " Lowest:", lowest, " Courses Passed:", passed)