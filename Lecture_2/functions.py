
# сохранение элемента в конец списка

list_1 = [1,5]
print(list_1)

list_1.append(8)
print(list_1)

list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)
# Удаление последнего элемента списка.

list_1 = [12, 7, -1, 21, 0]
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.pop())

list_1 = [12, 7, -1, 21, 0]
a = list_1.pop()
print(list_1)

#Удаление конкретного элемента из списка.
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(2)) # 12
print(list_1)

# 3. Добавление элемента на нужную позицию. inserrt

list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11)) # 1 cifra v skobkah pozocoya elementa, 2 ego znachenie
print(list_1) 

print(list_1.insert(4, -15))
print(list_1) 