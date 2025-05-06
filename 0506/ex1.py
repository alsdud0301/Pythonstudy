import random_func

array = random_func.random_num(20)
print(array)
for i in range(len(array)-1):
     for j in range(len(array)-1-i):
        if array[j]> array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]

print(array)
