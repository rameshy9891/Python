import tkinter as tk
import random

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

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    return computer_choice, result

def update_score(result):
    if result == 'draw':
        scores['draws'] += 1
    elif result == 'user':
        scores['user_wins'] += 1
    else:
        scores['computer_wins'] += 1

def update_display():
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    result_label.config(text=f"Result: {result.capitalize()}")
    score_label.config(text=f"Score: You ({scores['user_wins']}) - Computer ({scores['computer_wins']}) - Draws ({scores['draws']})")

def on_rock():
    global user_choice, computer_choice, result
    user_choice = 'rock'
    computer_choice, result = play_game(user_choice)
    update_score(result)
    update_display()

def on_paper():
    global user_choice, computer_choice, result
    user_choice = 'paper'
    computer_choice, result = play_game(user_choice)
    update_score(result)
    update_display()

def on_scissors():
    global user_choice, computer_choice, result
    user_choice = 'scissors'
    computer_choice, result = play_game(user_choice)
    update_score(result)
    update_display()

def on_quit():
    root.destroy()

# Initialize the game
scores = {'user_wins': 0, 'computer_wins': 0, 'draws': 0}
user_choice = ''
computer_choice = ''
result = ''

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create widgets
user_choice_label = tk.Label(root, text="Your choice: ")
computer_choice_label = tk.Label(root, text="Computer's choice: ")
result_label = tk.Label(root, text="Result: ")
score_label = tk.Label(root, text="Score: You (0) - Computer (0) - Draws (0)")

rock_button = tk.Button(root, text="Rock", command=on_rock)
paper_button = tk.Button(root, text="Paper", command=on_paper)
scissors_button = tk.Button(root, text="Scissors", command=on_scissors)
quit_button = tk.Button(root, text="Quit", command=on_quit)

# Place widgets on the window
user_choice_label.pack()
computer_choice_label.pack()
result_label.pack()
score_label.pack()
rock_button.pack(side=tk.LEFT, padx=10, pady=5)
paper_button.pack(side=tk.LEFT, padx=10, pady=5)
scissors_button.pack(side=tk.LEFT, padx=10, pady=5)
quit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
