import random

def run_game():
    """Simple Rock-Paper-Scissors Game"""
    while True:
        print("\nType 'r' for Rock, 'p' for Paper, or 's' for Scissors")
        player = input("Your choice: ").lower()

        # Generate a random choice for computer
        options = ['r', 'p', 's']
        computer = random.choice(options)

        # Display both choices
        print(f"You chose {player}, Computer chose {computer}")

        # Check for tie
        if player == computer:
            print("It's a tie!")

        # Winning conditions
        elif (player == 'r' and computer == 's') or \
             (player == 's' and computer == 'p') or \
             (player == 'p' and computer == 'r'):
            print("🎉 You won!")

        # Losing condition
        else:
            print("💀 You lost!")

        # Ask if player wants to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break

# Run the game
run_game()
