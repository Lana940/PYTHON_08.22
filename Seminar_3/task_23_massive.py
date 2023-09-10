# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

list_1 = [randint(1,10) for _ in range(4, 15)]
print(list_1)

result = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i -1]]
print(result)

print(len(result))


#reshenie 2 cherez cycle for 

list_2 =[randint(1,10) for _ in range(4, 15)]
print(list_2)

res_count = 0

for i in range(1, len(list_2)):
    if list_2[i]>list_2[i-1]:
        res_count+=1
print(res_count)