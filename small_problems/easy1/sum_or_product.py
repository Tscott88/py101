# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product
# of all numbers between 1 and the entered integer, inclusive.
# Finally, share the result with them.
count = 0
def prompt(msg):
    print(f'==> {msg}')

def invalid_num(num):
    try:
        int(num)
    except ValueError:
        return True

    return False

def sum_of_num(num):
    return sum(range(1, int(num) + 1))

def product_of_num(num):
    result = 1
    for i in range(1, int(num) + 1):
        result *= i
    return result

###################################

prompt('Please enter an real number greater than 0: ')
number = input()

while invalid_num(number):
    prompt('Please enter a valid real number only')
    number = input()

prompt('Enter "s" to compute the sum, or "p" to compute the product.')
choice = input()

while choice not in ['s', 'p']:
    prompt('That is not a valid selelection. Please select "s" or "p"')
    choice = input()

match choice:
    case 's': prompt(sum_of_num(number))
    case 'p': prompt(product_of_num(number))
    case _: prompt('Unkwown Error')