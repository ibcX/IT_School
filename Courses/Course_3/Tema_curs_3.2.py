
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
my_list.remove(10)
print(f"Lista fara elementul 10 este: \n{my_list}")

square_index_2 = my_list[2]**2
my_list[2] = square_index_2
print(f"\nLista in care indexul 2 a fost inlocuit cu patratul acestuia, este: \n{my_list}")

print(f"\nValoarea 22 se afla in lista: \n{22 in my_list}")

list_2 = ["salut", "sunt", "razvan"]
my_list.extend(list_2)
print(f"\nLista extinsa este: \n{my_list}")

element_index_10 = my_list.pop(10)
print(f"\nElementul cu indexul 10 este: \n{element_index_10}")

my_list[3:4] = [99, 100]
print(f"\nLista in care elementul de la indexul 3 a fost inlocuit cu [99, 100] este: \n{my_list}")

my_list.clear()
print(f"\nLista stearsa: \n{my_list}")


# Scoate elementul cu valoarea 10 din lista
# Schimba valoarea elementului de pe indexul 2 cu patratul acestuia
# Printeaza daca valoarea 22 se afla in lista
# Extinde lista “list” cu lista [‘salut’, ‘sunt’, ‘razvan’]
# Scoate elementul cu indexul 10 din lista si il printeaza
# Adauga [99,100] in locul elementului de la indexul 3
# Sterge intreaga lista

# https://pastebin.com/YNEVJdqf