import random


def checkiner(player, computer):
    if player == "Rock" and computer == "Scissors":
        return True
    elif player == "Paper" and computer == "Rock":
        return True
    elif player == "Scissors" and computer == "Paper":
        return True
    return False


def isTie(player, computer):
    if player == computer:
        return True


def validate(player_choice, available_choice):
    for i in range(len(available_choice)):
        if player_choice == available_choice[i]:
            return True
    return False


available_choice = ["Rock", "Paper", "Scissors"]


print("\t .:Miku's Rock Paper Scissors:.")
print("Enter choice:")
print("> ", end="")

player_choice = input()
# print("Player choose: ", player_choice)

valid_choice = False
valid_choice = validate(player_choice, available_choice)

# print("is player choice valid: ", valid_choice)

if valid_choice == False:
    while valid_choice == False:
        print("Oops! Try again!")
        print("Please enter Rock, Paper,  or Scissors")
        print("> ", end="")
        player_choice = ""
        player_choice = input()
        valid_choice = validate(player_choice, available_choice)

computer_choice = random.choice(available_choice)

print("Miku choose:", computer_choice)

if checkiner(player_choice, computer_choice):
    print("You won hacker...")

elif checkiner(player_choice, computer_choice) == False:
    if isTie(player_choice, computer_choice):
        print("Its a tie!")
    else:
        print("Miku win!! You lose!! :D")
