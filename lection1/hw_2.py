# Check type of input number


def get_num(input_num):
    try:
        input_num = int(input_num)
        return input_num
    except ValueError:
        try:
            input_num = float(input_num)
            return input_num
        except ValueError:
            return False


while True:
    num1 = input("Input number1: ")
    num2 = input("Input number2: ")
    if get_num(num1) != False and get_num(num2) != False:
        sum = get_num(num1) + get_num(num2)
        print(f"Sum: {sum}")
        break
    else:
        print("You entered an invalid number")