# Отсортируйте список случайной длины в зависимости от мода (reverse) по возрастанию или по убыванию
import random

MAX_NUM = 10**5


def quicksort(lst: list, reverse: bool):
    if len(lst) > 1:
        pivot = lst[random.randint(0, len(lst)-1)]
        lo = [value for value in lst if value < pivot]
        eq = [value for value in lst if value == pivot]
        hi = [value for value in lst if value > pivot]
        if reverse is True:
            lst = quicksort(hi, reverse) + eq + quicksort(lo, reverse)
        else:
            lst = quicksort(lo, reverse) + eq + quicksort(hi, reverse)
    return lst


def sort(tpl: tuple, reverse: bool = False):
    lst = list(tpl)
    return quicksort(lst, reverse)


if __name__ == '__main__':
    numbers = tuple(random.randint(0, MAX_NUM) for _ in range(random.randint(0, MAX_NUM)))
    print(sort(
        numbers,
        reverse=False  # change mod here
    ))