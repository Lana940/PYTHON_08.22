import math
#Сколькодней нужно, чтобы проехать маршрут длиной m километров? 
# n = 700 km/d  c = 750 km   output:2


# speed = int(input("put speed: "))
# distance = int(input("put distance: "))
# days = math.ceil(distance/speed)  # okruglenie vverh ceil
# print(days)

speed = int(input("put speed: "))
distance = int(input("put distance: "))
days = math.ceil(distance/speed)  # 1 reshenie
days2 = (distance + speed -1)//speed  # 2 reshenie
day2boolresolv = (distance//speed) + bool(distance%speed) # bool v znachenii TRUE vsegda daet 1, v FALSE 0
print(day2boolresolv)