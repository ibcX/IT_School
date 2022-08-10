# Exercitiul 1:

text = "Hello World"
print(text[0])
print(text[2:5])
print(text[::-1])
print("\n")
#Exercitiul 2:

varsta = 28
nume = "Razvan"
my_string = f"{nume} are {varsta} ani"
print(my_string)
my_string2 = "{} are {} ani"
print(my_string2.format(nume, varsta))

my_string3 = "{1} are {0} ani"
print(my_string3.format(varsta, nume))
print("\n")

#Exercitiul 3:
text_2 = "Hello World"
text_modificat = text_2.replace("H", "J")
print(text_modificat)
