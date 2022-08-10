
# Write a program that will compute the factorial of a number imputed by the user (using for loops)

number = int(input("Introduceti numarul: "))

factorial = 1
for i in range(1, number+1, 1):
    factorial *= i

print("Factorialul numarului", number, "este: ", factorial)
