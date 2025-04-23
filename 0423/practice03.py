# 함수 매개변수로 함수 전달하기
def hellofunc(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕")

hellofunc(print_hello)

# map(), filter()
def power(item):
    return item * item
def under_3(item):
    return item<3

list_input_a = [1,2,3,4,5]

output_a = map(power,list_input_a)
print("map(power,list_input_a) : ", output_a)
print("map(power,list_input_a) : ", list(output_a))

output_b = filter(under_3,list_input_a)
print("filter(under_3,list_input_a) : ",output_b)
print("filter(under_3,list_input_a) : ", list(output_b))
