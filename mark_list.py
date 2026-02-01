# Input collection
student_Name = str(input("Enter student name: "))

maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
English_marks = int(input("Enter English marks: "))

# Initialize grade and status with default values
grade = "N/A"
status = "Fail"

if maths_marks < 0 or maths_marks > 100 or science_marks < 0 or science_marks > 100 or English_marks < 0 or English_marks > 100:
    print("Invalid marks entered")
    total_score = 0 # Set to 0 or handle as needed for invalid input
    average_score = 0
else:
    total_score = maths_marks + science_marks + English_marks
    average_score = total_score / 3

    if maths_marks >= 40 and science_marks >= 40 and English_marks >= 40:
        status = "Pass"
        if average_score >= 75:
            grade = "A"
        elif average_score >= 60:
            grade = "B"
        elif average_score >= 45:
            grade = "C"
    else:
        status = "Fail"
    


print(f"Student name: {student_Name}")
print(f"Total Marks: {total_score}")
print(f"Percentage: {average_score:.2f}") # Format average to 2 decimal places
print(f"status: {status}")
print(f"Grade: {grade}")
