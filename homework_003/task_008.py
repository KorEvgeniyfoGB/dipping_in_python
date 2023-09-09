# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends = {
    'Иван': ('палатка', 'нож', 'книга', 'спички'),
    'Кирилл': ('шутки', 'прибаутки', 'палатка'),
    'Главный': ('палатка', 'спальный мешок', 'голубь'),
}

# находим вещи, которые взяли все три друга
common_items = set(list(friends.values())[0])
for friend, items in friends.items():
    common_items &= set(items)
if common_items:
    print('Вещи, которые взяли все друзья:', common_items)
else:
    print('Вещей, которые взяли все друзья - нет.')

# Находим вещи, которые есть только у одного друга
all_items = set()
for friend, items in friends.items():
    all_items |= set(items)
print(f'вещи, которые есть только у одного друга: {all_items - common_items}')

# Находим вещи, которые есть у всех, кроме одного
items_without_one_friend = {}
for friend, items in friends.items():
    items_without_other_friends = set(items) - common_items
    items_without_one_friend[friend] = items_without_other_friends

print('Вещи, которые есть у всех, кроме одного:')
for friend, items in items_without_one_friend.items():
    print(f'{friend}: {items}')
