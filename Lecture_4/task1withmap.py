# def select(f, col):
#     return[f(x) for x in col] #возвращает список в котором к каждому ел применили функцию ф(x)
# вместо селект сразу встроенн0251й модуль map
def where(f,col):
    return[x for x in col if f(x)] # возвращает только те значения которые прошли проверку условия ф(x)

data = [1,2,3,5,8,15,23,38]
res = map(int, data)
print(res)
res = where(lambda x: x%2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)