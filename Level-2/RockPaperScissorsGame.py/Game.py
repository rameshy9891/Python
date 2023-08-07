import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors) or 'q' to quit: ").lower()
        if user_choice in ('rock', 'paper', 'scissors'):
            return user_choice
        elif user_choice == 'q':
            return 'q'
        print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'q'.")


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()

        if user_choice == 'q':
            print("Thank you for playing!")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == 'draw':
            print("It's a draw!")
            draws += 1
        elif result == 'user':
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Score: You ({user_wins}) - Computer ({computer_wins}) - Draws ({draws})")
        print()

if __name__ == "__main__":
    main()
