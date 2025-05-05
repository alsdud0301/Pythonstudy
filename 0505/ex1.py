#입력받는 값을 범위로 지정해 랜덤 정수를 배열에 저장 단, 중복된 값을 제외하고 저장
import random as r
num = int(input("정수 입력 : "))

array = []
for i in range(num):
    random_sum= r.randint(1,num)
    while random_sum in array:
        random_sum = r.randint(1,num)
    array.append(random_sum)

print(array)

