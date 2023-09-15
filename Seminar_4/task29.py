# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”.

n = int(input("vvedite chislo: "))
max_number = -1
while n != 0:
  n = int(input("vvedite chislo: "))
  if max_number < n:
    max_number = n
print(max_number)

#petya

n = int(input("vvedite chislo: "))
max_number = -1
while n != 0:
   n = int(input("vvedite chislo: "))
   if max_number < n:
     max_number = n
print(max_number) 