
my_set = {1, 2, 3, "a", "b", "c"}
print(my_set)
my_set.add(4)
my_set.update([4, 5, 6])
print(my_set)

set_1 = {"ra", "raz", "python", 1}
set_2 = {1, 2, 3}
print(set_2.issubset(set_1))
print(set_1.difference(set_2))
