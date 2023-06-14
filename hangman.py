
import tkinter
import random

stop = False
person_1 = []


slova = ["zajo", "zvarac", "samo", "tomas", "adam"]

for pismeno in random.choice(slova):

    person_1.append(pismeno)



guess = ['*'] * len(person_1)




while "*" in guess:
    
    x = False
    bad_letter = False


    print(f"\nHadaj slovo {guess}")
    guess_input = input("PISMENO: ")






    for i, letter in enumerate(person_1):


        if letter == guess_input:
            guess[i] = random.choice(person_1)
            x = True

        elif guess_input.isspace() or len(guess_input) == 0:
            guess[i] = random.choice(person_1)
            x = True
