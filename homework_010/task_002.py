# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
class Triangle:

    @staticmethod
    def verification(a, b, c):
        if a < b + c or b < a + c or c < a + b:
            return True
        return False

    def __init__(self, a, b, c):
        if self.verification(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise Exception("Такого треугольника не существует")

    def what_is_triangle(self):
        if self.a == (self.b + self.c) / 2 or self.b == (self.a + self.b) / 2 or self.c == (self.a + self.b) / 2:
            print("Треугольник равносторонний")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")


#Напишите функцию для транспонирования матрицы
import random


class Matrix:
    def __init__(self, m, n, a, b):
        self.writing_in_matrix = [[random.randint(a, b) for j in range(n)] for i in range(m)]

    def get_transportes_matrix(self) -> list:
        self.writing_in_matrix = [[row[i] for row in self.writing_in_matrix] for i in
                                  range(len(self.writing_in_matrix[0]))]
        return self.writing_in_matrix

    def print_matrix(self):
        for i in range(len(self.writing_in_matrix)):
            for j in range(len(self.writing_in_matrix)):
                print(self.writing_in_matrix[i][j], end=" ")
            print()
