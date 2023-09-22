# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: 6,13     [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random 

size1 = random.randint(1,15)
first_list = [random.randint(0,20) for _ in range (size1)]

print(first_list)

min_num = random.randint(1,6)
print(min_num)
max_num = random.randint(7,15)
print(max_num)
new_list = []

for i in range (size1):
    if min_num < first_list[i] < max_num:
        new_list.append(i)
print(new_list)

