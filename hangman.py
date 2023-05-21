import re
import tkinter


canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

uppercase_pattern = r'^[A-Z]+$'
non_letter_pattern = r'[^A-Za-z]'
stop = False
person_1 = []


while stop == False:

    person_1 = []
    error = False
    stop = False
    count = 0

    person_1_input = input("Zadaj slovo ktore sa bude hadat(Iba VELKE PISMENA): ")
    
    for i in person_1_input:
        count +=1

        if len(person_1_input) != count:

            if re.match(uppercase_pattern, i):

                person_1.append(i)

            else:

                error = True
                break

        elif len(person_1_input) == 1:

            if re.match(uppercase_pattern, i):

                person_1.append(i)
                stop = True

            else:

                error = True
                break

        else:

            stop = True
            person_1.append(i)
            print(len(person_1))
            print(count)
            break
            
    if error == True:

        print("Zle zadane slovo")




guess = ['*'] * len(person_1)
try_count = 10



while "*" in guess and try_count > 0:
    
    x = False
    bad_letter = False


    print(f"\nHadaj slovo {guess} | POCET PISMEN V SLOVE: {len(guess)} | POCET POKUSOV: {try_count}")
    guess_input = input("PISMENO: ")


    if guess_input.isspace() or len(guess_input) == 0:

        None

    elif guess_input in guess:

        print("toto pismeno si uz uhadol")
        x = True
    
    elif len(guess_input)>1:

        print("Zadaj len jedno pismeno!")
        x = True
    else:

        for i, letter in enumerate(person_1):
            

            if letter == guess_input:
                guess[i] = letter
                x = True

    if x == False:

        try_count -= 1
        print("zle pismeno")

    if bad_letter == True:

        try_count -=1
        print("zle pismeno")

    if try_count == 9:

        canvas.create_line (300, 500, 600, 500, width=3)

    elif try_count == 8:

        canvas.create_line (400, 500, 400, 190, width=3)

    elif try_count == 7:
        canvas.create_line (399, 190, 600, 190, width=3)

    elif try_count == 6:

        canvas.create_line (600, 250, 600, 190, width=3)

    elif try_count == 5:

        canvas.create_oval(575, 300,625, 250, width=3, tags="hlava")
        canvas.create_line(585, 285,615, 285, width=3, tags="hlava")
        canvas.create_line(585, 270,589, 270, width=3, tags="hlava")
        canvas.create_line(611, 270,615, 270, width=3, tags="hlava")

    elif try_count == 4:

        canvas.create_line (600, 300, 600, 380, width=3, tags="telo")

    elif try_count == 3:

        canvas.create_line(575, 330,600, 320, width=3, tags="telo")

    elif try_count == 2:

        canvas.create_line(600, 320,625, 330, width=3, tags="telo")

    elif try_count == 1:

        canvas.create_line(575, 405,600, 375, width=3, tags="telo")



if try_count <= 0:

    print("Nemas pokusy, prehral si!")
    canvas.create_line(600, 375,625, 405, width=3, tags="telo")

else:

    print(f"Super!!! Uhadol si slovo: {''.join(guess)}")

tkinter.mainloop()