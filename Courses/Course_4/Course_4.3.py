
# Seturi

my_set = {2, 1, 3, 4, 5, 5, "a"}
print(my_set)
my_set.add(15)   # adauga un element
print(my_set)
my_set.update([44, 55, 66])  # adauga o lista de elemente
print(my_set)
my_set.remove(44)
print(my_set)
my_set.discard(66)
print(my_set)
print(my_set.pop())  # scoate un elment arbitrar

my_set = {1, 2, 3, 4}
my_set2 = {4, 5, 6}
print(my_set.difference(my_set2))
my_set.difference_update(my_set2)
print(my_set)  # face update la set si elimina elementele comune

my_set = {0, 1, 2, 3, 4}
my_set2 = {4, 5, 6, 1, 2, 3}
print(my_set.intersection(my_set2))
print(my_set.isdisjoint(my_set2))

print(my_set.issubset(my_set2))

print(my_set2.issuperset(my_set))

print(my_set.symmetric_difference(my_set2)) # elementele care apar doar intr un set

print(my_set.union(my_set2))
