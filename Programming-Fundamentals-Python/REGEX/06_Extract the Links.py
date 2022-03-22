import re
string = input()
regex = r"www.(?:[-a-zA-Z0-9.])*\.[a-z]+"
new_list = []
while string != '':

    links = re.finditer(regex, string)
    for link in links:
        new_list.append(link.group())
    string = input()

print("\n".join(new_list))