# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    _profit = None

    def __init__(self, name, old):
        self.name = name
        self.old = old

    @classmethod
    def get_profit(cls):
        return cls._profit


class Cow(Animal):
    _profit = "milk"

    def __init__(self, name, old):
        super().__init__(name, old)


class Chicken(Animal):
    _profit = "egg"

    def __init__(self, name, old):
        super().__init__(name, old)


class Sheep(Animal):
    _profit = "wool"

    def __init__(self, name, old):
        super().__init__(name, old)


class Factory:
    _farm_animals = {"cow": Cow, "сhicken": Chicken, "sheep": Sheep}

    def create(self, *args):
        if args[0] in self._farm_animals:
            return self._farm_animals[args[0]](*args[1:])
    raise Exception("Такого класса нет")


factory = Factory()
d = factory.create("sheep", "F", 5)
print(d)
print(d.name)
print(d.old)
с = factory.create("fsfs0", "dfsf", 6)
