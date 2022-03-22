import re
import string
string = input()
regex = r"[A-Za-z']+"

match = re.findall(regex, string)

for i in match:
    

print(count)