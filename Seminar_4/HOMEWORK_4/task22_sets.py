import random
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n_size = int(input("Vvedite kol-vo elem 1-go mnozhestva: "))
list_1 = [random.randrange(1,20) for i in range(n_size)]

print(set(list_1))

m_size = int(input("Vvedite kol-vo elem 1-go mnozhestva: "))
list_2 = [random.randrange(1,15) for i in range(m_size)]

print(set(list_2))

same_elemets = set(list_1).intersection(set(list_2))
res = list(same_elemets)
print(res)
print(sorted(res))






