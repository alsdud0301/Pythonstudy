import random

def random_num(num):
    array=[]
    for i in range(num):
        while True:
            random_sum = random.randint(1,num)
            if random_sum not in array:
                array.append(random_sum)
                break
    return array

def insert_sort(array):
    for i in range(1,len(array)):
        tmp = array[i]
        for j in range(i-1,-1,-1):
            if tmp < array[j]:
                index = j
                array[j+1]=array[j]
                array[index] = tmp
        print(array)

insert_sort(random_num(10))

