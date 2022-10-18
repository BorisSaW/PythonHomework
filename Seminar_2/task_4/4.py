"""
Задача 4
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random

number = int(input("Введите число: "))
result = list(range(-number, number + 1))
path = 'file.txt'
data = open(path, 'r')
multi = 1
for position in data:
    multi *= result[int(position)]
data.close()
print(result)
print(f'Произведение элементов = {multi}')
