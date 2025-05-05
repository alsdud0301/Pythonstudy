# 배열 정렬
import ex3
array = ex3.random_num(20)

for i in range(len(array)-1):
    min_num = i
    for j in range(i+1, len(array)):
        if array[min_num] > array[j]:
            min_num = j
    array[i], array[min_num] = array[min_num], array[i]

print(array)
