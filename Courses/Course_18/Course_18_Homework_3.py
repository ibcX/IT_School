# PASWWORD VERIFICATION

# O functie ce verifica daca o parola respecta cerintele:
# Sa aibe cel putin un numar, sa aibe cel putin un caracter special,
# sa aibe o cel putin o litera mare si sa fie de cel putin dimensiune 8
#
# Examplu:
# Input : R@m@_f0rtu9e$
# Output : Valid Password
#
# Input : Ramafortune$
# Output : Invalid Password
# Explanation: Number is missing
#
# Input : Rama#fortu9e
# Output : Invalid Password
# Explanation: Must consist from  or @ or $


upper_chars = "ABCDEFGHIJKLMNOPQRSTUVXZ"
lower_chars = "abcdefghijklmnopqrstuvxz"
numbers = "0123456789"
special_chars = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

upper_in_pass = False
lower_in_pass = False
number_in_pass = False
special_in_pass = False

password = input("Insert password to be verified: ")

for character in password:
    if character in upper_chars:
        upper_in_pass = True
    if character in lower_chars:
        lower_in_pass = True
    if character in numbers:
        number_in_pass = True
    if character in special_chars:
        special_in_pass = True

if upper_in_pass and lower_in_pass and number_in_pass and number_in_pass and special_in_pass and len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")
if not upper_in_pass:
    print("Upper character is missing!")
if not lower_in_pass:
    print("Lower character is missing!")
if not number_in_pass:
    print("Number character is missing!")
if not special_in_pass:
    print("Special character is missing!")
if len(password) < 8:
    print("Length of the password must be at least 8 character long!")
