students = {}

print(students)

students["Mon"] = 23
students["Uriah"] = 21
students["Kerelly"] = 20
students["Jelly"] = 20
students["Josh"] = 22
students["Althea"] = 19
students["Den"] = 21
students["Jesha"] = 20
students["Loida"] = 20
students["Janna"] = 20
students["Philoy"] = 24
students["Rhizzalyn Ann M Close"] = 19.99999
students["Lee Min"] = 19
students["Daphne"] = 20
students["Jellah"] = 19
students["Ivan"] = 19
students["Wayne"] = 20

print(students)

"""
student_name = input("\nName of classmate: ")
age = students.get(student_name, 0)
print(f"The age of {student_name} is {age} years old.")
"""

names = students.keys()
names = list(students.keys())
names = sorted(names, reverse=True)
print(names)


population = len(students)
print(f"Class size is {population} students.")