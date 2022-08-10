
#The user will input 5 numbers (one at a time)
# print the min and the max values


num = float(input(f"Introduceti primul numar: "))
min = max = num
i = 1
while i < 5:
    num = float(input(f"Introduceti numarul {i+1}: "))

    if num < min:
        min = num
    elif num > max:
        max = num
    i += 1

print(f"Cel mai mic numár este: {min}")
print(f"Cel mai mare numar este: {max}")
