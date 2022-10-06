
# Write a program that will tell if a dictionary is empty or not:

def empty_or_not (dict):
    if len(dict) == 0:
        print("Empty dictionary!")
    else:
        print("Dictionary not empty!")
dict_1 = {
    "name": "Bogdan",
    "sex": "male"
}
dict_2 = {

}
empty_or_not(dict_1)
empty_or_not(dict_2)
