software_version = input().split('.')
string = ''

for i in range(len(software_version) - 1, -1, - 1):
    new_version = []
    last_version = software_version[i]
    if int(last_version) < 9:
        last_version = int(software_version[i]) + 1
        new_version.append(str(last_version))
        software_version.pop(i)
        software_version.insert(i, str(new_version[0]))
        string ='.'.join(software_version)
        break
    else:
        software_version.pop(i)
        software_version.append("0")
        continue

print(string)