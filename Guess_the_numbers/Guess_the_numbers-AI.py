import random as rd
def Games(x):
    numbers=rd.randint(1,x)
    guess=0
    print(f"Numbers will randow (1,{x})")
    while guess!=numbers:
        guess=int(input(f"Guess numbers 1 and 10: {guess}"))
        if guess>numbers:
            print(f"Sorry. Your number {numbers}.Too high")
        elif guess<numbers:
            print(f"Sorry. Your number {numbers}. Too low")
    print(f"Correct.Your numbers {numbers}")

def computer(x):
    low=1
    high=x
    feedback= ""
    while feedback!='c' :
        if low!=high:
            guess=rd.randint(low,high)
        else:
            guess=low    
        feedback=str(input(f"Is {guess} too high(H), too low(L) and correct(C)")).lower()
        if feedback=="h":
            high=guess
        elif feedback=='l':
            low=guess
    print(f"Correct, my numbers {guess}")

computer(100)