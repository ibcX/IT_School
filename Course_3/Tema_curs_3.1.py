
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

last_element = my_list.pop()
first_element = my_list.pop(0)

my_list.append(first_element)
my_list.insert(0, last_element)

print(my_list)

# https://pastebin.com/tgKzhier