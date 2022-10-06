

# The palindrome checker:

# ex:
# Input: aba
# Output: YES

while True:
    word_input = input("Insert a word to check if it is a palindrome or enter command 'exit' to exit the program: \n>")
    if len(word_input)<2:
        print("The word must be at least two characters long!\n")
        continue
    elif word_input == "exit":
        break
    else:
        palindrome = word_input[::-1]

        if palindrome == word_input:
            print("YES")
        else:
            print("NO")
