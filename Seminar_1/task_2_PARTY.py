# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# # Input: 20 21 22(ввод чисел НЕ в одну строку) output: 32

kids1grade = int(input("enter amount of pupils in 1st grade: "))
kids2grade = int(input("enter amount of pupils in 2st grade: "))
kids3grade = int(input("enter amount of pupils in 3st grade: "))

desks_1 = kids1grade//2 + bool(kids1grade%2)
desks_2 = (kids2grade + 1)//2
desks_3 =(kids3grade + 1)//2

sum_of_desks = desks_1 + desks_2 + desks_3

print(sum_of_desks)