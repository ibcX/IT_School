# Exercitiul 1: Create a list with elements from 0 to 100 using list comprehension

list_0_to_100 = [i for i in range (0, 101)]
print(f"Rezultatul exercitiului 1 este: \n{list_0_to_100}")



# ● Exercitiul 2: Given the list lst1=[1,2,3,4,5] create an identical list from the first list using list comprehension.

lst1 = [1, 2, 3, 4, 5]
new_list = [i for i in lst1]
print(f"\nRezultatul exercitiului 2 este: \n{new_list}")



# ● Exercitiul 3: Given a list lst1=[2, 4, 6, 8, 10, 12, 14], using list comprehension, construct a new list from the squares of each element in the list lst1.
#
lst1=[2, 4, 6, 8, 10, 12, 14]
new_list = [i*i for i in lst1]
print(f"\nRezultatul exercitiului 3 este: \n{new_list}")


# ● Exercitiul 4: Given a list of numbers original_list = [2,3.75,.04,59.354,6,7.7777,8,9], create a new list without float numbers using list comprehension

original_list = [2, 3.75, .04, 59.354, 6, 7.7777, 8, 9]
new_list = [i for i in original_list if type(i) == int]
print(f"\nRezultatul exercitiului 4 este: \n{new_list}")
