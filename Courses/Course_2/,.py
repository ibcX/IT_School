
nume = input("Introduceti numele pacientului: ")
prenume = input("Introduceti prenumele pacientului: ")
greutate = float(input("Introduceti greutatea pacientului (kg): "))
inaltime = int(input("Introduceti inaltimea pacientului (cm): "))
oras = input("Introduceti orasul: ")
observatii = input("Introduceti eventualele observatiile: ")

print()
print("*************************************************************")
print("*                                                                                                          *")
print("*                                   Fisa pacientului:                                                *")
print("*                                                                                                          *")
print("*************************************************************")

print(f"Pacient: {nume} {prenume}")
print(f"Greutatea: {greutate} kg")
print(f"Inaltimea: {inaltime} cm")
print(f"Orasul: {oras}")
print(f"Observatii: {observatii}")

print("*************************************************************")
