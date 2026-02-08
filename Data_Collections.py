subjects = ("Math", "Science", "English")
students = ["Raj", "Priya", "Amit", "Sneha", "Karan"]
marks = {
    "Raj": {"Math": 85, "Science": 78, "English": 90},
    "Priya": {"Math": 92, "Science": 88, "English": 85},
    "Amit": {"Math": 70, "Science": 75, "English": 68},
    "Sneha": {"Math": 95, "Science": 90, "English": 92},
    "Karan": {"Math": 80, "Science": 82, "English": 78}
}
print("All Students:", students)
print("First 3 Students:", students[:3])
print()
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"
top_student = ""
highest_avg = 0
unique_grades = set()
for student in students:
    total = sum(marks[student].values())
    average = total / len(subjects)
    grade = get_grade(average)
    
    unique_grades.add(grade)
    
    print(f"{student} - Average: {average:.2f} - Grade: {grade}")
    
    if average > highest_avg:
        highest_avg = average
        top_student = student
print()
print("Top Student:", top_student)
print("Unique Grades:", unique_grades)
