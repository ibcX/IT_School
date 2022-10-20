#                Cool
# Se consideră un șir A format din N elemente naturale nenule.
# Numim secvență de lungime K a șirului A orice succesiune de elemente consecutive
# din șir de forma Ai, Ai+1, ..., Ai+K-1.
# O secvență o numim secvență cool dacă elementele care o compun sunt distincte și pot fi rearanjate astfel
#  încât să alcătuiască o secvență continuă de numere consecutive.
# De exemplu, considerând șirul
# A = (3, 1, 6, 8, 4, 5, 6, 7, 4, 3, 4), atunci secvența
# (8, 4, 5, 6, 7) este o secvență cool deoarece conține elemente distincte ce pot fi rearanjate astfel încât să
# alcătuiască # șirul de numere consecutive 4, 5, 6, 7, 8,
# pe când secvențele (4, 3, 4), (6, 7, 4, 3) nu sunt considerate secvențe cool.
# Cerință:
#     Pentru o valoare dată K să se verifice dacă secvența
#     A1, A2 ... AK este secvență cool.
#     Dacă secvența este cool, atunci se va afișa cea mai mare valoare ce aparține secvenței.
#     Dacă secvența nu este cool, atunci se va afișa numărul elementelor distincte din secvența
# A1, A2, ..., AK, adică numărul elementelor care apar o singură dată.
# Date de intrare:
#     Se citesc N și K de la tastatură care vor determina numărul de elemente din sir
#     respectiv lungimea secvenței cool de verificat.
# Exemple:
# INPUT:
# 7 4
# 6 4 5 7 8 3 5
# OUTPUT:
# 7
# Secvența 6 4 5 7 este cool.
# Valoarea maximă din secvență este 7
# INPUT:
# 7 6
# 6 4 5 7 5 4 3
# OUTPUT:
# 2
# Secvența 6 4 5 7 5 4 nu este secvență cool.
# Numărul valorilor distincte din secvență este 2.
# Valorile distincte sunt: 6, 7

from collections import deque

N = int(input("Insert the number of the elements in the array: > "))
K = int(input("Insert the length of the cool sequence to be verified: > "))


def insert_array():
    array = []
    index = 1
    while index <= N:
        number = int(input(f"Insert number {index}: > "))
        if number < 1:
            continue
        else:
            array.append(number)
        index += 1

    return array


def cool_check(array):
    sequence_cool = []
    sequence_not_cool = []
    sequence_sorted = []

    for index_1 in range(0, N - K + 1):
        queue = []
        cool_bool = True
        for index_2 in array[index_1:index_1 + K]:
            queue.append(index_2)
        sorted_queue = queue.copy()
        sorted_queue.sort()
        sequence_sorted.append(sorted_queue)
        for i in range(1, len(sorted_queue)):
            if (sorted_queue[i] - sorted_queue[i - 1]) != 1:
                cool_bool = False
        if cool_bool:
            sequence_cool.append(queue)
        else:
            sequence_not_cool.append(queue)
    return sequence_cool, sequence_sorted, sequence_not_cool


def count_distinct_numbers(array):
    queue_set = set(array)
    distinct_numbers = []
    for number in queue_set:
        count = array.count(number)
        if count == 1:
            distinct_numbers.append(number)
    return distinct_numbers


def print_sequences():
    array = insert_array()
    sequence_cool, sorted_queue, sequence_not_cool = cool_check(array)

    if len(sequence_cool) > 1:
        print(f"The following sequences are cool: ")
        for sequence in sequence_cool:
            print(f"{sequence} and the biggest number in sequence is {sorted_queue[-1]}")

    elif len(sequence_cool) == 1:
        print(f"The following sequence is cool: {sequence_cool[0]} and the biggest number in sequence is {sorted_queue[0][-1]}")
    else:
        print(f"The sequences {sequence_not_cool} are not cool!")
        distinct_numbers = count_distinct_numbers(array)
        print(f"There are {len(distinct_numbers)} distinct numbers: {distinct_numbers}")


print_sequences()
