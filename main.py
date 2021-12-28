import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
you = input("Press enter to start the game....")       
while you != 'Z':
    print("Computer's Turn: Snake(s) Water(w) or Gun(g)?")
    randNo = random.randint(1,3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'   

    you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
    a = gameWin(comp, you)
    
    if you != 'Z':
        if you == 's' or you == 'w' or you == 'g':
            print(f"Computer chose: {comp}")
            print(f"You chose: {you}")

            if a== None:
                print("The game is a tie!")
            elif a:
                print("You Win!")
            else:
                print("You Lose!")
        else:
            print("You chose the wrong character")
    else:
        print("Thank you for playing!")