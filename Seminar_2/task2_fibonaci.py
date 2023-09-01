# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 ...

fib1, fib2 = 0, 1
number = int(input("put number >  1: "))

count = 2 
fib = 0
while number >= fib2:
    count+=1
    fib = fib2
    fib2 = fib2 + fib1
    fib1 = fib 
    if number == fib2:
        print("number of this element is:", count)
        break
else:
    print(-1)
