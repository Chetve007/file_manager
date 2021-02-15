import random

min_number = 1
max_number = 100
result = None
count = 1

while result != '=':
    print(f'Try number {count}')
    number = random.randint(min_number, max_number)
    print(number)
    result = input('= > <: ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number - 1

    if count == 10:
        print('Computer looose!')
        break
    count += 1
else:
    if count > 6:
        print('It was very hard for you, but you did it!')
    else:
        print('Well done!!! You win!')
