import random

number = random.randint(1, 100)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = None
while 1:
    level = int(input('Select difficulty level: '))
    if level not in levels.keys():
        print('You have only three difficult levels: 1, 2, 3')
        continue
    break

max_count = levels[level]

user_count = int(input('Enter the number of users: '))
users = []
for i in range(user_count):
    user_name = input(f'Enter user name {i+1}: ')
    users.append(user_name)

is_winner = False
winner = None

while not is_winner:
    count += 1
    if count > max_count:
        print('All users are lose.')
        break
    print(f'Try # {count}')

    for user in users:
        print(f'Play user - {user}')
        user_number = int(input('Enter a number: '))
        if user_number == number:
            is_winner = True
            winner = user
            break
        elif number < user_number:
            print('Your number is greater')
        else:
            print('Your number is less')

else:
    print(f'Winner is - {winner}. Congrats!!!')
