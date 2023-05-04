# empty dict
d = {}

d = dict()  # same thing

d = {1: "one", 2: "two"}
print(d)

eng_to_spa = {  # english to spanish
    "hello": "hola", "yes": "sí",
    "dictionary": "diccionario", "one": "uno", "two": "dos",
    "no": "no"
}

print(eng_to_spa, len(eng_to_spa))
print(f"two in spanish is {eng_to_spa['two']}")
# print(eng_to_spa["three"]) would give error as it is not in the dictionary
eng_to_spa["three"] = "tres"  # this is how you add
eng_to_spa["two"] = "Dos"  # this is how you change a value

for i in eng_to_spa:
    print(i)  # you get the keys

print("Let me teach you Spanish")
for i in eng_to_spa:
    print(f"{i} is {eng_to_spa[i]}")  # this way you get keys and values