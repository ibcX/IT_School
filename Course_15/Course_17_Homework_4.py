
"""
In jungla:
Esti cu cortul in jungla singur si auzi niste animale in intuneric prin apropiere
Bazat pe sunet determina ce animale sunt
Task:
Ti se da sunetele facute de animalele din intuneric, evalueaza fiecare sunet
pentru a determina ce animal este:
Leii fac "Grr" , Tigri fac "Rawr", Serpii fac "Sss" iar pasarile fac "Cirip"

Input:
Un string ce reprezinta sunetele ce le auzi cu spatiu intre ele
Output:
Un string ce reprezinta animalele ce le auzi cu spatiu intre ele
(nota sunetele se pot repeta)

Ex:
Rawr Cirip Sss Sss
Tigru Pasare Sarpe Sarpe

"""

animale_jungla = {
    "Grr": "Leu",
    "Rawr": "Tigru",
    "Sss": "Sarpe",
    "Cirip": "Pasare"
}

sunete = input("Introduceti sunetele pe care le auziti: ")
lista_sunete = sunete.split(" ")

print("\nAnimalele pe care le auziti in jungla sunt: ")

for sunet in lista_sunete:
    if sunet in animale_jungla:
        print(animale_jungla[sunet], end=" ")
    else:
        print("Animal necunoscut", end=" ")
