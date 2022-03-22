fires_string = input().split('#')
water_amount = int(input())
effort = 0
total_fire = 0
new_fire_list = []

print('Cells:')
for i in range(len(fires_string)):
    new_fire_list = fires_string[i].split(' = ')

    if water_amount - int(new_fire_list[1]) >= 0:

        if new_fire_list[0] == 'High':
            if 85 <= int(new_fire_list[1]) <= 125:
                water_amount -= int(new_fire_list[1])
                effort += int(new_fire_list[1]) * 0.25
                print(f' - {int(new_fire_list[1])}')
                total_fire += int(new_fire_list[1])

        elif new_fire_list[0] == 'Medium':
            if 51 <= int(new_fire_list[1]) <= 80:
                water_amount -= int(new_fire_list[1])
                effort += int(new_fire_list[1]) * 0.25
                print(f' - {int(new_fire_list[1])}')
                total_fire += int(new_fire_list[1])

        elif new_fire_list[0] == 'Low':
            if 1 <= int(new_fire_list[1]) <= 50:
                water_amount -= int(new_fire_list[1])
                effort += int(new_fire_list[1]) * 0.25
                print(f' - {int(new_fire_list[1])}')
                total_fire += int(new_fire_list[1])
    else:
        continue

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
