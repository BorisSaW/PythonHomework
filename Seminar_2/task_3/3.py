"""
Задача 3
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }
"""

def is_int(number):
    return number.isdigit()

number=None

while not is_int(str(number)):
    number = input("Input number: ")

number = int(number)


result = dict()
for i in range(1, number+1):
    result[i] = round((1+1/i)**i)

print(result)