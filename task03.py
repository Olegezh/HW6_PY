# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные
# варианты и выведите 4 успешных расстановки.

from random import randint
from HW06.task02.chess import validate_queens


def generate_positions():
    count = 0
    while count < 4:
        positions = list((j+1,  randint(1, 8)) for j in range(8))  # создаём список с числами от 1 до 8
        if validate_queens(positions):
            print(positions)
            count += 1


generate_positions()
