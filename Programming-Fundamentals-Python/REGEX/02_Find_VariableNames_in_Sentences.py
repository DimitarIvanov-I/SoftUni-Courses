import re

text = input()
expression = r"(?<=_)([a-zA-Z0-9]+)"

matches = re.finditer(expression, text)

output = list()
for match in matches:
    output.append(match.group())

print(",".join(output))
