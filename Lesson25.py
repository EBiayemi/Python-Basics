my_dict = {
    "cat": 5,
    "dog": 3,
    "bird": 5,
    "fish": 2,
    "horse": 5
}
print("Orginal dictoanry:", my_dict)
number = 5
frequency = 0
for item in my_dict:
    if my_dict[item] == number:
        frequency += 1
print("The frequency is:", frequency)
#Activity 3
country_code = {
    "India": "0091",
    "Australia": "0025",
    "Nepal": "00977"
}
country = "Australia"
if country in country_code:
    print("The country code for", country, "is", country_code[country])
else:
    print("Country code not found")
country = "Japan"
if country in country_code:
    print("The country code for", country, "is", country_code[country])
else:
    print("Country code not found")
#Activity 1
students = {
    "id1": {"name": "John", "grade": 10, "subject": "History"},
    "id2": {"name": "Mary", "grade": 9, "subject": "Reading"},
    "id3": {"name": "John", "grade": 10, "subject": "History"},
}
unqiue_students = {}
for student_id, student in students.items():
    if student not in unqiue_students.values():
        unqiue_students[student_id] = student
print("Students without duplicates:")
for students_id, studdent in unqiue_students.items():
    print(student_id, "=", student)