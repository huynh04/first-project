import random as rd
def  play():
    user=input("'r' is rock, 'p' is paper, 's' is scissors: ")
    computer=rd.choice(["r", "p", "s"])
    print(f"Computer is {computer}")
    if user==computer:
        return "tie"
    if is_win(user, computer):
        return "You won!"

    return "You lost!"
  
          

def is_win(player, opponent):
    # s>p, p>r, r>s
    if (player == 'r' and opponent == 's') or (player == "s" and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True
      
print(play())
