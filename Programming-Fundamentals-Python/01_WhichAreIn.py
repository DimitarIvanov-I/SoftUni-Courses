first_seq = input().split(', ')
second_seq = input().split(', ')
new_seq = []

for i in range(len(first_seq)):
    substring = first_seq[i]
    for j in range(len(second_seq)):
        string = second_seq[j]
        if substring in string:
            if substring not in new_seq:
                new_seq.append(first_seq[i])

print(new_seq)

