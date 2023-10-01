# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]


list_1 = [1,2,3,5,8,15,23,38]
list_2 = []
for i in range (len(list_1)):
    if list_1[i] % 2 == 0:
        list_2.append(list_1[i])
print(list_2)

data = [1,2,3,5,8,15,23,38]
res = list()

for i in data:
    if i %2 == 0:
        res.append((i, i**2))

print(res)



#2 lambda

def select(f, col):
    return[f(x) for x in col] #возвращает список в котором к каждому ел применили функцию ф(x)

def where(f,col):
    return[x for x in col if f(x)] # возвращает только те значения которые прошли проверку условия ф(x)

data = [1,2,3,5,8,15,23,38]
res = select(int, data)
print(res)
res = where(lambda x: x%2 == 0, res)
print(res)

res = list(select(lambda x: (x, x**2), res))
print(res)


data = [1,2,3,5,8,15,23,38]
res = map(int, data)
res = filter(lambda x: x%2 == 0, res)
res = list(map(lambda x:(x, x**2), res))
print(res)