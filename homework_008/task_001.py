# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def dir_size(path_to_dir):
    total_size = 0
    with os.scandir(path_to_dir) as it:
        for entry in it:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += dir_size(entry.path)
    return total_size


def get_dict_directory(path_dir):
    lst_dir = list(os.walk(path_dir))
    data_list = []
    for parent_directory, directory, files in lst_dir:
        data_dict_lst = []
        for dir in directory:
            dir_dict = {}
            size_dir = dir_size(os.path.join(parent_directory, dir))
            dir_dict["root_directory"] = parent_directory
            dir_dict["name"], dir_dict["what_is_it"], dir_dict["size"] = dir, "directory", size_dir
            data_dict_lst.append(dir_dict)
        for file in files:
            file_dict = {}
            size_fie = os.path.getsize(os.path.join(parent_directory, file))
            file_dict["root_directory"] = parent_directory
            file_dict["name"], file_dict["what_is_it"], file_dict["size"] = file, "file", size_fie
            data_dict_lst.append(file_dict)
        data_list.append(data_dict_lst)
    return data_list


def get_json(data):
    with open("data.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_csv(data):
    with open("data.csv", "w", encoding="UTF-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0][0].keys(), extrasaction="ignore", delimiter=";")
        writer.writeheader()
        for i in data:
            for row in i:
                writer.writerow(row)


def get_picle(data):
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)


my_path = os.getcwd()
data = get_dict_directory(my_path)
get_json(data)
get_csv(data)
get_picle(data)
