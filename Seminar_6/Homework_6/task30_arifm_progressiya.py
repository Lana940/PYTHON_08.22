# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an= a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1= int(input("Vvedite 1 chislo: "))
d = int(input("Vvedite raznicu: "))
n = int(input("vvedite kol-vo elementov: "))

my_list = []
for i in range(1, n+1):
    a_n = a1 + (i-1) * d
    my_list.append(a_n)
print(my_list)