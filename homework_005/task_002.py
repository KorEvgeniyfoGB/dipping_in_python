# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os.path


def get_path(a :str):
    res = os.path.split(a)
    return res[0], *res[-1].split(".")


print(get_path('C:/home/User/Desktop/file.txt'))