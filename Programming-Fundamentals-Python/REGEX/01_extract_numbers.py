import re
string = input()
regex = r"\d+"
new_list = []
while string != '':

    numbers = re.findall(regex, string)
    new_list += numbers
    string = input()

print(" ".join(new_list))