
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def to_string(self):
        return "{}\t{}".format(self.name, self.age)


students = [
        Student("홍길동",30),
        Student("김길동", 25),
        Student("이길동", 28),
        Student("빅길동", 22),
]

for student in students:
    print(student.to_string())