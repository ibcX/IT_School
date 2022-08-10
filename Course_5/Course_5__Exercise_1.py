
#Exercise_1: Retrieve from the user using the input() method 5 numbers and print the average

# Varianta 1: inserarea valorilor primite intr-o lista:

# numbers = list()
#
# i = 0
#
# while i <= 4:
#     number = input(f"Numarul {i + 1} = ")
#     try:
#         number = float(number)
#     except:
#         print(f'"{number}" is not a number. Insert number {i+1} again')
#     else:
#         numbers.append(float(number))
#         i += 1
#
# average = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]) / 5
# print(f"\nAverage is: {average}")

# OR:
# # Varianta 2: fara ajutorul unei liste, adunand de fiecare data numarul introdus la suma numerelor precedente:

# i = 0
# sum = 0
#
# while i <= 4:
#     number = input(f"Number {i + 1} = ")
#     try:
#         number = float(number)
#     except:
#         print(f'"{number}" is not a number. Insert number {i+1} again')
#     else:
#         sum = sum + float(number)
#         i += 1
#
# average = sum / 5
# print(f"Average is: {average}")

# OR:
# # Varianta 3: pentru un numar indefinit de valori. Daca se introduce "stop", se calculeaza media:

# count = 0
# sum = 0
# number = 0
# while number != "stop":
#     number = input(f"Number {count+1} = ")
#     if number != "stop":
#         try:
#             number = float(number)
#         except:
#             print(f'"{number}" is not a number. Insert number {count+1} again')
#         else:
#             sum = sum + float(number)
#             count += 1
#     else:
#         break
#
# average = sum / count
# print(f"Average is: {average}")

# OR:
# Varianta 4: ceva mai complex... am vrut sa ii intrebi pe utilizator daca mai doreste sa introduca un numar:

# count = 1
# insert = ""
# number = ""
# while type(number) == str:
#     number = input(f"Insert first number = ")
#     try:
#         number = float(number)
#     except:
#         print(f'"{number}" is not a number. Insert first number again')
#     else:
#         sum = number
#         while insert != "n" or insert != "y":
#             insert = input("Insert another number? (y/n): ")
#             if insert == "n":
#                 break
#             elif insert == "y":
#                 count += 1
#                 while insert != "n":
#                     number = input(f"Insert number {count} = ")
#                     try:
#                         number = float(number)
#                     except:
#                         print(f'"{number}" is not a number. Insert number {count} again')
#                     else:
#                         sum = sum + float(number)
#                         while insert != "n" or insert != "y":
#                             insert = input(f"Insert another number? (y/n): ")
#                             if insert == "n":
#                                 break
#                             elif insert == "y":
#                                 count += 1
#                                 break
#             if insert == "n":
#                 break
#
# average = sum / (count)
# print(f"Average is: {average}")
