
# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
from random import randint 

# size = int(input("vvedite razmer massiva: "))
# list_1 = [randint(0,10) for _ in range(size)]
# print(list_1)

# k = randint(0,20)
# print(k)   

list_1 = [1, 12, 6, 7, 8, 15]
k = 11        

min = (k - list_1[0])
index = 0

for i in range(1, len(list_1)):
    count = (k - list_1[i])
    if count <0:
        count *=-1
    if count < min:
        min = count
        index = i

print(list_1[index])











