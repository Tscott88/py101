def prompt(msg):
    print(f'==> {msg}')

def invalid_num(num):
    try:
        float(num)
    except ValueError:
        return True

    return False

#################################3

prompt('Enter the first number:')
first_num = input()

while invalid_num(first_num):
    prompt('Invalid number, please enter a valid number')
    first_num = input()

prompt('Enter the first number:')
second_num = input()

while invalid_num(second_num):
    prompt('Invalid number, please enter a valid number')
    second_num = input()

first_num = float(first_num)
second_num = float(second_num)

prompt(f'{first_num} + {second_num} = {first_num + second_num}')
prompt(f'{first_num} - {second_num} = {first_num - second_num}')
prompt(f'{first_num} * {second_num} = {first_num * second_num}')
prompt(f'{first_num} / {second_num} = {first_num / second_num}')
prompt(f'{first_num} // {second_num} = {first_num // second_num}')
prompt(f'{first_num} % {second_num} = {first_num % second_num}')
prompt(f'{first_num} ** {second_num} = {first_num ** second_num}')
