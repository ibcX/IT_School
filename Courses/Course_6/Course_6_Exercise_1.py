
# import random
#
# start_no = 1
# end_no = 10
# chosen_number = random.randint(start_no, end_no)
#
# print(f"Ghiceste un numar intre {start_no} si {end_no}")
#
# while True:
#     my_number = int(input())
#     if my_number > chosen_number:
#         print("Go lower!")
#     elif my_number < chosen_number:
#         print("Go higher!")
#     else:
#         print("You guessed it")
#         break

# add counter

import random

start_no = 1
end_no = 10
chosen_number = random.randint(start_no, end_no)

print(f"Ghiceste un numar intre {start_no} si {end_no}")
counter = 0
while counter < 3:
    my_number = int(input())
    if my_number > chosen_number:
        print("Go lower!")
    elif my_number < chosen_number:
        print("Go higher!")
    else:
        print("You guessed it")
    counter += 1

