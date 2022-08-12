# Game of Thrones
# Dothraki plănuiesc să usurpe tronul Regelui Robert. Regele Robert aude de această conspirație de la un raven și plănuiește să încuie singura ușă prin care inamicul poate să pătrundă în regat lui.
#     Dar această ușă are nevoie de o cheie care este reprezentată de către anagrama unui palindrom. începe să caute în cutia lui de șiruri de caractere, verificând pe fiecare în parte dacă poate fi rearanjat într-un palindrom.
# Cerință:
#     Pentru un șir de caractere, să se tipărească pe ecran cuvântul DA sau NU dacă acest șir poate fi rearanjat astfel încât să fie un palindrom.
# Constrangeri:
# Poate fi folosite doar caractere din alfabetul latin cu litere mici
# Date de intrare:
#     Șirul de caractere.
# Exemplu:
# INPUT:
# aaabbbb
# OUTPUT:
# DA
# Șirul poate fi permutat astfel: bbaaabb

char_list = "abcdefghijklmnopqrstuvwxyz"

while True:
    check_latin_char = True
    odd_count = 0

    word_input = input("Insert a word to check if it is a palindrome or enter command 'exit' to exit the program: \n>")
    if len(word_input) < 2:
        print("The word must be at least two characters long!\n")
        continue

    elif word_input == "exit":
        break
    else:
        i = 0
        for character in word_input:
            if character not in char_list:
                check_latin_char = False
            j = 0
            count = 0
            for j in word_input[i:]:
                if character == j:
                    count += 1
            if count % 2 == 1:
                odd_count += 1

        if not check_latin_char:
            print("The word must contain only lowercase Latin alphabet characters!\n")
            continue

        if odd_count > 1:
            print("NO")
        else:
            print("YES")
