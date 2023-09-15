# ✔ Создайте функцию генератор чисел Фибоначчи

def get_fib_num():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = iter(get_fib_num())
a = [next(gen) for i in range(int(input()))]
print(a)