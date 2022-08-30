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
        try:
            int(num)
            result_array.append(math.pow(num, 2))
        except Exception as e:
            pass
    return result_array


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    i = 3
    while i <= num and num % i != 0:
        i += 2
    if i < num or num == 1:
        return False
    else:
        return True


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
    result_array = []
    for num in nums:
        try:
            int(num)
            if filter_type == ODD:
                result_array.append(num) if num % 2 != 0 else None
            elif filter_type == EVEN:
                result_array.append(num) if num % 2 == 0 else None
            else:
                result_array.append(num) if is_prime(num) else None
        except Exception as e:
            pass
    return result_array
