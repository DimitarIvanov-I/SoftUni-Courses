travelers = int(input())
lift_state = list(map(int, input().split(' ')))

for car in range(len(lift_state)):
    cartridge = int(lift_state[car])
    current_empty_space = 4 - cartridge

    if current_empty_space == 0:
        continue

    if travelers == 0:
        break

    if travelers >= current_empty_space:
        travelers -= current_empty_space
        lift_state.pop(car)
        lift_state.insert(car, current_empty_space + cartridge)

    elif travelers < current_empty_space:
        lift_state.pop(car)
        lift_state.insert(car, travelers)
        travelers -= travelers
        print("The lift has empty spots!")

if travelers > 0:
    print(f"There isn't enough space! {travelers} people in a queue!")

filled_lift = list(map(str, lift_state))
print(' '.join(filled_lift))