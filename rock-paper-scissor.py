import random

def games():
    while(True):
        computer=random.choice(['r','p','s'])
        user=input("Enter r for rock,p for paper,s for scissor : ").lower()
    #r>s,s>p,p>r
    
        if (user==computer):
            print("tie")
        elif (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
            print("you won")
        elif (computer=='r' and user=='s') or (computer=='s' and user=='p') or (computer=='p' and user=='r'):
            print("you loss")
        else:
            print("Please enter either r,p,s")
    
games()  

