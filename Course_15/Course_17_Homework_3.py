"""
Ai 2 prieteni ce vorbesc orca intre ei.Limba orca sunt aceleasi cuvinte
ca in limba romana doar ca se ia prima litera a fiecarui cuvant si se pune
la sfarsitul cuvantului in urma caruia se adauga un ay
drum = rumday
Input:
Un string ce reprezinta o propozite in limba romana
Output:
Un string ce reprezinta traducerea in limba orca
"""

propozitie_romana = input("Introduceti propozitia in romana pentru a fi tradusa in limba orca: ")

lista_cuvinte = propozitie_romana.split(" ")

propozitie_orca = ""
i = 1
for cuvant in lista_cuvinte:
    j = 1
    cuvant_orca = ""
    for litera in cuvant:
        if j == 1:
            cuvant_orca = cuvant.removeprefix(litera)

            if "." in cuvant:
                cuvant_orca = cuvant_orca.strip(".")

            cuvant_orca = cuvant_orca + litera

        j += 1
    if cuvant.istitle():
        propozitie_orca = propozitie_orca + cuvant_orca.title() + "ay" + " "
    else:
        propozitie_orca = propozitie_orca + cuvant_orca + "ay" + " "

    if "." in cuvant:
        propozitie_orca = propozitie_orca.strip() + "."

    i += 1

print(f"\nFraza tradusa in limba orca este:\n{propozitie_orca}")





