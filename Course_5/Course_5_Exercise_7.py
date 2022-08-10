
# Finding the sum of numbers in a list using while
# loop

num_list = [1, 3, 23, 5, 10, -1, -4]

i = 0
sum = 0
while i < len(num_list):
    sum += num_list[i]
    i += 1

print("Suma numerelor din lista este: ", sum)
