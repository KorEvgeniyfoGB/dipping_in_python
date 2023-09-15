# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def get_n_prime_num(n):
    def prime():
        num = 2
        while True:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num
            num += 1
    gen = iter(prime())
    return [next(gen) for i in range(n)]


get_n_prime_num(6)

