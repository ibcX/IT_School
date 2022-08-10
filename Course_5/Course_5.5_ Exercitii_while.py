# print Salutare de 5 ori
import numbers
from typing import List

i = 1

while i <=5:
    print("Salutare")
    i += 1

# print Hello
str = "Hello"
i = 0
while i <= len("Hello")-1:
    if str[i] == "e" or str[i] == "e":
        i += 1
        continue
    print(str[i])
    i += 1

# Iesi din loop cand dai de l:
str = "Hello"
i = 0
while i <= len("Hello")-1:
    if str[i] == "l":
        break
    print(str[i])
    i += 1

numbers = list()
i = 0
while i <= 4:
    number = input(f"Numarul {i+1} = ")
    try:
        number=float(number)
        numbers.append(float(number))
        i += 1
    except:
        print("It's not a number")

average = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])/5
print(average)

