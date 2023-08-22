# Императивное
# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.

import sys

def smallestNumber(numbers):
    min = sys.maxsize
    for number in numbers:
        if min > number:
            min = number
    return min

numbers = [40, 20, 90, 11, 5]

print(smallestNumber(numbers))
