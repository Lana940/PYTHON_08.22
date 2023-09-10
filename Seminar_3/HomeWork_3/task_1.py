# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

from random import randint 

# list_1 = [1, 2, 3, 3, 3, 4, 5]
size = randint(5,10)
list_1 = [randint(0,10) for _ in range(size)]
print(list_1)

k = randint(1,10)
print(k)

count = 0
for i in range(len(list_1)):
               if list_1[i] == k:
                       count+=1
print(count)



                
       



