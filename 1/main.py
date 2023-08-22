# Императивное
# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.

def sumOdd(N):
    sum = 0
    for number in range(N + 1):
        if number % 2 == 0:
            sum += number
    return sum

N = int(input())

print(sumOdd(N))

