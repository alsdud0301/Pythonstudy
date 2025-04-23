# 튜플은 내부 요소 변경 불가
tuple_test = (10,20,30)

print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])

# 요소를 하나만 가진 튜플
# tuple_one_x = (123) -> 이렇게 선언하면 숫자를 괄호로 감싼 것으로 인식하여 요소 뒤에 쉼표를 넣어 선언
tuple_one = (123,)

# 괄호가 없는 튜플
tuple_test2 = 10,20,30,40
print("tuple_test2 : ", tuple_test2)
print("type(tuple_test2) : ", type(tuple_test2))

# 괄호가 없는 튜플
a,b,c = 10,20,30
print("a,b,c : ", a,b,c)