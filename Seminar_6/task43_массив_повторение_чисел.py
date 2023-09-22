# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:                  Вывод:
# 1 2 3 2 3                 4

from random import randint 

size1 = randint(5, 10)
first_list = [randint(0, 10) for _ in range(size1)]
print(first_list)

count = 0

for i in range(size1 - 1):
    for j in range(i+1, size1):
        if first_list[i] == first_list[j]:
            count+=1
print(count)