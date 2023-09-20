# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def get_dct_stavka(a: list, b: list, c: list):
    return {i: k * (1 + int(j[:-1]) / 100) for i, k, j in list(zip(a, b, c))}
