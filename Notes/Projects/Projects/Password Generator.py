"""
    A beginner project on password Generator 
"""
import random , string



#i defined a funtion
def password_generator():
    """Password generator"""
    
    #ask users for how long there password should be
    prompt = int(input("How long do you want your password to be 'should be a number': \n")) 
    
    #Join them together into a single string.
    password_combo = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(random.choice(password_combo) for _ in range(prompt))


print(password_generator())

















