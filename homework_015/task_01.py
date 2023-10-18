# Напишите код, который запускается из командной строки и получает на вход путь до директории
# на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='log.txt', level=logging.INFO)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def collect_directory_info(directory_path: str):
    if os.path.exists(directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                name, extension = os.path.splitext(file)
                file_info = FileInfo(name, extension, False, os.path.basename(root))
                logging.info(file_info)
            for dir in dirs:
                dir_info = FileInfo(dir, None, True, os.path.basename(root))
                logging.info(dir_info)
    else:
        raise ValueError("Проверьте правильность введенного пути")


if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    collect_directory_info(dir_path)
