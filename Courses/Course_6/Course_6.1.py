
# For loops

my_list = ["a", "b", "c"]

for element in my_list:
    print(element)


for i in range(1, len(my_list)):
    print(my_list[i], end=" ")


adj = ["red", "yellow", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

