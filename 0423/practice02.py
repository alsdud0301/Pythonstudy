def test():
    return 10,20
a,b = test()

print(a,b)


for i,value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다.".format(i,value))

