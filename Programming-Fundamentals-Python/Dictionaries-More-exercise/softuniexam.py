def banned_func(line, main_dict):
    command = line.split("-")
    student = command[0]
    for x in main_dict.values():
        for y in x:
            if student == y:
                del x[student]
                break
    return main_dict


def fund_statistics():
    line = input()
    main_dict = {}
    total_submissions = {}

    while True:
        if 'banned' in line:
            banned_func(line, main_dict)
            line = input()
        if line == 'exam finished':
            break

        command = line.split("-")
        student = command[0]
        language = command[1]
        points = int(command[2])
        if language not in total_submissions.keys():
            total_submissions[language] = 0
        if language not in main_dict.keys():
            main_dict[language] = {student: points}
            total_submissions[language] += 1
        else:
            if student not in main_dict[language]:
                main_dict[language][student] = points
                total_submissions[language] += 1
            else:
                if main_dict[language][student] < points:
                    main_dict[language].update({student: points})
                    total_submissions[language] += 1
                else:
                    total_submissions[language] += 1

        line = input()
    print("Results:")
    for results in main_dict.values():
        for key, val in results.items():
            print(f'{key} | {val}')
    print("Submissions:")
    for course, count in total_submissions.items():
        print(f'{course} - {count}')


fund_statistics()
