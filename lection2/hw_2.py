# Выведите все простые числа для заданного интервала
# Гарантируется, что start и end типа int. Вводятся в одну строку через пробел


def get_prime_nums(start: int, end: int):
    seq = set(range(2, end+1))
    sieve = []
    while seq:
        prime = min(seq)
        sieve.append(prime)
        seq -= set(range(prime, end+1, prime))  

    index = 0
    while start > sieve[index]:
        sieve.pop(index)
    print(*sieve)


if __name__ == '__main__':
    start, end = map(int, input().split())
    get_prime_nums(
        start=start,
        end=end,
    )