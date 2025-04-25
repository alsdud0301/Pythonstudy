class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
students = [
    Student("John", 18),
    Student("Jim", 19),
    Student("im", 23),
]

for Student in students:
    print(Student.name,Student.age)