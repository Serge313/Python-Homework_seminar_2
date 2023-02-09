"""Задача 3: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P."""


import sys


try:
    x, y = map(int, input("Enter sum and product in format \"S P\": ").split())
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


z = 0
for i in range(x + y):
    if z:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            z = 1
            print(f"X, Y = {i, j}")
