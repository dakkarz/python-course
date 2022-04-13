# Запишите в словарь по ключам от 1 до 10, список чисел от 0 до 1000, которые делятся на соответствующие ключи
# Пример числа от 1 до 6:
# {
#     1: [1, 2, 3, 4, 5, 6],
#     2: [2, 4, 6],
#     3: [3, 6],
#     ...
# }


def get_dividers_dict():
    result = {}

    for k in range(1, 11):
        result[k] = [v for v in range(k, 1001, k)]

    return result


if __name__ == '__main__':
    print(get_dividers_dict())
