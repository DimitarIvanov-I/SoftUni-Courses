def skip_take_func(skip, take, letters_list):
    skipped_list = []
    taken_list = []
    encrypted_list = ''
    for i in range(len(take)):
        index1 = int(take[i])
        index2 = int(skip[i])
        taken_list = ''.join(letters_list[:index1])
        encrypted_list += ''.join([str(x) for x in taken_list])  # [str(taken_list[x]) for x in range(len(taken_list))]
        del letters_list[:index1]
        skipped_list.append(letters_list[:index2])
        del letters_list[:index2]

    return str(encrypted_list)


def lists(string):
    converted_list = list(string.split())
    numbers_string = []
    take_list = []
    skip_list = []
    non_numbers_list = []
    for index in range(len(string)):
        if string[index].isdigit():
            numbers_string.append(string[index])
            take_list = [numbers_string[x] for x in range(len(numbers_string)) if x % 2 == 0]
            skip_list = [numbers_string[x] for x in range(len(numbers_string)) if x % 2 != 0]
        else:
            non_numbers_list.append(input_string[index])
    print(skip_take_func(skip_list, take_list, non_numbers_list))


input_string = input()
lists(input_string)
