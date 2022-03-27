def reverse_for(interval):
    print("Вывод интервала циклом for:")
    reverse_seq = [i for i in range(interval[0], interval[1]-1, -1)]
    return reverse_seq


def reverse_while(interval):
    print("Вывод интервала циклом while:")
    reverse_seq = []
    while interval[0] >= interval[1]:
        reverse_seq.append(interval[0])
        interval[0] -= 1
    return reverse_seq


def main():
    print("Здесь не будет проверки на корректность ввода чисел, подразумевается что пользователь введёт целые числа.")
    print("Вывод интервала по убыванию, где [a,b] замкнутый конечный промежуток.")
    interval = []
    interval.append(int(input("Input num1: ")))
    interval.append(int(input("Input num2: ")))

    if interval[0] == interval[1]:
        print(interval[0])
    else:
        interval.sort(reverse=True)
        print(*reverse_for(interval))
        print("--------------------------")
        print(*reverse_while(interval))


if __name__ == "__main__":
    main()