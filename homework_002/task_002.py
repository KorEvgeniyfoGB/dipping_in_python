from fractions import Fraction

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

a = input()
b = input()
fract_a, fract_b = [int(i) for i in a.split("/")], [int(i) for i in b.split("/")]
if fract_a[-1] == fract_b[-1]:
    fract_sum = [fract_a[0] + fract_b[0], fract_a[-1]]
else:
    fract_a1 = fract_a[-1]
    fract_b1 = fract_b[-1]
    m = fract_a1 * fract_b1
    while fract_a1 != 0 and fract_b1 != 0:
        if fract_a1 >= fract_b1:
            fract_a1 = fract_a1 % fract_b1
        else:
            fract_b1 = fract_b1 % fract_a1
    nok = m // (fract_a1 + fract_b1)
    fract_sum = [(fract_a[0] * int((nok / fract_a[-1])) + fract_b[0] * int((nok / fract_b[-1]))), nok]
fract_prod = [fract_a[0] * fract_b[0], fract_a[-1] * fract_b[-1]]


def nod(lst):
    a = lst[0]
    b = lst[-1]
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b


nod_prod = nod(fract_prod)
nod_sum = nod(fract_sum)
fract_sum = [str(i // nod_sum) for i in fract_sum]
fract_prod = [str(i // nod_prod) for i in fract_prod]
print("/".join(fract_sum), "/".join(fract_prod))
print(Fraction(a) + Fraction(b), Fraction(a) * Fraction(b))
