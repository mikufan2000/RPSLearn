def validate(player_choice, available_choice):
    for i in range(len(available_choice)):
        if player_choice == available_choice[i]:
            return True
    return False


available_choice = ["Rock", "Paper", "Scissors"]


print("\t .:Rock Paper Scissors:.")
print("enter your choice")
print("> ", end="")

player_choice = input()
# print("Player choose: ", player_choice)

valid_choice = False
valid_choice = validate(player_choice, available_choice)

# print("is player choice valid: ", valid_choice)

if valid_choice == False:
    while valid_choice == False:
        print("invalid input asshole")
        print("Please enter Rock Paper or Scissors")
        print("> ", end="")
        player_choice = ""
        player_choice = input()
        valid_choice = validate(player_choice, available_choice)
