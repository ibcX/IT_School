

"""
Jefuesti o banca, dar nu iei tot. Cauti un obiect specific din cutiile cu valori.Va trebui
sa cauti in feicare pentru a gasi obiectul ce vrei sa il iei, dar cat timp iti va lua
procedura?
Task:
\Determina timpul de a gasi obiectul cautat stiind ca iti ia 5 minute sa cauti
in fiecare cutie cu valori
Input :
Un string ce reprezinta obiectele din fiecare cutie care va fi cautata(obiectele sunt separate de o virgula),iar al doilea string obiectul ce vrei sa il gasesti
Output :
Un numar ce reprezinta timpul ce iti va lua sa gasesti obiectu
ex:
Input:
aur,diamante,documente,tablou picasso,chei
tablou picasso
Output:
20
"""

# cutie_obiecte = input("Lista obiecte cutie valori: ")
#
# obiecte_lista = cutie_obiecte.split(",")
# obiect_cautat = input("Obiectul cautat: ")
# i=1
# timp_total = 1
# if obiect_cautat not in obiecte_lista:
#     print("Obiectul nu se gaseste in cutia respectiva")
# else:
#     # for obiect in obiecte_lista:
#     #     if obiect == obiect_cautat:
#     #         timp_total = 5*i
#     #     i += 1
#     index=obiecte_lista.index(obiect_cautat)
#     print(5*(index+1))

numbers = input("Numerele")
list_numbers = numbers.split(",")
i = 1
for number in list_numbers:

    for j in range(i, len(list_numbers)-1):
        if list_numbers[j] == number:
            list_numbers.remove(number)
    i += 1

print(list_numbers)