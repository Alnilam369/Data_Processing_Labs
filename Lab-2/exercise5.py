student = {
    "name": "Sara",
    "id": "26-12457-1",
    "department": "Data Science",
    "cgpa": 3.25
}

for key, value in student.items():
    print(key, ":", value)

if student["cgpa"] >= 2.50:
    print("Good Standing")
else:
    print("Academic Warning")