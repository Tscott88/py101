import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(msg):
    print(f"==> {msg}")

def display_winner(player, computer):
    prompt(f"you chose {player}, computer chose {computer}")

    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:

    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break