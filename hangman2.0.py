
import tkinter
import random

stop = False
person_1 = []


slova = ["zajo", "zvarac", "samo", "tomas", "adam"]

for pismeno in random.choice(slova):

    person_1.append(pismeno)



guess = ['*'] * len(person_1)

split_guess = ''.join(person_1)

x = -1

while len(guess) > x+1:
    
    x += 1



    print(f"\nHadaj slovo {guess}")
    guess_input = input("PISMENO: ")


    if split_guess == guess_input:

        print("uhadol si!")

        x = len(guess)+1

    elif guess_input is None or len(guess_input.strip()) == 0:

        guess[x] = person_1[x]


        print("neuhadol si!")


print(f'slovo bolo {person_1}')

