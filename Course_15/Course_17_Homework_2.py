"""
Esti pe un vas de croaziera care ancoreaza langa o plaja superba.Exita o barcuta
mica ce va duce pasageri pe plaja.Te pui la rand .
Cat timp trebuie sa astepti stiind ca pe barcuta intra 20 de oameni iar un drum dureaza 10 minute.
Task:
Determina timpul de astptare daca stii numarul de persoane in fata ta
Input :
un numar intreg ce reprezinta numarul total de perosane aflate in fata ta
Output:
un numar intreg ce reprezinta numarul de minute ce trebuie sa astepti
ex:
Input:25
Ouptut:10
"""

while True:
    numar_persoane = input("Numarul persoanelor in fata: ")
    try:
        int(numar_persoane)
        break
    except:
        print("Introduceti un numar valid!")


numar_calatorii = int(numar_persoane)//20