# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def input_Numbers(size):
    if size == 0:
        return ""
    
    n = (input("vvedite chislo: "))
    size -= 1
    return input_Numbers(size) +" "+ n 

size = int(input("vvedite razmer: "))
print(input_Numbers(size).strip())

