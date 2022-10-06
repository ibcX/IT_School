
inaltime_cm = float(input("Introduceti inaltimea (cm): "))
greutate = float(input("Introduceti greutatea (kg): "))
inaltime_m = inaltime_cm / 100

bmi = greutate / (inaltime_m * inaltime_m)
print(f"BMI = {bmi}")

# underweight (bmi < 18.5), normal_weight: 18.5 - 24.9; overweight (bmi 25 - 29.9), obese (>30)

print(f"Underweight {bmi < 18.5}")
print(f"Normal weight {bmi>= 18.5 and bmi < 24.9}")
print(f"Overweight {bmi>= 25 and bmi < 29.9}")
print(f"Obese {bmi>= 30}")