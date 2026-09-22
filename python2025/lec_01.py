#DataType
# message = "Hello World"
# score = 23
# cgpa = 8.98
# active = False
# list_of_subjects = ["Web D", "SWE", "EVS", 12, 34.98, True]
# location_of_college = ("Gurugram", "Pune",[2,3])
# data_of_student = {
#     'student_name' : "Archit",
#     'enrollment_no': 20251200,
#     'batch':2025,
#     'cgpa' : cgpa,
#     'active' : active
# }


# print(type(message))
# print(type(score))
# print(type(cgpa))
# print(type(active))
# print(type(list_of_subjects))
# print(type(location_of_college))
# print(type(data_of_student))


# Formatted String
# friend = "Aniket"
# print(f"Hello {data_of_student['student_name']}.\t Your College is in {location_of_college[0]}. \n Your scoring Subject is {list_of_subjects[1]}")




# Conditional Statement
# points = 268
# time = 4.56

# if points >=100 and time < 2:
#     print("A : Congratulations..")
# elif time<1 :
#     print("C: You're Supreme :)")
# elif points > 200:
#     print("Master Of Game :p")
# else:
#     print("B : You can Play Better..!!")



# Iterations - FOR LOOP
# good_students = ['Sumit', 'Kashvi', 'Hanu', 'Kiyana', 'Aryan']

# for student in good_students :
#     print(f"{student}", end="\t")

# Iterations through two Lists
# good_students = ['Sumit', 'Kashvi', 'Hanu', 'Kiyana', 'Aryan']
# courses = ["SWE", "Web Dev", "Cybersecurity", "AI Engg", "Medical Science"]

# for student,sbj in zip(good_students, courses) :
#     print(f"{student} : {sbj}")

# Iteration : WHILE LOOP
# list = [["w", "w", "w", "w", "w", "w", "*", "w", "w", "w"]]

# i = 0
# while i<len(list):
#     if list[i] == "w":
#         print("I got a W")
#         i += 1
#     else:
#         print("I got a STAR")
#         i += 1




# ----------------------
# | PROBLEM OF THE DAY  |
# ----------------------
# list = [
#     ["w", "w", "w", "w", "w", "w", "w"],
#     ["w", "w", "w", "w", "w", "w", "w"],
#     ["w", "w", "w", "w", "w", "w", "w"],
#     ["w", "w", "w", "w", "*", "w", "w"],
#     ["w", "w", "w", "w", "w", "w", "w"]
#     ]

# OUTPUT : I got star at (3,4)



# score = [2, 4, 7, 4.5, 23, 10, 87]

# for i in range (len(score)):
#     print(score[i]*2)
