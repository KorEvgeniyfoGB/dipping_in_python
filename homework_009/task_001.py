# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random


def import_quandratic_equation(func):
    def wrapper(file="a lot of num.csv"):
        with open(file, "r") as f:
            reader = csv.reader(f)
            res = []
            for row in reader:
                for i in row:
                    res.append([float(j) for j in i.split(";")])
            result = []
            for i in res:
                result.append([str(i), func(*i)])
        return result

    return wrapper


def get_json_with_solution(func):
    def wrapper(*args):
        result = {k: v for k, v in func(*args)}
        with open("data.json", "w") as f:
            json.dump(result, f, indent=4)

    return wrapper


@get_json_with_solution
@import_quandratic_equation
def solve_quadratic_equation(a, b, c):
    disk = b ** 2 - 4 * a * c
    if disk > 0:
        x1 = (-b + disk ** 0.5) / 2 * a
        x2 = (-b - disk ** 0.5) / 2 * a
        return x1, x2
    elif disk == 0:
        x = -b / (2 * a)
        return x
    return "no solutions"


def get_3_num_in_csv(min_lim, max_lim, number_of_digits):
    res = []
    for i in range(100):
        res.append([round(random.uniform(min_lim, max_lim), number_of_digits) for i in range(3)])
    with open("a lot of num.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(res)


get_3_num_in_csv(-100, 100, 3)
solve_quadratic_equation()
