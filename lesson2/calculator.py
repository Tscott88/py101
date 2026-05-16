def prompt(msg):
    print(f"==> {msg}")

def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False

###############################################

prompt('Welcome to Calculator!')

# ask the user for the first number.
prompt("What's the first number?")
num1 = input()

while invalid_number(num1):
    prompt("Hmm... that doesn't look like a valid number.")
    num1 = input()

# ask the user for the second number.
prompt("What's the second number?")
num2 = input()

while invalid_number(num2):
    prompt("Hmm... that doesn't look like a valid number.")
    num2 = input()

# ask the user for an operation to perform.
prompt('What operation would you like to perform?\n \
       1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
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
prompt(f"The result is: {output}")