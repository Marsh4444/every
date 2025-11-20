prompt = "wlecome to Marsh Culure we are happy to see you here"
prompt += "\n\nBe sure to stay active here cos you will see massive changes soon in your life if you follow all our guides"

print(prompt)


while True:

    user_name = input("\nwhat is your name friend? ")
    user_name = user_name.title()
    
    if user_name.isdigit():
        print("enter a valid name")       
        continue        
        
    elif user_name != user_name.strip:
        print("enter a valid name")       
        continue  
#    elif user_name:
#        print("enter a valid name")       
#        continue
       
        
    

    else:
        print(f"\nwelcome to Marsh Culture {user_name}, lets tansform ourselves together!!!")       
        break

#if user_name != str(user_name):
#    print("make sure you enter a correct username")
#else:
#    print("\nsee your message below")

        














