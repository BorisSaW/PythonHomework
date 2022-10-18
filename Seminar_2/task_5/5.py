"""
Задача 5
Реализуйте алгоритм перемешивания списка.
"""

import random


def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_random = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_random]
        list[index_random] = temp
    return list


list = [1, 4, 81, 34, 7, 150, 5, 4, 12, 6]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
