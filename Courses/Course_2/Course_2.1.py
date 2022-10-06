
a = "Acasa"
print(a)
print(a[3])    # String index
print(a[0])
print(len(a))
print(a[0:5], a[:], a[1:], a[:4])
# String slicing
numere = "0123456789"
print(numere[0:9:3])
print(numere[:5])  # daca start_index nu e specificat by default e 0
print(numere[5:])  # daca stop_index nu e specificat by default e len(numere)-1

print(numere[len(numere)-2:])
print(numere[-2:])

print(numere[::-1])

print(numere[len(numere)-1:-4:-1])

