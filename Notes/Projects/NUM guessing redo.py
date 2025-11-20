#import random

#print("Welcome to marsh guessing game")
#number = random.randint(0, 15)
#time = 0
#while time <= 5:
#    time += 1
#    guess = input("Enter your guess: ")

#    if guess.isalpha():
#        print("input a valid number")
#        continue
    
#    if guess == number:
#        print("Hurray you got it 'Bravo' ✌️✌️ ")
#        print(f"your guess: {guess}, computers guess: {number}")
#        print(f"it took you {time} times to get the right answer")
#        game = input("enter q to quit or y to continue ")
#        if game == 'y':
#            continue
#        elif game == 'q':
#            break
        
#    elif guess != number:
#        print("try again chad ❌\n")
#        if guess < number:
#            print("Number is too low")
#        elif guess > number and guess < 15:
#            print("Number is too high")
#        else:
#            print("Invalid number range")

#    print(f"Guess: {time}")

#    if time == 5:
        
#        print("you have exhausted all the guess, the lucky number is {number}")
#        break
    
#well structured

import random

def marsh_guessing_game():
    print("🎯 Welcome to Marsh Guessing Game!")
    
    while True:
        number = random.randint(0, 15)
        attempts = 0
        print("\nI've picked a number between 0 and 15. Can you guess it?")
        
        while attempts < 5:
            try:
                guess = int(input("👉 Enter your guess: "))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
                continue
            
            attempts += 1
            
            if guess == number:
                print(f"✅ Bravo! You guessed it in {attempts} tries.")
                print(f"Your guess: {guess}, Computer's number: {number}\n")
                break
            elif guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            
            print(f"Attempts left: {5 - attempts}")
        
        else:
            print(f"\n❌ You’ve used all 5 guesses! The correct number was {number}.\n")
        
        # Ask to play again
        play_again = input("Play again? (y/q): ").lower()
        if play_again == 'y':
            continue
        elif play_again == 'q':
            print("\n👋 Thanks for playing Marsh Guessing Game!")
            break
        else:
            print("⚠️ Invalid choice. Exiting game.")
            break

# Start the game
marsh_guessing_game()

