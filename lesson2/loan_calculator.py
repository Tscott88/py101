def prompt(msg):
    print(f"==> {msg}")

def loan_calc(principal, rate, loan_duration):
    p = float(principal)
    j = float(rate)
    n = float(loan_duration)

    return (p * (j / (1 - (1 + j) ** (-n))))

def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True

    return False
############################################

while True:

    # welcome message to users
    prompt('Welcome to the loan calculator!')

    # the amount of the loan
    prompt('Please enter your loan amount: "100,000 = 100000"')
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt('Number must be greater than 0.')
        loan_amount = input()

    # the loan's interest rate, converted to a decimal
    prompt('Plese enter your interest rate: "5% = 5"')
    interest_rate = input()

    while invalid_number(interest_rate):
        prompt('Number must be greater than 0.')
        interest_rate = input()

    interest_rate = (float(interest_rate) / 100) / 12 # monthly interest rate

    # the duration of the loan in months
    prompt('Please enter your loan duration in years: ')
    loan_duration_in_months = input()

    while invalid_number(loan_duration_in_months):
        prompt('Number must be greater than 0.')
        loan_duration_in_months = input()

    # multiplies by 12 to get duration in months
    loan_duration_in_months = float(loan_duration_in_months) * 12

    m = loan_calc(loan_amount, interest_rate, loan_duration_in_months)
    m = round(m, 2)
    prompt(f'Your monthly payment with interest is ${m}\n')

    prompt('Would you like me to preform another calculation? (Y/n) ')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break