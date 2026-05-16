import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(msg):
    print(f"==> {msg}")

def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False

###############################################

while True:

    prompt(MESSAGES['welcome'])

    # ask the user for the first number.
    prompt(MESSAGES['first_number'])
    num1 = input()

    while invalid_number(num1):
        prompt(MESSAGES['invalid_number'])
        num1 = input()

    # ask the user for the second number.
    prompt(MESSAGES['second_number'])
    num2 = input()

    while invalid_number(num2):
        prompt(MESSAGES['invalid_number'])
        num2 = input()

    # ask the user for an operation to perform.
    prompt(
        f"{MESSAGES['operation']}\n"
        f"1) {MESSAGES['add']} "
        f"2) {MESSAGES['subtract']} "
        f"3) {MESSAGES['multiply']} "
        f"4) {MESSAGES['divide']}")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(f"{MESSAGES['choose']} 1, 2, 3, or 4")
        operation = input()

    # perform the operation on the two numbers.
    match operation:
        case '1':
            output = int(num1) + int(num2)
        case '2':
            output = int(num1) - int(num2)
        case '3':
            output = int(num1) * int(num2)
        case '4':
            output = int(num1) / int(num2)

    # print the result to the terminal.
    prompt(f"{MESSAGES['result']}: {output}")

    prompt(MESSAGES['operation_two'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break