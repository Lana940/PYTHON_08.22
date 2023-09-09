# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).
dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

print(dictionary['left']) # ← типы ключей могут отличаться

print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента



d = {}
d = dict()
d['q'] = 'qweerrty'
print(d)
d['w'] = 'werty'
print(d['w'])

dictionary = {}
dictionary = { 'up': '↑', 'down' : '↓', 'left' : '←', 'right' : '→'}
print( dictionary)
print(dictionary['left'])

dictionary[895] = 865465
print(dictionary)

del dictionary['left']
print(dictionary)
for item in dictionary: 
    print(item)


print(dictionary)
for item in dictionary: 
    print('{} : {}'.format(item,dictionary[item]))

print(dictionary.items()) # dict_items([('up', '↑'), ('down', '↓'), ('right', '→'), (895, 865465)])  spisok iz kortezhey
for (k,v) in dictionary.items():   # k,v zdes key and value, kluch i znachenie
    print(k,v)