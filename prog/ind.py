#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Объявите функцию, которая принимает строку, удаляет из нее все
# подряд идущие пробелы и переводит ее в нижний регистр – малые буквы.
# Результат (строка) возвращается функцией. Определите декоратор,
# который строку, возвращенную функцией, переводит в азбуку Морзе,
# используя следующий словарь для замены русских букв и символа
# пробела на соответствующие последовательности из точек и тире.
# Преобразованная строка возвращается декоратором. Примените декоратор
# к функции и вызовите декорированную функцию.
# Результат работы отобразите на экране.

def sum_decorator(start):
    def decorator(func):
        def wrapper(numbers):
            nums = [int(num) for num in numbers.split()]
            total_sum = sum(nums) + start
            return total_sum

        return wrapper

    return decorator

@sum_decorator(start=5)
def sum_of_numbers(numbers):
    # Функция для подсчета суммы чисел
    nums = [int(num) for num in numbers.split()]
    total_sum = sum(nums)
    return total_sum

# Ввод строки целых чисел
numbers_string = input("Введите строку целых чисел через пробел: ")

# Получаем сумму чисел с учетом декоратора
result = sum_of_numbers(numbers_string)

print("Сумма чисел с учетом стартового значения 5:", result)
