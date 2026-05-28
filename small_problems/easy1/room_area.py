# Build a program that asks the user to enter the length and width of a room
# in meters, then prints the room's area in both square meters and square feet.

def invalid_num(num):
    try:
        float(num)
    except ValueError:
        return True

    return False

print('Please enter the length of the room in meters')
length = input()

while invalid_num(length):
    print('Invalid number, please enter the length.')
    length = input()

print('Please enter the width of the room in meters')
width = input()

while invalid_num(width):
    print('Invalid number, please enter the length.')
    width = input()

area_in_meters = float(length) * float(width) # formula for area is L x W

area_in_feet = round((area_in_meters * 10.7639), 2) # meters to sq. ft rounded

print(f'The room area in square meters is: {area_in_meters} \n'
      f'and the room area in square feet is: {area_in_feet}')