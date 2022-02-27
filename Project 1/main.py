import random

def game(player, computer):
    # If two values are equal, declare a tie!
    if computer == player:
        return None

    # Check for all possibilities when computer chose snake
    elif computer == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True

    # Check for all possibilities when computer chose water
    elif computer == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True

    # Check for all possibilities when computer chose gun
    elif computer == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True


print("Computer's Turn: Choose from Snake as (s), Water as (w) and Gun as (g) ")
randNo = random.randint(1,3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'

player = input("Your Turn: Choose from Snake as (s), Water as (w) and Gun as (g): ")

a = game(player, computer)

print(f"Computer Choose {computer}")
print(f"You Choose {player}")

if a == None:
    print("Game is Tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")