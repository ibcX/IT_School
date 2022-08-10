# Write a hangman game:
# The words are in a list and one of them is chosen randomly
# User selects a letter , if present in word , the letter reveals itself
# The user has 5 lives, game ends if the user finds all letters of the word or runs out of lives

import random

words = ['casa', 'python', 'masina', 'autobuz']


Version1
chosen_word =words[random.randint(0, len(words) -1)]
print(chosen_word)

Version2
chosen_word = random.choice(words)
lives = 5
print(chosen_word)
guess_word = "_" * len(chosen_word)
print(guess_word)
user_guessed_letters_correctly = set()

while True:
    user_input = input("Specify a letter:")
    if len(user_input) > 1:
        print("PLease add only one character!")
        continue

    if user_input in chosen_word:
        user_guessed_letters_correctly.add(user_input)
    else:
        lives = lives-1
    guess_word = ""
    for letter in chosen_word:
        if letter in user_guessed_letters_correctly:
            guess_word = guess_word+letter
        else:
            guess_word = guess_word+"_"
    print(guess_word)
    print(f'Lives {lives}')
    if guess_word == chosen_word:
        print("Congrats!")
        break
    if lives == 0:
        print("Sorry, try again!")
        break



# Hangman V2 prima si ultima litera la vedere
# words = ['casa', 'python', 'masina', 'autobuz']
#
# chosen_word =words[random.randint(0, len(words) -1)].upper()
#
# print(chosen_word)
#
# hangman_word = chosen_word[0] + "_"*(len(chosen_word)-2) + chosen_word[-1]
#
# hangman_word = list(hangman_word)
#
# for i in range(0, len(chosen_word)):
#     if chosen_word[i] == chosen_word[0] or chosen_word[i] == chosen_word[-1]:
#         hangman_word[i] = chosen_word[i]
#
#
# backup_word = hangman_word
# hangman_word = str()
#
# for i in range(0, len(backup_word)):
#     hangman_word = hangman_word +backup_word[i]
#
#
#
#
# for i in range(0, 5):
#     if i == 4:
#         print("Ultima sansa")
#     else:
#         print(f"Mai ai {5-i}")
#
#     print(hangman_word)
#
#     print("Enter a letter or the word:")
#     user_input = input().upper()
#     if user_input == chosen_word:
#         print("Congrats, this is the word!")
#         print(chosen_word)
#         break
#     else:
#         for j in range(0, len(chosen_word)):
#             if chosen_word[j] == user_input:
#                 hangman_word = list(hangman_word)
#                 hangman_word[j] = user_input
#                 backup_word = hangman_word
#                 hangman_word = str()
#                 for x in range(0, len(backup_word)):
#                     hangman_word = hangman_word +backup_word[x]
#
#     if i < 5 and hangman_word == chosen_word:
#         print("This is the chosen word !")
#         print(chosen_word)
#         break
#     elif i == 4 :
#         print("Ai pierdut!")