#객체를 처리하는 함수
def create_student(name,age):
    return {
        "name":name,
        "age":age
    }
def student_to_string(student):
    return "{}\t{}".format(student["name"],student["age"])

students = [
    create_student("John",20),
    create_student("Mark",25),
    create_student("Alice",30)
]


for student in students:
    print(student_to_string(student))