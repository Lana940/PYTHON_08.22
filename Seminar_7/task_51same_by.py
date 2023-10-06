# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод:                           Вывод:
# values = [0, 2, 10, 6]                     same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects:list):
    char_0 = characteristic(objects[0])
    for num in objects[1:]:
        if char_0 != characteristic(num):
            return False
    return True


values = [0, 2, 10, 2]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

#reshenie s filter 

def same_by(characteristic, objects):
    chars = list(filter(characteristic, objects))

    if len(chars) == 0 or len(chars) == len(objects):
        return True
    return False

values = [0, 2, 13, 6]
if same_by(lambda x: x % 2, values): 
    print('same')
else:
    print('different')

#reshenie s map
#  
def same_by(characteristic, objects):
    chars = list(map(characteristic, objects))

    if len(chars) == 0 or len(chars) == len(objects):
        return True
    return False

values = [0, 2, 13, 6]
if same_by(lambda x: x % 2, values): 
    print('same')
else:
    print('different')