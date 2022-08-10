
# Write a program that finds and prints the largest number from a list of lists

my_list = [[-1, -2, 2], [22, -21, -22], [-11, -1, -2, 30], 200, [-21, 32]]

# definim variabila max_num:
if type(my_list[0]) == int:
    max_num = my_list[0]
else:
    max_num = my_list[0][0]

# aflam maximul:
for elem_list_1 in my_list:
    if type(elem_list_1) == int:
        if elem_list_1 > max_num:
            max_num = elem_list_1
    else:
        for elem_list_2 in elem_list_1:
            if elem_list_2 > max_num:
                max_num = elem_list_2

print(f"Maximul din lista este: {max_num}")


