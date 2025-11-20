#using json dump() and load()

#json dump() to store data
#import json
#numbers = [2,3,5,7,11,13]

#filename = 'numbers.json'
#with open(filename, 'w') as f:
#    json.dump(numbers, f)

#json load() to load the stord data to memory

#import json
#filename = 'numbers.json'

#with open(filename) as f:
#    numbers = json.load(f)

#print(numbers)

#saving and reading usr_generaated Data

#import json

#username = input("What is your name? ")
#filename = 'username.json'

#with open(filename, 'w') as f:
#    json.dump(username, f)
#    print(f"We'll remember you when you come back, {username}!")


#program that greets user that name as been stored

#import json

#filename = 'username.json'
#   username = json.load(f)
#    print(f"\nHello {username}, welcome to Marsh Culture lad!")

#import json
 # Load the username, if it has been stored previously.
 #  Otherwise, prompt for the username and store it.
#filename = 'username.json'
#try:#this tell python to try and open a file
#    with open(filename) as f: # in the file object f 
#         username = json.load(f) # the content there was attributed to a variable username
#except FileNotFoundError: #if that file is not found then we can then prompt the user to request for his username and store it in the object file
#    username = input("What is your name? ") #the variable username holds the info that the user types
#    with open(filename, 'w') as f: #this tells python to open the file or create the file and store the info in the variable to that file
#        json.dump(username, f)#this takes the prompted info and stores it in the object f
#        print(f"We'll remember you when you come back, {username}!")# this print a statement using that info
#else:
#    print(f"Welcome back, {username}!")

#refractoring the code into 2 diff func one loads and the other prints the greeting 
#import json
#def get_stored_username():
#    """Get stored username if available."""
#    filename = 'username.json'
#    try:
#        with open(filename) as f:
#            username = json.load(f)
#    except FileNotFoundError:
#        return None
#    else:
#        return username

#def greet_user():
#    """Greet the user by name."""
#    username = get_stored_username()
#    if username:
#        print(f"Welcome back, {username}!")
#    else:
#        username = input("What is your name? ")
#        filename = 'username.json'
#        with open(filename, 'w') as f:
#            json.dump(username, f)
#            print(f"We'll remember you when you come back, {username}!")

#greet_user()

#this is the best refactoring form each function as a new task

import json
#funct1 gets a the stored username if there is in the file_object
def get_stored_username():
    """Get stored username if available."""
    filename = 'ame.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

#creates a username if the user is not available    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'ame.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()






















