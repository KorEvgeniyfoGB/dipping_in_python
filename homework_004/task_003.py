# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


def up_bank_acc(bank_acc, cash):
    if windrawal_cash(cash):
        print(f'Счёт пополнена на {cash}, счёт составляет {bank_acc + cash}')
        return wealth_check(bank_acc + cash)
    print(f'Сумма пополнения должна быть кратной 50 у.е., счёт остался {bank_acc}')
    return wealth_check(bank_acc)


def get_cash(bank_acc, cash):
    if get_cash_withdrawal_request(bank_acc, cash):
        print(f'Вы сняли {cash} у.е., сумма счёта составляет {bank_acc - cash - get_piercent(cash)}')
        return wealth_check(bank_acc - cash - get_piercent(cash))
    print(f'Недостаточно средств на счёте')
    return wealth_check(bank_acc)


def get_piercent(cash):
    if 30 < cash * 0.015 < 600:
        return cash * 0.015
    elif cash * 0.015 < 30:
        return 30
    elif cash * 0.015 > 600:
        return 600


def get_cash_withdrawal_request(bank_acc, cash):
    if bank_acc >= cash + get_piercent(cash):
        return True
    else:
        return False


def windrawal_cash(cash):
    if cash % 50 == 0:
        return True
    else:
        return False


def wealth_check(bank_acc):
    if bank_acc >= 5000000:
        print(f'Налог на богатство 10 %. Сумма на счетё {bank_acc - bank_acc * 0.1}')
        return bank_acc - bank_acc * 0.1
    return bank_acc


def get_bonus(banc_acc, counter):
    if counter == 3:
        banc_acc *= 1.03
        print(f'Бонус тебе. Твой счёт теперь такой {banc_acc}')
        return banc_acc
    return banc_acc


def atm(bank_acc=0, tranzaction=0):
    while True:
        zapr = int(input("1 - накинуть бабла, 2 - снять бабла, 3 - закончить сессию: "))

        if zapr == 1:
            cash = int(input("Введите сумма что накинуть: "))
            bank_acc = up_bank_acc(bank_acc, cash)
            tranzaction += 1
            bank_acc = get_bonus(bank_acc, tranzaction)

        elif zapr == 2:
            cash = int(input("Введите сумма что хотите снять: "))
            bank_acc = get_cash(bank_acc, cash)
            tranzaction += 1
            bank_acc = get_bonus(bank_acc, tranzaction)

        elif zapr == 3:
            print(f'На твоём счету {bank_acc}, покеда')
            break
    return bank_acc


your_acc = atm()
print(your_acc)
