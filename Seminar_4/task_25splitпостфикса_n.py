# ; #Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# ; уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# ; Input: a a a b c a a d c d d
# ; Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функци .split()

my_str = 'a a a b c a a d c d d'
my_str = my_str.split()
print(my_str)

my_dict = {}
for letter in my_str:
    if letter in my_dict:
        my_dict[letter] +=1
        print(letter+'_'+str(my_dict[letter]), end=' ')
    else:
        my_dict[letter] = 0
    print(letter, end=' ')
    

print(my_dict)
