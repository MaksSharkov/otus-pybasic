"""
Домашнее задание №1
Функции и структуры данных
"""
import math


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result_array = []
    for num in nums:
        result_array.append(math.pow(num, 2)) if isinstance(num, int) else None
    return result_array


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if not isinstance(num, int):
        return False

    if num % 2 == 0 and num != 2:
        return False

    i = 3
    while i <= num and num % i != 0:
        i += 2

    if i < num or num == 1:
        return False
    else:
        return True


def is_odd(num):
    return True if isinstance(num, int) and num % 2 != 0 else False


def is_even(num):
    return True if isinstance(num, int) and num % 2 == 0 else False


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return list(filter(is_odd, nums))
    elif filter_type == EVEN:
        return list(filter(is_even, nums))
    else:
        return list(filter(is_prime, nums))
