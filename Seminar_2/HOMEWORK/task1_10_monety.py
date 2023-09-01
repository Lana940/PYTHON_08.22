#Пользователь вводит число N. На следующих строках нужно вводить 1 или 0, в ответе вывести кол-во наименее встречающихся из них(т.е кол-во 0 либо 1, в зависимости от того, кого меньше)
# Input 5 -> 1 0 1 1 0
# output: 2

N = int(input("Vvedite chislo: "))

max_num = 0
min_num = 0 
for _ in range(N):
    num = int(input("Vvedite chisla ot 0 do 1: "))
    if num > 0:
        max_num +=1
    elif num <= 0:
        min_num +=1
if min_num < max_num:
    print(f" 0 vsego {min_num} ")
else:
    print(f" 1 vsego {max_num} ")