#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import sys
from task_001 import _is_leapyear, is_true_date


if __name__ == "__main__":
    cons_date = str(sys.argv[1])
    print(is_true_date(cons_date))