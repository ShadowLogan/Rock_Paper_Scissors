import random

comp_wins = 0
player_wins = 0



def choose_option():
    user_choice = input("Choose - Rock,Paper or Scissors?: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    else:
        print("I don't understand, try again!")
    choose_option()
    return user_choice
def computer_option():
    comp_choice == random.randint(1, 3)
    if comp_choice == 1:
        comp_choice == "r"
    elif comp_choice == 2:
        comp_choice == "s"
    else:
        comp_choice == "p"
    return comp_choice()


while True:
    print(" ")
    user_choice = choose_option()
    comp_choice = computer_option()
    print(" ")
    if user_choice == "r":
        if comp_choice == "r":
            print("It is a tie!")
        elif comp_choice == "s":
            print("You win rock smashes scissors!")
        elif comp_choice == "p":
            print("You lose paper covers rock!")
        if user_choice == "p":
            if comp_choice == "p":
                print("It is a tie!")
            elif comp_choice == "r":
                print("You win paper covers rock!")
            elif comp_choice == "r":
                print("You win scissors cut paper!")
                if user_choice == "s":
                    if comp_choice == "s":
                        print("It is a tie!")
                    elif comp_choice == "p":
                        print("You win scissors cut paper!")
                    elif comp_choice == "r":
                        print("You lose rock smashes scissors!")

while True:
    print("") + ("Player wins: " + str(player_wins))
    print("") + ("Computer wins: " + str(comp_wins))
    user_choice = input("Do you want to play again?: (y/n) ")
    if user_choice in ["Y", "y", "yes"]:
        pass
    if user_choice in ["N", "n", "no", "nah", "nope"]:
        break
    else:
        break
