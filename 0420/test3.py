# 정수를 입력받아 오름차순으로 정렬하기

a = [int(input("정수 입력 : ")) for _ in range(5)]

for i in range(len(a)-1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)