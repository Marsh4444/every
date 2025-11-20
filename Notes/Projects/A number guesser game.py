# This is a number guser game i did with the help of chatGbt this code took only five steps but we also modified it to an attempt of only 5 trials



import random   #Step1: Import random

lucky_number = random.randint(1, 30)#2. Generate a Random Number from 1 to 30

trials = 5 # set a variable trial to 5 indicating the number of attempts

#while True: we want limited number of tries thats why we removed the while loop and we are going to use a for loop.

for i in range(trials): #6. (Optional) Add Limited Attempts
     
    guess = input(f"Attempt {i + 1}: Enter your guess: ")#3. Ask the User for Input

    try:
        guess = int(guess) # checks and try to comfirm input to a number
    except ValueError:
        print("Please enter a valid number.")
        continue

 #4. Compare Guess with Secret Number used if for comparison
    
    if guess > lucky_number:
        print("number is too high ")
    elif guess == lucky_number:
        print("number is correct congratulations")
 #       break
    elif guess < lucky_number:
        print("number is too low")

else:
    print(f"you are out of attempts, the lucky number is: {lucky_number}.")# ends the for loop 
    










