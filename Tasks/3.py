students =[
{"name": "Ahmed", "grades": [85, 90, 78]},
{"name": "Sara", "grades": [60, 88, 40]},
{"name": "Omar", "grades": [50, 75, 80]}
]
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name} - Average Grade: {average:.2f}")
