import random
from types import TracebackType


def game_win(comp , you):

    if(comp == you):
        return None

    elif(comp == "s"):
         if(you == "w"):
              return False
         elif(you == "g"):
               return True


    elif(comp == "w"):
         if(you == "g"):
             return False
         elif(you == "s"):
              return True

    elif(comp == "g"):
         if(you == "s"):
              return False
         elif(you == "w"):
              return True



print("comp turn : Snake(s) Water(w) or Gun(g)? ")
Rand_No =  random.randint(1 , 3)
if(Rand_No == 1):
     comp = "s"
elif(Rand_No == 2):
     comp = "w"
elif(Rand_No == 3):
     comp = "g"
              



    
you = input("your turn : Snake(s) Water(w) or Gun(g)? ")
a = game_win(comp , you)

print(f"Comp Choose {comp}")
print(f"You Choose {you}")

 
if(a == None):
     print("Game Tied..! :-|")
elif(a == True):
    print("You Win..! :-)")
elif(a == False):
     print("You Lose...!  :-(")