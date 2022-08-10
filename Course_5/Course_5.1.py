
# dictionaries

# my_dict = {
#     "name":"Razvan",
#     "age":28,
#     "city":"Arad"
# }

# print(my_dict)
#
# my_dict_2 = dict((("name","Razvan"), ("age", 28)))
# print(my_dict_2)
                                                   # ultima cheie este suprascrisa primei
# my_dict = {
#     "name":"Razvan",
#     "age":28,
#     "city":"Arad",
#     "age":30,
#     10: "Arad",
#     "house_number":28,
#     "my_info": {
#         "cnp": 1213,
#         "adresa":"Str."
#     }
# }
# print(my_dict["name"])
# print(my_dict.get(11))
#
# print("name" in my_dict)

# my_keys = my_dict.keys()
# my_values = my_dict.values()
# my_items = my_dict.items()
# print(my_items)
# print(my_keys)
# print(my_values)
#########################################################
# my_dict = {
#     "name":"Razvan",
#     "age":28,
#     "city":"Arad",
#     "age":30,
#     10: "Arad",
#     "house_number":28,
#     "my_info": {
#         "cnp": 1213,
#         "adresa":"Str."
#     }
# }
# my_dict["inaltime"] = 180
# print(my_dict)
# my_dict.update((("culoare_ochi", "Albastri"),))
# print(my_dict)

# my_dict["house_number"] = 100                            # se adauga elemente sau updateaza
# print(my_dict)
# my_dict.update((("age", 20),("name", "Toma")))          # se adauga elemente sau updateaza
# print(my_dict)
#
# print(my_dict.pop("age"))                                 # pentru eliminarea unei chei
# print(my_dict)
#
# print(my_dict.pop("test", 0))
# print(my_dict)

# popitem() elimina ultimul element inserat:
# print(my_dict.popitem())
# print(my_dict)

# Nested dictionaries:
# mom_dict = {"name": "Monica"}
# mom = "mom"
# family = {
#     "dad": {
#         "name": "Stefan"
#     },
#     mom: mom_dict
#
# }
# print(family)

my_dict = {
    "name":"Razvan",
    "age":28,
    "city":"Arad",
    "age":30,
    10: "Arad",
    "house_number":28,
    "my_info": {
        "cnp": 1213,
        "adresa":"Str."
    }
}

my_dict.setdefault("age", 31)
print(my_dict.setdefault("age1", 25))
print(my_dict)