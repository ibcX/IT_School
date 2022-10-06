
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car["model"])            # trebuie sa fie cheia respectiva in dictionar
print(car.get("colour"))
# print(car.setdefault("colour", "red")
car.update(
    (("colour", "red"),)
    )
# car["colour"] = "red"
print(car)
possible_colours = ["red", "blue", "black"]
car["colour"] = possible_colours
print(car)

print(car.setdefault("owner_name", "Razvan"))
print(car)
