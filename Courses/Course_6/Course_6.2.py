
# print all keys in a dictionary

dictionary = {
    1: "a",
    2: "b",
    3: "c",
    "a": 3
}

# for key in dictionary:
#     print(key)   # cheie
#     print(dictionary[key])  # valoarea
#
# print("With packing")
# for key, item in dictionary.items():
#     print(key)   # cheie
#     print(item)  # valoarea
#
# print("Without unpacking")
# for i in dictionary.items():
#     key, item = i
#     print(key)
#     print(item)

my_list = [1, 2, 3, 5, 6, 8, 10]

for element in my_list:
    if element %2 == 0:
        print(element, end=" ")
print("\n")
for i in range(0, len(my_list), 1):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")
