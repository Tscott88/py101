def prompt(msg):
    print(f'==> {msg}')

def invalid_num(num):
    try:
        float(num)
    except ValueError:
        return True

    return False

prompt('Welcome to the tip calculator...')
prompt('What is the bill for the meal? ')
bill = input()

while invalid_num(bill):
    prompt('That is in invalid number. Please enter the amount for the bill')
    bill = input()

prompt('What is the percentage you would like to tip? ')
tip_percent = input()

while invalid_num(tip_percent):
    prompt('That is in invalid number. Please enter the amount you\'ll tip')
    tip_percent = input()

meal_tip = ((float(tip_percent) / 100) * float(bill))
meal_total = float(bill) + meal_tip

print()
prompt(f'The tip is ${meal_tip:.2f}')
prompt(f'The total is ${meal_total:.2f}')
