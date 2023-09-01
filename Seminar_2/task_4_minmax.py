# # Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке каждое. 
# Вывести максимальное и минимальное(циклы):  Вторая строка содержит N чисел,
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

N = int(input("Vvedite chislo:  "))
num = int(input("Vvedite chisla: "))
max_num = num
min_num = num

for _ in range(N-1):
    num = int(input("Vvedite chisla: "))
    if num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
print(max_num)
print(min_num)
