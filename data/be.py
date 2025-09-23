import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 22, 19, 21, 20],
    "Grade": ["A", "B", "A", "C", "B"],
    "Marks": [85, 78, 92, 65, 74]
}

students_data = pd.DataFrame(data)
print("First 3 rows:\n", students_data.head(3))
print("\nName and Marks columns:\n", students_data[["Name", "Marks"]])
print("\nStudents with grade A:\n", students_data[students_data["Grade"] == "A"])
