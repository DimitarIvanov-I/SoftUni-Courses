def decryption(data): # 72olle 103doo 100ya
    new_list = ''
    for word in range(len(data)):
            code = ''.join([n for n in data[word] if n.isdigit()])
            list_of_word = list(data[word])
            list_of_code = list(code)
            for i in range(len(list_of_code)):
                list_of_word.remove(list_of_code[i])
            letter = chr(int(code))
            list_of_word[0], list_of_word[-1] = list_of_word[-1], list_of_word[0]
            list_of_word.insert(0, letter)
            new_list += ''.join(list_of_word) + ' '
    print(new_list)


input_text = input().split(' ')
decryption(input_text)
