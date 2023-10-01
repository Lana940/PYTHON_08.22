# def where(f,col):
#     return[x for x in col if f(x)] # возвращает только те значения которые прошли проверку условия ф(x) = filter

data = [1,2,3,5,8,15,23,38]
res = map(int, data)

res = filter(lambda x: x%2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)