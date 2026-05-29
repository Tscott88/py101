def invalid_name(name):
    return not isinstance(name, str) or name.strip() == ''

########################################3

print('What is your name?')
name = input()

while invalid_name(name):
    print('Please enter a valid name')
    name = input()

if name.endswith('!'):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')