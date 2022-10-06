
fruits = ["banana", "apple", "cherry", "kiwi"]

new_list = []

for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)

print(new_list)

# newlist= [expression for item in iterable if condition == True]

new_list2 = [fruit for fruit in fruits if "a" in fruit]
print(new_list2)

# Create a new list with elements from 0 to 10

no_list = []

for number in range (0, 11):
    if number>=6: continue
    if number % 2 == 0:
        no_list.append("Par")
    else:
        no_list.append("Impar")
print(no_list)

no_list2 = [number for number in range(0, 11) if number % 2 == 0]
print(no_list2)

no_list3 = ["PAR" if number %2 == 0 else "IMPAR" for number in range(0,11) if number < 6]
print(no_list3)

