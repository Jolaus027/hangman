import random

slova = ["zelene", "zvarac", "tomas", "jaro", "adam"]

slovo = random.choice(slova)

pokusy = len(slovo)

print(slovo)

pismenko = 0

while pokusy != 0:

    pokusy -= 1

    zadane_slovo = input("Hadaj slovo: ")

    if zadane_slovo != slovo:

        print("neuhadol si!")

        print(slovo[pismenko])
        pismenko += 1

    else:

        print("uhadol si!")

        pokusy = 0

