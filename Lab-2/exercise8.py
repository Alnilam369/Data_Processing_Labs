students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]


def calculate_average(students):
    total = 0

    for student in students:
        total += student["marks"]

    return total / len(students)


def highest_marks_student(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest


def count_low_attendance(students):
    count = 0

    for student in students:
        if student["attendance"] < 80:
            count += 1

    return count


average = calculate_average(students)
highest = highest_marks_student(students)
low_attendance = count_low_attendance(students)

print("Average Marks:", average)
print("Highest Marks Student:", highest["name"])
print("Highest Marks:", highest["marks"])
print("Students with Attendance Below 80%:", low_attendance)