# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Дан список размеров(длина, ширина)
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# напишите функцию find_farthest_orbit(orbits) которая найдет площадь самого большого елипся и возвратит кортеж с его размерами. 
# площадь елипса формула : S = pi*a*b, a, b - длина и ширина осей елипса 
# площась кругов не учитивать, т.е если а ==б то ето круг
# при решении использовать генератори списков
# елипс с самой больпой орбитой только один. 
# print(*find_farthest_orbit(orbits))

# output: 2.5 10


#2
def find_farthest_orbit(list_of_orbits):
 
    max_area = 0
    list_of_orbits = list(filter(lambda pair: pair[0] != pair[1], list_of_orbits)) # filter ne propustit krugi
    list_of_areas = list(map(lambda pair: pair[0] * pair[1] * 3.14, list_of_orbits)) #ploshad vychislili
    max_area = max(list_of_areas)
    i_max_area = list_of_areas.index(max_area)
    return list_of_orbits[i_max_area]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))







#1
def  find_farthest_orbit(list_orbits):
    max_area = 0 
    max_index = 0
    for i, pair in enumerate(list_orbits):
        # print(pair)
        area = pair[0] * pair[1]
        if pair[0] != pair[1]:
            if area > max_area:
                max_area = area
                max_index = i
    return list_orbits[max_index]
   
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
