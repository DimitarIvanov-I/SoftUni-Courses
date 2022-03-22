from collections import defaultdict

def user_func(contest_dict):
    line = input()
    user_dict = {}

    while True:
        if line == 'end of submissions':
            break
        command = line.split("=>")
        course = command[0]
        if course in contest_dict.keys():
            keyword = command[1]
            if keyword in contest_dict.values():
                username = command[2]
                points = int(command[3])
                if course not in user_dict.keys():
                    user_dict[course] = [(username, points)]
                else:
                    for el in user_dict[course]:
                        if username != el[0]:
                            user_dict[course].append((username, points))
                        else:
                            if points > el[1]:
                                user_dict[course].remove(el)
                                user_dict[course].append((username, points))
        line = input()

    new_list = []
    for val in user_dict.values():
        for el in val:
            new_list.append(el)
    counter = defaultdict(int)
    for person, value in new_list:
        counter[person] += value

    candidate = max(counter, key=counter.get)
    max_value = max(counter.values())
    print(f"Best candidate is {candidate} with total {max_value} points.")


def contest_func():
    line = input()
    contest_dict = {}
    while True:
        if line == 'end of contests':
            break
        command = line.split(":")
        contest = command[0]
        password = command[1]
        contest_dict[contest] = password

        line = input()
    user_func(contest_dict)


contest_func()
