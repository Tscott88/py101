import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['paper', 'spock'],
    'spock':    ['rock', 'scissors'],
}

SHORTHANDS_CHOICES = {
    'r':  'rock',
    'p':  'paper',
    'sc': 'scissors',
    'l':  'lizard',
    'sp': 'spock'
}

def prompt(msg):
    print(f"==> {msg}")

def display_winner(player, computer):
    prompt(f"you chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        prompt('You win this round!')
        return 'player'
    elif player == computer:
        prompt("This round is a tie!")
        return 'tie'
    else:
        prompt("Computer wins this one")
        return 'computer'

def player_wins(player_choice, computer):
    return computer in WINNING_COMBOS[player_choice]

while True:
    player_score = 0
    computer_score = 0
    prompt('Welcome to the RPSLS Challenge!')
    prompt("Best out of five will win the game.")

    while player_score < 3 and computer_score < 3:
        prompt(f"Choose one: (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock")
        choice = input()
        if choice in SHORTHANDS_CHOICES:
            choice = SHORTHANDS_CHOICES[choice]

        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice")
            choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        round_winner = display_winner(choice, computer_choice)

        if round_winner == 'player':
            player_score += 1
        elif round_winner == 'computer':
            computer_score += 1

        prompt(f"The score is You: {player_score} | Computer: {computer_score}")

    prompt(f"The final score is You: {player_score} | Computer: {computer_score}")
    if player_score == 3:
        prompt("Good Job! You are the winner \U0001F3C6")
    else:
        prompt("Better luck next time. You lose! \U0001F916")

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break