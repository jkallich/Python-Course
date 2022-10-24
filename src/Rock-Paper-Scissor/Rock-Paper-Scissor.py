import random
choices = ["rock", "paper", "scissor"]
print('Rock crushes scissor, scissor cuts paper, and paper covers rock.' +
      'Let the games BEGIN!!')
print()
prompt = "Do you want to be rock, paper, or scissor(or quit)? "
player_choice = input(prompt)
while player_choice != "quit":
    player_choice = player_choice.lower()
    computer_choice = random.choice(choices)
    print("You chose " + player_choice + ",and the computer chose " + computer_choice + ".")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock':
        if computer_choice == 'scissor':
            print("You win!")
        else:
            print("Computer wins!")
    elif player_choice == 'scissor':
        if computer_choice == 'paper':
            print("You win!")
        else:
            print("Computer wins!")
    elif player_choice == "paper":
        if computer_choice == 'rock':
            print('You win!')
        else:
            print("Computer wins!")
    else:
        print("I think there was some sort of error...")
        print()
        player_choice = input(prompt)
    break

