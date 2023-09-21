# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def is_prime(a):
    if a % a == 0 and a != 0:
        return True
    else:
        return False

a = int(input("Enter a number: "))
print(is_prime(a))


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True
print(is_prime(int(input())))