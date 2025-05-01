# 약수합 구하기
import math

while True:
    num = int(input("정수를 입력 : "))
    if num==-1:
        print(num)
        break
    else:
        numlist = [1]
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                numlist.append(i)
                if i != num // i:
                    numlist.append(num//i)
        print(sum(numlist))
        numlist.sort()
        print(numlist)
