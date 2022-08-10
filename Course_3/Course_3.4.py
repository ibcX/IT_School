
# Liste

# my_list = ["mar", "banana", "Kiwi"]
#
# print(type(my_list))

#
# my_list = list(("mar", "banana", "Kiwi"))         # functia constrictor
# print(*my_list)

#
# my_list = list(("mar", "banana", "Kiwi"))
# print("mar" in my_list)
#
# my_list2 = ["mar", True, 2.5]
# my_list2[0] = "kiwi"
# print(my_list2)
#
# my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list3[1:3] = ["a", "b", "c", "d", "e"]
# print(my_list3)

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.insert(2, "Salut")
# print(my_list)

# my_list = [1, 2, 3]
# my_list2 = [4, 5, 6]
# my_list.extend(my_list2)                       # extend - adauga la o lista alta lista  # append ar adauga lista ca un element
# print(my_list)
# print(my_list.count(3)) # de cate ori se afla nr intr o lista

# stergerea unui element cu .REMOVE
# stergerea unui element de la un anumit index cu .POP

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 5]
# print(my_list)
# a = my_list.remove(5)
# print(a)
# print(my_list)
#
# a = my_list.pop(5)    #index
# print(a)
# print(my_list)
# my_list.clear()
# print(my_list)

# a = [1, 2, 3]
# b = a          # b este acelasi lucru cu a-ului
# c = a.copy()      # c este copia originala a a-ului
# #sau c = list(a)
# print(a)
# print(b)
# print(c)
# a.append(4)
# print(a)
# print(b)
# print(c)

fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits)
fruits[1:2]= ["mar", "cireasa"]
print(fruits)
masini = ["volvo", "dacia", "aro"]
fruits.extend(masini)
print(fruits)
a = fruits.pop(4)
print(a)
fruits.remove("aro")
print(fruits)

