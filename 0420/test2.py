# 입력받은 문자열 뒤집기

a = input("문자열 입력 : ")
b = a.split()
for i in b:
    print(i[::-1],"" , end ="")

# print(" ".join(word[::-1] for word in input("문자열 입력 : ").split()))