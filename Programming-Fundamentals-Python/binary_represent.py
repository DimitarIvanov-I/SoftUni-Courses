n = int(input())
number = n
b = int(input())
binary_code = []
count = 0
while n > 0:
    if n % 2 == 0 and n != 0:
        binary_code.append(0)
        n = n // 2
    else:
        binary_code.append(1)
        n = n // 2

for i in range(len(binary_code)):
    if b == binary_code[i]:
        count += 1

print(f"The binary code of {number} is: 0b" + ''.join(map(str, reversed(binary_code))))
print(f"The {b} count is: {count}")