import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    print(f"is '{username}' your username? ")
    new_username = input("Enter 'n' to type your own username or enter 'y' if it is yours ")
    if new_username == 'y':
            print(f"Welcome back, {username}!")
    elif new_username == 'n':
        #print(f"We'll remember you when you come back, {username}!")
        username = get_new_username()
        print(f"your user name have been updated {username}")
        print(f"Welcome back, {username}!")
    else:
        print("make sure you type in 'y/n'\n")

greet_user()


























