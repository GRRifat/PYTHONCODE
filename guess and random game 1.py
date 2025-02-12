import random

""" 
guessnum = int(input("Enter num 1 to 5: "))
randomnum = randint(1,5)

if guessnum == randomnum :
    print("WIN")
else :
    print("LOSE")

    print("Random Number: ",randomnum)
    """

op=["rock,paper,sijer"]

gus= input("Enter rock/paper/sijer: rock")
ran= random.choice(op)

if gus==ran:
    print(" Win")


else :
    print("Lose")
