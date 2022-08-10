
# Get all values from the dictionary and add them to a list but don’t add duplicates (use for loops and do it without for loops)
# data = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

data = {
    'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54
}

# for loop solution:
my_list = [data["jan"]]

for value in data.values():
    if my_list.count(value) == 0:
        my_list.append(value)

print("Lista valorilor din dictionar fara duplicate este: ", my_list)

# without loops:  aici m-am inspirat de pe net...
my_list = list(data.values())
no_duplicates_list = list(dict.fromkeys(my_list))

print("Lista valorilor din dictionar fara duplicate este: ", no_duplicates_list)

# Using sets
my_set = set(data.values())
my_list = list(my_set)

print("Lista valorilor din dictionar fara duplicate este: ", my_list)
