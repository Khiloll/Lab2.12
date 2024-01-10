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

def morze_decorator(func):
    """
    Декоратор функции, возвращающий строку, преобразованную в азбуку морзе.
    """
    morze = {
        'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.',
        'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
        'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--',
        'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...',
        'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
        'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--',
        'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-···-'
    }

    def wrapper(arg):
        """
        Функция-обертка.
        """
        arg = func(arg)
        return ' '.join([morze[char] for char in arg if char in morze])
    return wrapper


@morze_decorator
def process_string(s):
    """
    Переводит строку в нижний регистр и удаляет из нее лишние пробелы.    
    """
    s = ' '.join(s.lower().split())
    return s


if __name__ == "__main__":
    input_string = "ПрИвЕт Я Хилол"
    output_string = process_string(input_string)
    print(f"{output_string = }")
