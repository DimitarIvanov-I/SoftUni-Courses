def average_rating_func(final_dict):
    for rate in final_dict.values():
        if len(rate) > 2:
            count = 0
            total_sum = 0
            for index in range(len(rate) - 1, 0, -1):
                if rate[index] == 0:
                    rate.pop(index)
                else:
                    total_sum += int(rate.pop(index))
                    count += 1
            rate.append(total_sum / count)
    return final_dict


def plant_func():
    plant_dict = {}
    num_of_plants = int(input())

    for num in range(num_of_plants):
        plant = input().split('<->')
        plant_name = plant[0]
        plant_rarity = int(plant[1])
        if plant_name not in plant_dict:
            plant_dict[plant_name] = [plant_rarity]
        else:
            plant_dict[plant_name].pop(0)
            plant_dict[plant_name].append(plant_rarity)

    return plant_dict


def exhibition_func():
    exhibition_dict = plant_func()
    command = input()

    while True:
        if command == 'Exhibition':
            break
        else:
            command = command.split(': ')

        if command[0] == 'Rate':
            rating = command[1].split(' - ')
            plant_name = rating[0]
            plant_rating = int(rating[1])

            if plant_name in exhibition_dict.keys():
                exhibition_dict[plant_name].append(plant_rating)
            else:
                print("error")

        elif command[0] == 'Update':
            update = command[1].split(' - ')
            plant_name = update[0]
            plant_update = int(update[1])

            if plant_name in exhibition_dict.keys():
                exhibition_dict[plant_name].pop(0)
                exhibition_dict[plant_name].insert(0, plant_update)
            else:
                print("error")

        elif command[0] == 'Reset':
            plant_name = command[1]
            if plant_name in exhibition_dict.keys():
                for i in range(len(exhibition_dict[plant_name]) - 1, 0, -1):
                    exhibition_dict[plant_name].pop(i)
                exhibition_dict[plant_name].append(0)
            else:
                print("error")

        command = input()

    final_dict = average_rating_func(exhibition_dict)

    print("Plants for the exhibition:")
    for key, value in final_dict.items():
        if len(value) < 2:
            print(f'- {key}; Rarity: {value[0]}; Rating: {0:.2f}')
        else:
            print(f'- {key}; Rarity: {value[0]}; Rating: {float(value[1]):.2f}')


exhibition_func()
