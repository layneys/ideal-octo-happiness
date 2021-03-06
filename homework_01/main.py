"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [n**2 for n in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    i = 1
    k = 0
    while i <= number:
        if number % i == 0:
            k += 1
        i += 1
    if k == 2:
        return True
    else:
        return False


def filter_numbers(numbers_list, number_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if number_type == ODD:
        return list(filter(lambda n: n % 2 != 0, numbers_list))
    elif number_type == EVEN:
        return list(filter(lambda n: n % 2 == 0, numbers_list))
    elif number_type == PRIME:
        return list(filter(is_prime, numbers_list))
