import random

# Instructions
print("Welcome to Rock-Paper-Scissors!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.")

rock_picture='''
Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)


'''

paper_picture = '''
 Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)

'''

scissors_picture = '''

 Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)


'''

pictures=[rock_picture, paper_picture, scissors_picture]
# Possible choices
choices = ["rock", "paper", "scissors"]
# ascii.co.uk/art

# Game loop
while True:

    # Player's choice

    player_choice = input("Your choice (rock/paper/scissors): ").lower()
    if player_choice=="quit":
        break;
    index_player_choice=choices.index(player_choice)
    print(pictures[index_player_choice])
    
    # Check if the player wants to quit
    if player_choice == "quit":
        print("Thanks for playing! Goodbye!")
     

    # Validate player's input
    if player_choice not in choices:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")


    # Computer's random choice
    computer_choice = random.choice(choices)

    index_computer_choice=choices.index(computer_choice)
    print(pictures[index_computer_choice])
    # Print the choices
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
    (player_choice == "scissors" and computer_choice == "paper") or \
    (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
       print("Computer wins!")

    print("_______________________")  # Add a blank line for better readability