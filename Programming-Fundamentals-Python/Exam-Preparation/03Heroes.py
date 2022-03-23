def heroes_func():
    heroes_dict = {}
    number_of_heroes = int(input())
    for num in range(1, number_of_heroes + 1):
        heroes = input().split()
        hero = heroes[0]
        hp = int(heroes[1])
        mp = int(heroes[2])
        heroes_dict[hero] = [hp, mp]

    return heroes_dict  # input: {hero name} {HP} {MP}


def start_game():
    main_dict = heroes_func()
    line = input()

    while line != 'End':  # Input: End command at the End
        line = line.split(' - ')
        command = line[0]
        hero = line[1]

        if command == 'CastSpell':  # input: CastSpell – {hero name} – {MP needed} – {spell name}
            if hero in main_dict:
                mp = main_dict[hero][1]
                needed_mp = int(line[2])
                spell_name = line[3]
                if mp >= needed_mp:
                    mp -= needed_mp
                    main_dict[hero][1] = mp
                    print(f"{hero} has successfully cast {spell_name} and now has {mp} MP!")
                else:
                    print(f"{hero} does not have enough MP to cast {spell_name}!")

        if command == 'TakeDamage':  # input: TakeDamage – {hero name} – {damage} – {attacker}
            hp = main_dict[hero][0]
            damage = int(line[2])
            attacker = line[3]
            if hp - damage > 0:
                main_dict[hero][0] -= damage
                print(f'{hero} was hit for {damage} HP by {attacker} and now has {main_dict[hero][0]} HP left!')
            else:
                print(f"{hero} has been killed by {attacker}!")
                main_dict.pop(hero)

        if command == 'Recharge':  # input: Recharge – {hero name} – {amount}
            recharge = int(line[2])
            if main_dict[hero][1] + recharge <= 200:
                main_dict[hero][1] += recharge
                print(f"{hero} recharged for {recharge} MP!")
            else:
                print(f"{hero} recharged for {abs(200 - main_dict[hero][1])} MP!")
                main_dict[hero][1] = 200

        if command == 'Heal':  # input: Heal – {hero name} – {amount}
            amount = int(line[2])
            if main_dict[hero][0] + amount <= 100:
                main_dict[hero][0] += amount
                print(f"{hero} healed for {amount} HP!")
            else:
                print(f"{hero} healed for {abs(100 - main_dict[hero][0])} HP!")
                main_dict[hero][0] = 100

        line = input()
    return main_dict


data = start_game()

for key, value in data.items():
    print(key)
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')
