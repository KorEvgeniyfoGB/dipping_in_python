# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.
#
# def get_dict(str):
#     res = [int(i) for i in str.split("/")]
#     d = {}
#     d[res[1]], d[res[2]] = res[0], tuple(res[3:])
#     return d
#
#
# print(get_dict("1/2/3/4/5/5"))

# ✔Самостоятельно сохраните в переменной строку текста.
# ✔Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔Напишите преобразование в одну строку.
# d = {k: ord(k) for k in input()}
# iter1 = iter(d.items())
# for i in range(5):
#     print(next(iter1))

# ✔Создайте генератор чётных чисел от нуля до 100.
# ✔Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔Решение в одну строку.

# gen = (i for i in range(0, 101) if i % 2 == 0 and sum([int(j) for j in str(i)]) != 8)
# # for i in range(200):
# #     print(next(gen))

# ✔Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔Вместо чисел, кратных пяти — слово «Buzz». ✔Если число кратно и 3, и 5,
# то программа должна выводить слово «FizzBuzz».
# ✔*Превратите решение в генераторное выражение.
# gen = ("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in
#        range(1, 101))
#
# print(*gen, sep="\n")
#
# for i in range (2, 10):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")
#     print("")

# days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month, day = map(int, input().split())
# fday = day + 1
# fmonth = month
# pday = day - 1
# pmonth = month
# if day in days:
#     fmonth = month + 1
#     fday = 1
# elif day == 1:
#     pday = days[month - 1]
#     pmonth = month - 1
# print(f"{pmonth:02}.{pday:02} {fmonth:02}.{fday:02}")

# где N — количество строк в таблице, а M — количество столбцов в таблице.
# matrix = [[1, 0, 0, 0, 0, 0, 0, 0],
#           [0, 1, 0, 0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0],
#           [0, 0, 0, 1, 0, 0, 0, 0],
#           [0, 0, 0, 0, 1, 0, 0, 0],
#           [0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 0, 0, 0, 0, 0, 1, 0],
#           [0, 0, 0, 0, 0, 0, 0, 1]]
# N = 8
# M = 8
# diagonals0 = [[] for i in range(N + M - 1)]
# diagonals1 = [[] for i in range(N + M - 1)]
# for i in range(-(N - 1), M):
#     for j in range(N):
#         row, col = j, i + j
#         if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
#             diagonals0[i + len(matrix) - 1].append(matrix[row][col])
#             diagonals1[i + len(matrix) - 1].append(matrix[row][M - col - 1])
#
#             #print(matrix[row][col])
#             # if 1 in matrix[row][col] and matrix[row][col].count(1):
#             #     break
#             #matrix[row][M - col - 1]
# diagonals0
# diagonals1

# import csv
#
#
# # Создаем список словарей
# my_list = [{'name': 'John', 'age': 25, 'hobbies': ['reading', 'swimming', 'traveling']}, {'name': 'Alice', 'age': 30, 'hobbies': ['hiking', 'dancing', 'cooking']}]
# # Открываем файл для записи
# with open('my_file.csv', 'w', newline='') as file:
# # Создаем объект DictWriter
#     writer = csv.DictWriter(file, fieldnames=my_list[0].keys())
# # Записываем заголовок
#     writer.writeheader()
# # Записываем данные
#     for row in my_list:
#         writer.writerow(row)
# import os
#
#
# def dir_size(path_to_dir):
#     total_size = 0
#     with os.scandir(path_to_dir) as it:
#         for entry in it:
#             if entry.is_file():
#                 total_size += entry.stat().st_size
#             elif entry.is_dir():
#                 total_size += dir_size(entry.path)
#     return total_size
#
#
# def get_dict_directory(path_dir):
#     lst_dir = list(os.walk(path_dir))
#     data_list = []
#     for parent_directory, directory, files in lst_dir:
#         data_dict = {}
#         data_dict[parent_directory] =[]
#         for dir in directory:
#             dir_dict = {}
#             size_dir = dir_size(os.path.join(parent_directory, dir))
#             dir_dict["name"] = dir
#             dir_dict["what_is_it"] = "directory"
#             dir_dict["size"] = size_dir
#             data_dict[parent_directory].append(dir_dict)
#         for file in files:
#             file_dict = {}
#             size_fie = os.path.getsize(os.path.join(parent_directory, file))
#             file_dict["name"] = file
#             file_dict["what_is_it"] = "file"
#             file_dict["size"] = size_fie
#             data_dict[parent_directory].append(file_dict)
#         data_list.append(data_dict)
#     return data_list

# def get_dict_directory(path_dir):
#     lst_dir = list(os.walk(path_dir))
#     data_dict = {}
#     for parent_directory, directory, files in lst_dir:
#         data_dict[parent_directory] =[]
#         for dir in directory:
#             size_dir = dir_size(os.path.join(parent_directory, dir))
#             a = dir + ", this is directory " + ",size: " + str(size_dir)
#             data_dict[parent_directory].append(a)
#         for file in files:
#             size_fie = os.path.getsize(os.path.join(parent_directory, file))
#             b = file + ", this is file " + ",size: " + str(size_fie)
#             data_dict[parent_directory].append(b)
#     return data_dict

# class Factorial:
#     def __init__(self, limit: int):
#         self.limit = limit
#         self.storage = {}
#
#     def _fact(self, num: int):
#         factorial = []
#         number = 1
#         for i in range(1, num + 1):
#             number *= i
#             factorial.append(number)
#         return factorial
#
#     def __call__(self, number: int):
#         result = self._fact(number)[-self.limit:]
#         self.storage[number] = result
#         return result
#
# class Factorial:
#     def __init__(self, *args):
#         self.start, self.stop, self.step = 1, 1, 1
#         if args:
#             args = list(map(int, args))
#             match len(args):
#                 case 1:
#                     self.stop = args[0]
#                 case 2:
#                     self.start, self.stop = args
#                 case 3:
#                     self.start, self.stop, self.step = args
#         self._value = self._fact()
#
#     def _fact(self):
#         result = []
#         number = 1
#         for i in range(self.start, self.stop, self.step):
#             number *= i
#             result.append(number)
#         return result
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self._value:
#             return self._value.pop(0)
#         raise StopIteration
#
#
# a = Factorial(2,20,2)
#
# for i in a:
#     print(i)


#
# class Value:
#     def __init__(self, min_value: int, max_value: int):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return 'ЦЫФРА'
#
#     def __set__(self, instance, value):
#         setattr(instance, self.param_name, self._validate(value) + 10)
#
#     def _validate(self, value: int):
#         if not value % 2:
#             raise ValueError
#         return value
#
#
# class Rectangle:
#     width = Value(10, 100)
#     height = Value(10, 100)
#
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
#
# a = Rectangle(11, 13)
# print(a.__dict__)
# print(a.area)

