import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(int(input("Guess number between 1 to 10: ")))
        if guess>random_number:
            print("Number is too high")
        elif guess<random_number:
            print("Number is too low")
    print("You've guessed correct number")
guess(10)

        
    
