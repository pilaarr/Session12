import random

eng_to_spa = {  # english to spanish
    "hello": "hola", "yes": "sí",
    "dictionary": "diccionario", "one": "uno", "two": "dos",
    "no": "no"
}

del(eng_to_spa["hello"])  # delete the item
if "hello" in eng_to_spa:
    print("I know how to say hello in spanish")
else:
    print("I do not know how to say hello in spanish")

print(list(eng_to_spa.values()))  # get the values and convert into a list
print(list(eng_to_spa.keys()))  # get the keys

print(f"Word of the day: ", random.choice(list(eng_to_spa.values())))  # get a random item from the dict


# score = 0
# for i in range(10):
#     random_word = random.choice(list(eng_to_spa.keys()))
#     answer = input(f"How do you say {random_word} in Spanish? ")
#     if answer == eng_to_spa[random_word]:
#         print("Well done")
#         score += 1
#     else:
#         print(f"The correct answer was {eng_to_spa[random_word]}")
# print("Final score: ", score)

print(f"Horse is {eng_to_spa.get('horse', 'not defined')}")
# if 'horse' in eng_to_spa: ... else: not defined