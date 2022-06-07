from random import choice,randint

#Setting the environment for the game
print('-----------------------------------------------------------------------')
print()
print("---------    WELCOME TO ROCK,PAPER AND SCISSORS GAME PORTAL!    -------")
print()
print('-----------------------------------------------------------------------')


#receiving the preffered name for the player and generate a welcome message
player_name = input("\nEnter your game name:  ").title()
print('You are welcome,', player_name,)

#create a list for the available choice to be made
game_choice = ['R', 'P', 'S']
R = 'ROCK'
P = 'PAPER'
S = 'SCISSOR'

#create a user flow for human player in choice making
for user in range(3):
    human_choice = input("Choose 'R' for Rock, 'P' for Paper, 'S' for Scissor:  ").upper()
    if human_choice == 'R':
        print(player_name, 'your choice is ROCK')
    elif human_choice == 'P':
        print(player_name, 'your choice is PAPER')
    elif human_choice == 'S':
        print(player_name, 'your choice is SCISSOR')
    else:
        print('your choice:', human_choice, 'is Invalid')
        human_choice = input("Enter valid choice among 'R' for Rock, 'P' for Paper, 'S' for Scissor:  ").upper()
        if human_choice == 'R':
            print(player_name, 'your choice is ROCK')
        elif human_choice == 'P':
            print(player_name, 'your choice is PAPER')
        elif human_choice == 'S':
            print(player_name, 'your choice is SCISSOR')
        else:
            print('your choice:', human_choice, 'is Invalid')
            print('Game Over')
            break

#create a computer player named robot, and set its choice to random using choice

    robot_choice = choice(game_choice)

#create a user flow for human player in choice making
    if robot_choice == 'R':
        print("computer chose: is ROCK")
    elif robot_choice == 'P':
        print('computer chose: is PAPER')
    elif robot_choice == 'S':
        print('computer chose: SCISSOR')
    else:
        print('Error Detected')

#create a user flow for the game between human and computer

    if human_choice == robot_choice:
       print('It is a tie')
    elif human_choice  == 'R' and robot_choice == 'S':
       print(player_name, 'won')
       break
    elif human_choice  == 'P' and robot_choice == 'R':
       print(player_name, 'won')
       break
    elif human_choice  == 'S' and robot_choice == 'P':
       print(player_name, 'won')
       break
    else:
       print('computer won')
       break

print('-----------------------------------------------------------------------')
print()
print("---------    THANK YOU FOR PLAYING!    -------")
print()
print('-----------------------------------------------------------------------')



