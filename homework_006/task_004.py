# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки
from task_003 import *
import random


def get_rand_queens():
    return random.randint(0, 7), random.randint(0, 7)


res = []
while True:
    n = 8
    m = 8
    var = [get_rand_queens() for i in range(8)]
    a, b, c, d, e, f, g, h = var
    if is_it_solution(eight_queens_on_board(a, b, c, d, e, f, g, h, task_001.get_matrix(n, m, 0, 0))):
        res.append(var)
    if len(res) == 4:
        break
print(*res, sep="\n")
