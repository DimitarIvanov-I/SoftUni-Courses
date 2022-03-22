import sys

event_string = input().split('|')
current_energy = 100
initial_coins = 100
new_list = []
gained_energy = 0
new_coins = 0
# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
for i in range(len(event_string)):
    new_list = event_string[i].split('-')

    if new_list[0] == 'rest':
        if current_energy < 100 and gained_energy + current_energy <= 100:
            gained_energy += int(new_list[1])
            current_energy += gained_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {current_energy}.')
            gained_energy = 0
        else:
            print('You gained 0 energy.')
            print(f'Current energy: {current_energy}.')

    elif new_list[0] == 'order':
        if current_energy >= 30:
            current_energy -= 30
            new_coins += int(new_list[1])
            initial_coins += new_coins
            print(f'You earned {new_coins} coins.')
            new_coins = 0
        else:
            current_energy += 50
            print('You had to rest!')

    else:
        item = str(new_list[0])
        if initial_coins >= int(new_list[1]):
            initial_coins -= int(new_list[1])
            print(f'You bought {item}.')
        else:
            print(f'Closed! Cannot afford {item}.')
            sys.exit()

print("Day completed!")
print(f'Coins: {initial_coins}')
print(f'Energy: {current_energy}')

