
file = open("test.txt", "a")
file.write("Salut11")
file.close()

with open("test.txt", "a") as file:
    file.write("Salut\n")

file = open("test.txt", "r")
# print(file.readlines())
for line in file:
    print(line)

import os

os.remove("test.txt")
