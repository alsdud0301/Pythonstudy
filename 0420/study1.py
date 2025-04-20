# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"*" ,j,"=",i*j, end="\t")
#     print()
#
# for i in range(2,10,2):
#     print(i)

# a = [int(input()) for _ in range(5)]
# b = 0
# for i in a:
#     b+= i
# print(b/5)

a = input()
for i in range(len(a)):
    print(a[len(a)-i-1], end='')