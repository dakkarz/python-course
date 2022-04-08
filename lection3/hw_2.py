# Найдите сумму всех чисел меньше 1000, кратных 3 или 5 с помощью функции генератора


def gen_func():
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            yield i


if __name__ == '__main__':
    # call your generator func here
    print(sum(gen_func()))