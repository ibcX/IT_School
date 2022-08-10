

# IF

a = 1
b = 9

if a > b:
    print("A")
elif a == b:
    print("Egal")
elif a + b == 10:
    print("10")
else:
    print("B")

if a != b: print("not equal")

print("A") if a > b else print("B")

# folosim cuvantul pass daca vrem sa trecem peste o conditie (cand nu avem cod inca)

if a < b:
    pass
else:
    print("E")

