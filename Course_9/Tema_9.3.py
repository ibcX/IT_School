#  Exercitiile de pe slide-ul 17:

# ● Exercitiul 1: Create a function to reverse a string.

def reverse(string):
    reversed_string = ""
    string = list(string)
    reversed_list = string[::-1]
    for letter in reversed_list:
        reversed_string += letter
    return reversed_string


result = reverse("elephant")

print("Rezultatul primului exercitiu este: ", result)

# ● Exercitiul 2: Create a function that accepts a string and calculate the number of upper case letters.

def upper_calculator(string):
    string=list(string)
    upper_count = 0
    for i in string:
        if i.isupper() == True:
            upper_count += 1
    return upper_count

result = upper_calculator("ElePhAnt")

print("Rezultatul exercitiului 2 este: ", result)

# ● Exercitiul 3: Create a function that squares up a list of numbers and returns the new list with the numbers squared

my_list = [0, 1, 3, 5, 2, 9]

def square_function(number_list):
    new_list = [i*i for i in number_list]
    return new_list

result = square_function(my_list)
print("Rezultatul exercitiului 3 este: ", result)

# ● Exercitiul 4: Create a function that removes all vowels from a string given as argument and returns the new string.

my_string = "Elephant"

def vow_rem_funct(string):
    string = list(string)
    new_string = [i for i in string if i not in "aeiouăâîAEIOUĂÎÂ"]
    new_word = ""
    for i in new_string:
        new_word = new_word + (str(i))
    return new_word

result = vow_rem_funct(my_string)
print("Rezultatul exercitiului 4 este: ", result)
