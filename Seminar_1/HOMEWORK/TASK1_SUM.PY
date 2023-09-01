# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Enter your number: "))

num3 = num % 10
num2 = num // 10 % 10
num1 = num // 100
sum = num3 + num2 + num1
print(sum)