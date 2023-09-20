# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
def _is_leapyear(year):
    return bool(year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))



def is_true_date(isdate: str):
    isdate = list(map(int, isdate.split(".")))
    a, b, c = [1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]
    if all(map(lambda x: x > 0, isdate)):
        if isdate[-1] < 10000 and isdate[1] < 13:
            if isdate[1] in a and isdate[0] < 32 or isdate[1] in b and isdate[0] < 31 \
                    or _is_leapyear(isdate[-1]) and isdate[0] < 29 or not _is_leapyear(isdate[-1]) and isdate[0] < 30:
                return True
    return False


if __name__ == "__main__":
    print(is_true_date("32.03.2019"))

