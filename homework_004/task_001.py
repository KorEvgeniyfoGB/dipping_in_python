# Напишите функцию для транспонирования матрицы
import random


def get_matrix(m: int, n: int) -> list:
    return [[random.randint(0, 11) for j in range(n)] for i in range(m)]


def get_transportes_matrix(lst: list) -> list:
    return [[row[i] for row in lst] for i in range(len(lst[0]))]


m, n = int(input()), int(input())
a = get_matrix(m, n)
print(*a, sep="\n", end="\n\n")
print(*get_transportes_matrix(a), sep="\n")
