import random as r
import statistics as st
# print(r.randint(1, 100))
# 가위바위보 만들기
input_num = int(input("1 : 가위 ,2 : 바위 , 3 : 보"))
random_num = r.randint(1, 3)
print(random_num)
if ((input_num==1 and random_num==2)
    or (input_num==3 and random_num==1)
    or (input_num==2 and random_num==3)):
    print("컴퓨터 승리")
elif input_num == random_num:
    print("무승부")
else :
    print("사용자 승리")

# -----------------------------------------------------
number_list = []
for _ in range(10000):
    number_list.append(r.randint(0,1))

print(st.mean(number_list))
