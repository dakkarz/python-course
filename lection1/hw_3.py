import re

from datetime import date


def check_input(input_key, input_value):
    if input_key == 'year':
        reg_pat = r"[0-9]{4}"
    else:
        reg_pat = r"[a-zA-Z]+"

    reg_res = re.findall(reg_pat, input_value)

    if len(reg_res) == 0:
        return False
    elif len(reg_res) != 0 and reg_res[0] == input_value:
        return True
    else:
        return False


def validate_input(input_key):
    input_value = input(f"Input your {input_key}: ")
    while check_input(input_key, input_value) != True:
        print(f"Incorrect {input_key}")
        input_value = input(f"Input your {input_key}: ")
    return input_value 


while True:
    input_name = validate_input('name')
    input_surname = validate_input('surname')
    input_year = validate_input('year')
    break


today = date.today() 
year_today = today.year
age = year_today - int(input_year)


print(f"Hello {input_name} {input_surname} your age is {age} year")