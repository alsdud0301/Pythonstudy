


def isanagram(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    isana = True
    if n1 != n2 :
        print("어구전철x")
        isana = False
    list1 = []
    list2 = []
    for i in range(n1):
        list1.append(str1[i])
        list2.append(str2[i])

    for i in range(n1):
        if i < n1 :
            for j in range(n1):
                if list1[i] != list2[i] :
                    isana = False
                elif i == n1:
                    isana = True
    if isana:
        print("어구전철입니다")
    else :
        print("어구전철x")
    
str1 = input("문자열1 입력 : ")
str2 = input("문자열2 입력 : ")
isanagram(str1,str2)



    
    