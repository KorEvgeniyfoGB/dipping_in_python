# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# ОБЯЗАТЕЛЬНО! Используйте фикстуры

from task_from_sem13 import *
import pytest

@pytest.fixture
def data():
    return Company('nike')


def test_employee_name_validation():
    employee = Employee("Игорь Выдрович Шубин", 5, "123456")
    assert employee.name == "Игорь Выдрович Шубин"

    with pytest.raises(ValueError):
        employee.name = "игорь Выдрович Шубин"

    with pytest.raises(ValueError):
        employee.name = "И1горь Выдрович Шубин"


def test_employee_id_validation():
    employee = Employee("Игорь Выдрович Шубин", 5, "123456")
    assert employee.employee_id == "123456"

    with pytest.raises(ValueError):
        employee.employee_id = "12345"

    with pytest.raises(ValueError):
        employee.employee_id = "abcdef"


def test_hiring_process(data):
    employee_count = len(data.employees)

    me = Employee("Вышеслав Евстигнеевич Стрелков", 5, "352342")
    data.hiring(me, "Игорь Выдрович Шубин", "654221", 6)

    assert len(data.employees) == employee_count + 1
    assert any(employee.name == "Игорь Выдрович Шубин" for employee in data.employees)
