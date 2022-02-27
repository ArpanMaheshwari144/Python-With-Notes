import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
player_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    if _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n ")

    elif _input == "s" and _random == "w":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n ")

    elif _input == "w" and _random == "g":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        player_point = player_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > player_point:
    print("Computer wins and You loose")

if computer_point < player_point:
    print("You win and Computer loose")

print(f"Your point is {player_point} and Computer point is {computer_point}")