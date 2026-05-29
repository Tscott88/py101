# Build a program that displays when the user will retire 
# and how many years she has to work till retirement.

from datetime import datetime

print('What is your age?')
age = int(input())
print('At what age would you like to retire?')
retire_age = int(input())

this_year = datetime.now().year
remaining_years = retire_age - age
retirement = this_year + remaining_years

print(f"It's {this_year}. You will retire in {retirement}")
print(f"You have {remaining_years} years of work to go!")
