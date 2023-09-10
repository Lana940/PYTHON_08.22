# # # Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# # # (сдвиг - циклический) на K элементов вправо, K – положительное число.
# # # Input: [1, 2, 3, 4, 5] k = 3
# # # # Output: [4, 5, 1, 2, 3]
from random import randint 

# # Srezami
list_size = randint(5,10)
list_1 = [randint(0,30) for _ in range(list_size)] # sozdali spisok cherez list_comprehensions
k = randint(1,20) % list_size

print(list_1)
print(k)

# list = [1, 2, 3, 4, 5]
# k = 3

list_new = []
for num in list_1[-k:]:
    list_new.append(num)
for num in list_1[: -k]:
    list_new.append(num)
print(list_new)

# #list comprehension reshenie

list_size = randint(5,10)
print(list_size)
list_1 = [randint(0,30) for _ in range(list_size)] # sozdali spisok cherez list_comprehensions
k = randint(1,20) % list_size

print(list_1)
print(k)

list_new = list_1[-k:] + list_1[:-k]
print(list_new)


# indexami

list_1 = [1,2,3,4,5]
k = 8
k = k%len(list_1)
list_result = list()

for i in range(k, len(list_1)):
    list_result.append(list_1[i])

for i in range(k):
    list_result.append(list_1[i])
print(list_result)

# pop i insert

lst = [1,2,3,4,5]
k = 8
k = k%len(lst)
print(k)

for i in range(k):
    num = lst.pop(-1)
    lst.insert(0,num)
print(lst)