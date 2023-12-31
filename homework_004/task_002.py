# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def get_dict(**kwargs):
    return {v if isinstance(v, (str, tuple, int, float)) else str(v): k for k, v in kwargs.items()}


print(get_dict(key=1, key2="2", key3=[1, 2], key4={1,2}))
