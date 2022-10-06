
# while loops

counter = 0
while counter < 10:
    print("Jumbo", counter)
    if(counter == 5):
        break  # iese din loop   # continue - termina iteratia
    counter += 1

i = 1
j = 1

while i <= 3:
    print(i, "Outer loop is executed")
    while j <= 3:
        print(j, "inner loop is executed")
        j += 1
    i += 1
