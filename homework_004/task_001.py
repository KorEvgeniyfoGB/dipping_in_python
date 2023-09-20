# Напишите функцию для транспонирования матрицы
import random


def get_matrix(m: int, n: int, a, b) -> list:
    return [[random.randint(a, b) for j in range(n)] for i in range(m)]


def get_transportes_matrix(lst: list) -> list:
    return [[row[i] for row in lst] for i in range(len(lst[0]))]

if __name__ == "__main__":
    m, n = int(input()), int(input())
    a = get_matrix(m, n)
    print(*a, sep="\n", end="\n\n")
    print(*get_transportes_matrix(a), sep="\n")
