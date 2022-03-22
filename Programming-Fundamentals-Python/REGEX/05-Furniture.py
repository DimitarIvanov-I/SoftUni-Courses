import re
expression = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+[|.\d]+)!(?P<quantity>\d+)"
text = input()
total_price = 0
furniture_list = list()
while True:

    if text == 'Purchase':
        break

    matches = re.finditer(expression, text)


    for match in matches:
        furniture = match.group("furniture")
        furniture_list.append(furniture)
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total_price += price * quantity

    text = input()

print("Bought furniture:")
for item in furniture_list:
    print(str(item))
print(f'Total money spend: {total_price:.2f}')