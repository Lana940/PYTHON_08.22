# ; Пользователь вводит число N (1 ≤ N ≤ 10). В следующих строках  располагается N целых чисел от -50 д0 50..
#  нужно вывести наибольшее кол-во идущих подряд положительн0251х чисел.
# ; Input: 6 -> > -20 30 -40 50 10 -10
# ; Output: 2

N = int(input("Vvedite chislo > 1 и < 10: "))
k = 0
max_k = 0

for _ in range(N):     # _ peremennaya kotoraya ne ispol-sya vnutri cikla 
        n2 = int(input("vvedite cislo:  "))
        if n2 > 0:              
              k+=1
              if k > max_k:
                     max_k = k
        else:
              k = 0
print(max_k)