import random
import json
import os
from faker import Faker


def create_employee(company, count):
    employees = {}
    list_id = []
    for _ in range(count):
        name = Faker("ru_RU").name()
        while True:
            employee_id = str(random.randint(1, 999999)).zfill(6)
            if employee_id not in list_id:
                list_id.append(employee_id)
                break
        lvl_access = int(employee_id) % 7 + 1
        if lvl_access in employees:
            employees[lvl_access][employee_id] = name
        else:
            employees[lvl_access] = {employee_id: name}
    with open(f'{company}.json', 'w', encoding='UTF-8') as f:
        json.dump(employees, f, indent=4, ensure_ascii=False)
    return employees


class EmployeeName:
    def __set_name__(self, owner, name):
        self.parameter_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f"Имя должно состоять только из букв: {value}")
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f"Имена должны быть с большой буквы: {value}")
        setattr(instance, self.parameter_name, value)


class EmpoloyeeID:
    def __set_name__(self, owner, name):
        self.parameter_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not len(value) == 6:
            raise ValueError(f"ID должен быбыть шестизначным: {value}")
        if not value.isdigit():
            raise ValueError(f'ID должен содержать только цифры: {value}')


class Employee:
    name = EmployeeName
    employee_id = EmpoloyeeID

    def __init__(self, name, lvl_access, employee_id):
        self.name = name
        self.employee_id = employee_id
        if 0 < int(lvl_access) < 8:
            self.lvl_access = lvl_access
        else:
            raise ValueError

    def __str__(self):
        return f'{self.name} ({self.employee_id}) | Доступ: {self.lvl_access}'

    def __eq__(self, other):
        return self.name == other.name and self.employee_id == other.employee_id


class OwnBasicException(Exception):
    def __init__(self, message: str):
        self.massage = message

    def __str__(self):
        return f'{self.massage}'


class LevelError(OwnBasicException):
    def __init__(self, me, new):
        super(LevelError, self).__init__(f'Ошибка доступа! Служащий ({me.name}, доступ: {me.lvl_access})'
                                         f'не имеет права создать служащего ({new.name}, доступ: {new.lvl_access})'
                                         f'выше собственного уровня доступа')

    def __str__(self):
        return f'{self.massage}'


class AccessError(OwnBasicException):
    def __init__(self, me: Employee):
        super(AccessError, self).__init__(f'Ошибка доступаЖ Служащий {me.name} ({me.employee_id}) не найден в базе')

class UniqueID(OwnBasicException):
    def __init__(self, new_id: str):
        super(UniqueID, self).__init__(f'Ошибка доступа: Служащий с таким ID {new_id} уже существует')

class Company:
    def __init__(self, name):
        self.name = name
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as f:
                employees_list = json.load(f)
        else:
            employees_list = create_employee(self.name, 20)
        self.employees = [Employee(e_name, e_lvl, e_id)
                          for e_lvl, person in employees_list.items()
                          for e_id, e_name in person.items()]

    def login(self, name: str, e_id: str):
        for employee in self.employees:
            if employee.name == name and employee == employee.employee_id == e_id:
                return employee
        return False

    def hiring(self, me: Employee, new_name: str, new_id: str, new_lvl: int):
        if me:
            if me.lvl_access > new_lvl:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, int(new_lvl), new_id))
                    self.__save()
                else:
                    raise UniqueID(new_id)
            else:
                raise LevelError(me, Employee(new_name, new_lvl, new_id))
        else:
            raise AccessError(me)

    def __save(self):
        employees_list = {}
        for employee in self.employees:
            if employee.lvl_access in employees_list:
                employees_list[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_list[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as f:
            json.dump(employees_list, f, indent=4, ensure_ascii=False)

