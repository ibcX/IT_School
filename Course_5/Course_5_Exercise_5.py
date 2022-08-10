# Write a program that will compute the factorial
# of a number imputed by the user (using while
# loops)

number = int(input("Introduceti numarul: "))
product = 1
i = 1

while i <= number:
    product *= i
    i += 1

print(f"Factorialul numarului {number} este: {product}")

