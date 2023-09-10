import random 

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]

list_size = int(input("Vvedite razmer spiska : "))
list_1 = []
#list_ = [1, 1, 2, 0, -1, 3, 4, 4]

for _ in range(list_size):
    number = int(input("Vvedite chisla spiska: "))
    list_1.append(number)
print(list_1)


list_1 = set(list_1)
a = list_1
print(list_1)

print(len(set(list_1)))






# 2 cherez cycle reshenie:

size = random.randint(5,10)
list_2 = [random.randint(0,10) for _ in range(size)]
list_unique = [list_2[0]]
count = 1
print(list_2)


unique_2 = [num for num in list_2 if num in list_unique]
count2 = len(unique_2)

print(count2)



for num in list_2[1:]:
    if num in list_unique:
        list_unique.append(num)
        count += 1
      
print(count2)


unique = [num if num in unique else 0 for num in numbers]
