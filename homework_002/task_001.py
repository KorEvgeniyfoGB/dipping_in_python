# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
number = int(input())
print(hex(number))
hex_number = ""
while number > 0:
    hex_number = hex_list[number % 16] + hex_number
    number //= 16
print(hex_number)
print(hex(number))