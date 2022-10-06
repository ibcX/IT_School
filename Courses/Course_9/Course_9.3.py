# Functii

def my_function(nume):
    return f"Salutare {nume}"


result = my_function("Razvan")
print(result)

def my_function(nume = "Gigi"):
    return f"Salutare {nume}"


result = my_function()
print(result)


# Adunare, inmultire, impartire, scadere

def adunare (x,y):
    return x+y

print(adunare(10,11))



# functie care sa calculeze suma unei liste de numere primte ca si argument

def sum_list(a_list):
    result_sum = 0
    for number in a_list:
        result_sum += number
    return result_sum

our_sum = sum_list([item for item in range(1, 11)])
print(our_sum)



