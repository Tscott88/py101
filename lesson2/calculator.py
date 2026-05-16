print('Welcome to Calculator!')

# ask the user for the first number.
print("What's the first number?")
num1 = int(input())

# ask the user for the second number.
print("What's the second number?")
num2 = int(input())

# ask the user for an operation to perform.
print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = int(input())

# perform the operation on the two numbers.
match operation:
    case 1:
        output = num1 + num2
    case 2:
        output = num1 - num2
    case 3:
        output = num1 * num2
    case 4:
        output = num1 / num2
    case _:
        output = "Please enter your nubmers again please"

# print the result to the terminal.
print(f"The result is: {output}")