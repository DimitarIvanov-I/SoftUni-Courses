elements = input().split(' ')
line = input()
number_of_moves = 0
single_element = set(elements)

while line != "end":
    numbers = line.split(' ')
    index1 = numbers[0]
    index2 = numbers[1]
    middle = abs(int(len(elements)) // 2)

    if 0 >= int(index1) or int(index1) > len(elements):
        number_of_moves += 1
        elements.insert(middle, f'-{number_of_moves}a')
        if 0 >= int(index2) or int(index2) > len(elements):
            elements.insert(middle, f'-{number_of_moves}a')
        print("Invalid input! Adding additional elements to the board")
    else:
        current_move_a = elements[int(index1)]
        current_move_b = elements[int(index2)]

        if current_move_a == current_move_b:
            number_of_moves += 1
            elements.pop(int(index1))
            elements.pop(int(index2))
            print(f"Congrats! You have found matching elements - {current_move_a}!")
        else:
            number_of_moves += 1
            print("Try again!")

    line = input()

if index1 in elements[:-1] and index2 not in elements[:-1]:
    print(f"You have won in {number_of_moves} turns!")

if index1 not in elements[:-1]:
    print(f"Sorry you lose :(")
    print(' '.join(elements))
