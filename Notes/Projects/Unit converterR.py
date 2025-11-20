#this code converts kg(Mass) to newton(weight) and newton to kg
#will code this normal ,then use a func and later use a class

print("---------------------Welcome-------------------------------\n")
print("Unit converter , converts mass to weight and weight to mass")

while True:
    askUser = input("\nConvert to Mass/Weight?\n\nEnter'm' for mass or 'w' for weight ").lower()
    if askUser == 'm':
        #while True:
        try:
            mass = int(input("Enter the Mass of the objet: "))
            prompt = input("Enter 'y' to continue the convertion to newton: ").lower()
            if prompt == 'y':
                result = mass/10
                print(f"\nThe Weight is {result}N")
                ask = input("Do you want to convert again?(y/n) ")
                if ask == 'y':
                    continue
                else:
                    break
                
        except ValueError:
            print("\n❌❌ please enter a valid number❌❌")
            continue
            
    elif askUser == 'w':
 #   while True:
        try:
            weight = float(input("Enter the weight of the objet: "))
            prompt = input("Enter 'y' to continue the convertion to kg: ").lower()
            if prompt == 'y':
                result = weight*10
                print(f"\nThe weight is {result}kg")
                ask = input("Do you want to convert again?(y/n) ")
                if ask == 'y':
                    continue
                else:
                    break        
        except ValueError:
            print("\n❌❌ please enter a valid number❌❌")
            continue
    else:
        print("Invalid input check very well")
