# Exercitii
my_tuple = ("a", "b", "c", "d", "e", "f", "g")
a, *b, c = my_tuple
print(a)
print(b)
print(c)
# fie adaugam un element prin unirea a 2 tupleuri
one_element_tuple = ("h",)  # tuple de un singur element
new_tuple = my_tuple+one_element_tuple
print(new_tuple)
# sau trecem prin liste
my_list = list(my_tuple)
my_list.append("h")
my_tuple=tuple(my_list)
print(my_tuple)
print(my_list)

print("a" in my_tuple)
#sau prin atribuirea unei valori unei variabile
is_in_my_tuple = "a" in my_tuple
print(is_in_my_tuple)

my_tuple = (1, 2, True, [15, 20], "test")
print(my_tuple[3][1])
