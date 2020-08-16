import random

comp_score = 0
player_score = 0

game_list = ["Rock", "Paper", "Scissors"]

comp_choice = random.choice(game_list)
if comp_choice in ["Rock", "rock", "r", "R"]:
    comp_choice = "r"
if comp_choice in ["Scissors", "scissors", "s", "S"]:
    comp_choice = "s"
if comp_choice in ["Paper", "paper", "p", "P"]:
    comp_choice = "p"
print(comp_choice)

while True:
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    if player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "s"
    if player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"

    if player_choice == comp_choice:
        print("It is a draw!")

    if player_choice == "p":
        if comp_choice == "r":
            print("You chose Paper and the Computer chose rock. You win!")
            player_score += 1
        if comp_choice == "s":
            print("You chose Paper and the Computer chose scissors. You lose!")
            comp_score += 1

    if player_choice == "s":
        if comp_choice == "p":
            print("You chose Scissors and the Computer chose paper. You win!")
            player_score += 1
        if comp_choice == "r":
            print("You chose Scissors and the Computer chose rock. You lose!")
            comp_score += 1

    if player_choice == "r":
        if comp_choice == "s":
            print("You chose Rock and the Computer chose scissors. You win!")
            player_score += 1
        if comp_choice == "p":
            print("You chose Rock and the Computer chose Paper. You lose!")
            comp_score += 1

    print("Computer: " + str(comp_score) + " " + "Player: " + str(player_score))

    start = 1

    replay = input('Restart?  y/n:')

    if start != 1:
        print(replay)
    elif replay == 'y':
        pass
    elif replay == 'n':
        break
    else:
        print('Invalid input')
        continue
