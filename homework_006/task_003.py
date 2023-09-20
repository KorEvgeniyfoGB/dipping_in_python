# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from homework_004 import task_001


def eight_queens_on_board(queens1: tuple, queens2: tuple, queens3: tuple, queens4: tuple, queens5: tuple,
                          queens6: tuple, queens7: tuple, queens8: tuple, board):
    for i in [queens1, queens2, queens3, queens4, queens5, queens6, queens7, queens8]:
        a, b = i
        board[a][b] = 1
    return board


def is_it_solution(board):
    n, m = len(board), len(board[0])
    for i in board:
        if sum(i) > 1:
            return False
    for i in range(len(board)):
        lst_q_coll = []
        for j in range(len(board[i])):
            lst_q_coll.append(board[j][i])
        if sum(lst_q_coll) > 1:
            return False
    diagonals0 = [[] for i in range(n + m - 1)]
    diagonals1 = [[] for i in range(m + m - 1)]
    for i in range(-(n - 1), m):
        for j in range(n):
            row, col = j, i + j
            if 0 <= row < n and 0 <= col < m:
                diagonals0[i + n - 1].append(board[row][col])
                diagonals1[i + n - 1].append(board[row][m - col - 1])
    for i in diagonals0:
        if sum(i) > 1:
            return False
    for i in diagonals1:
        if sum(i) > 1:
            return False
    return True


if __name__ == "__main__":
    c = 8
    d = 8
    chess_board = task_001.get_matrix(c, d, 0, 0)
    r = eight_queens_on_board((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), chess_board)
    print(*r, sep="\n")
    print(is_it_solution(r))
