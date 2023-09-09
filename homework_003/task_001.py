# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [True, 1, 1, 2, 2, 2, 3, 3, 4, "python", "python", 4, 1.5, 1.5, True, False, 0]
lst_1 = [i if not isinstance(i, bool) else "yes" if i == True else "no" for i in lst]
double_lst = []
for i in set(lst_1):
    if lst_1.count(i) == 2 and isinstance(i, int | float | str):
        if i == "yes":
            double_lst.append(True)
        elif i == "no":
            double_lst.append(False)
        else:
            double_lst.append(i)
print(double_lst)
