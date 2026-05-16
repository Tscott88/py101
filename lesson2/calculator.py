LANGUAGE = 'en'
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(msg):
    print(f"==> {msg}")

def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

###############################################

while True:

    prompt(messages('welcome'))

    # ask the user for the first number.
    prompt(messages('first_number'))
    num1 = input()

    while invalid_number(num1):
        prompt(messages('invalid_number'))
        num1 = input()

    # ask the user for the second number.
    prompt(messages('second_number'))
    num2 = input()

    while invalid_number(num2):
        prompt(messages('invalid_number'))
        num2 = input()

    # ask the user for an operation to perform.
    prompt(
        f"{messages('operation')}\n"
        f"1) {messages('add')} "
        f"2) {messages('subtract')} "
        f"3) {messages('multiply')} "
        f"4) {messages('divide')}")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(f"{messages('choose')} 1, 2, 3, or 4")
        operation = input()

    # perform the operation on the two numbers.
    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)

    output = round(output, 2) # round the result to two decimals

    # print the result to the terminal.
    prompt(f"{messages('result')}: {output}")

    prompt(messages('operation_two'))
    answer = input()
    if answer and answer[0].lower() != 'y':
        break