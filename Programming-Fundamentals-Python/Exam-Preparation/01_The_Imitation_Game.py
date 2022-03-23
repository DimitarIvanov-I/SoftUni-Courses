encrypted_message = input()

line = input().split('|')
while True:
    if line[0] == 'Decode':
        break
    command = line[0]
    if command == 'Move':
        move = int(line[1])
        slise = encrypted_message[:move]
        encrypted_message = encrypted_message[move:] + slise
    if command == "Insert":
        index = int(line[1])
        value = line[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    if command == 'ChangeAll':
        substring = line[1]
        replacement = line[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring,replacement)
    line = input().split('|')

print(f"The decrypted message is: {encrypted_message}")
