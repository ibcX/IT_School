
# Creeaza o lista in care avem toate numerele de la 0 la 1000

my_list = [number for number in range(0, 1001)]
print(my_list)

# lista in care sa avem numere divizibile cu 8:

my_list = [number for number in range(0,1001) if number % 8 == 0]
print(my_list)

# numere care contin 6:
my_list2 = [number for number in range(0,1001) if "6" in str(number)]
print(my_list2)

# fructe cu litere mari:

fruits = ["apple", "banana", "cherry", "kiwi"]

new_list3 = [fruit.upper() for fruit in fruits]
print(new_list3)

# doar elementele pare din my_list

my_list = [0, 22, 41, 63, 82, 101, 122, 143, 167, 181]
new_list4 = [number for number in my_list if number%2 == 0]
print(new_list4)

# daca este par numarul sa se introduca even cu for

new_list5 = []
for number in my_list:
    if number%2 == 0:
        new_list5.append("even")
    else:
        new_list5.append("odd")

print(new_list5)

new_list6 = ["even" if number%2 == 0 else "odd" for number in my_list]
print(new_list6)

