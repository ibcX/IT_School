
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_tuple2 = 1, 2
print(*my_tuple)
print(type(my_tuple2))

print(my_tuple[0:5])
# my_tuple[0] = 10    nu se pot schimba datele din tuple

my_tuple = (1, 2, True, False, 1)
print(1 in my_tuple)

# unpacking tuple:
a, b, c, d, e = my_tuple
print(a, b, c, d, e)

a, b, *c = my_tuple
print(a, b, c)

a, b, *c, d = my_tuple   #pune toate elementele pana la penultimul la c
print(a, b, c, d)

# modificarea unui tuple:
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list[0] = "a"
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

#joining tuples
my_tuple1 = (1, 2, 3)
my_tuple2 = (3, 4, 5)
my_tuple3 = my_tuple1+my_tuple2
print(my_tuple3)

# multiplying elements
my_tuple1 = (1, 2, 3)
my_tuple2 = my_tuple1*3
print(my_tuple2)

# methods: .count; .index
