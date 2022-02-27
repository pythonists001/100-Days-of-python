## dictionary comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
import random
names = ["Alex", "Beth","Caroline","Dave","Eleanor","Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:number for (student,number) in student_scores.items() if number >= 60}
print(passed_students)