#from the python standard libary
#choice is one of a good choice of function out of random module
#it takes a list or tuple and returns a ramdom chosen element
from random import choice #from the random module import the choice function 

i = 1    #declared a variable i and assigned a value of 1 to it
attempts = 0
#trials = 4
print("\nYou could actuall make it big today if you guess right.")
print("\n\t'Wishing you all the best chad'")


while True:
    numbers = [1,2,3, 'a','b','c']
    attempts += 1
    i += 1
    #trials -= 1 
    first_choice = choice(numbers)

    print(f"\n\nChoose from the following numbers: {numbers}")
    guess = input("\nWHat do you think the next outcome will be: ")
    #if guess == first_choice:
    if guess != first_choice:
        print(f"The correct choice is: {first_choice}\n")
        continue
        #print("you got the guess correctly")
        #print(f"your choice is: {first_choice}, Attempt: {attempts}\n")
        #break

    #else:
        #if trials == 0:
         #   break
    if guess == first_choice:
       # print(f"You still have {trials} trials")
        print("you got the guess correctly")
        print(f"your choice is: {first_choice}, Attempt: {attempts}\n")
        break

    #             
    continue
print("You have exhausted your trials ")
print("\nopps you didnt get it right you can start the game all over")
    #i += 1
        
    
        


