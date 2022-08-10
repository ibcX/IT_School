
quantity = 20
fruit = "mere"
price = 40

text = "Vreau {} bucati de {} la pretul de {} RON"   # introducere variabile in text
print(text.format(quantity, fruit, price))

text_2 = "La pretul de {2} Ron, vreau sa cumpar {0} {1}"
print(text_2.format(quantity, fruit, price))
print("\n")

text_3 = f"Vreau {quantity} bucati de {fruit} la pretul de {price} RON"  # fstring pentru includere variabile in text intre acolade!
print(text_3)
print("\n")

text = "ana are mere"
print(text.capitalize())
text_4 = " ana are mere"
print(text_4.strip().capitalize())         # Metodele apelate la stringul initial nu modifica textul !
text_modificat = text_4.strip()
print(text_modificat)
print("\n")

text_5 = "RAzvan are mere"
print(text_5.upper())
print(text_5.lower())
