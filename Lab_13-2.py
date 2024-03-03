# Define the grades dictionary
grades = {
    "Lab 11-1": 100,
    "Lab 11-2": 100,
    "Lab 11-3": 100,
    "Lab 11-4": 100,
    "Lab 11-5": 100,
    "Lab 11-6": 100,
    "Lab 11-7": 100,
    "Lab 11-8": 100,
    "Lab 12-1": 100,
    "Lab 12-2": 100,
    "Lab 12-3": 100,
    "Lab 12-4": 100,
    "Lab 12-5": 100,
    "Lab 12-6": 100,
    "Lab 12-7": 100,
    "Lab 12-8": 100
}

# Print a list of grades received
print(list(grades.values()))

# Print the name of each assignment
for assignment in grades:
    print(assignment)

# Print the name and grade received on assignments with a grade of 70 or above
print("Grades of 70 or above:")
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

# Print the name and grade received on assignments with a grade of 50 or below
print("Grades of 50 or below:")
for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")
