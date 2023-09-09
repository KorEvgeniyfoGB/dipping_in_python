# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

try:
    with open("text.txt", encoding="UTF-8") as f:
        a = f.read()
        b = {}
        for i in set(a.lower().split()):
            if i not in "!\"#$%&\'()*+,-./:;<=>":
                b[i] = a.lower().split().count(i)
        res = sorted(b.items(), key=lambda x: x[1], reverse=True)[:10]
        print([i[0] for i in res])
except Exception as e:
    print(e)
finally:
    print("Вроде правильно")
