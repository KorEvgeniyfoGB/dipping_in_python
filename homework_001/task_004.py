# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint
num = randint(0, 1000)
a = int(input())
p = 0
while a != num:
    if a > num:
        print("Дофига")
        a = int(input())

    elif a < num:
        print("Маловато будет")
        a = int(input())
    p += 1
    if p == 9:
        print("Конец")
        break

else:
    print("Угадал")
