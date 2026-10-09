grades = {
    "John": 85,
    "Mary": 92,
    "David": 76,
    "Sarah": 88,
    "Peter": 67
}
total = 0
for score in grades.values():
    total += score
average = total / len(grades)
print("Student Grade Book")
print("Class Average:", round(average, 2))
top_student = max(grades, key=grades.get)
bottom_student = min(grades, key=grades.get)
print("Highest Scorer:", top_student, "-", grades[top_student])
print("Lowest Scorer:", bottom_student, "-", grades[bottom_student])
student_name = input("Enter a student's name to find their grade: ")
score = grades.get(student_name)
if score is not None:
    print(student_name, "'s grade is:", score)
else:
    print("Sorry student not found please check the name and try again")