users_weight = int(input("\nWeight: "))



convertion_lbs = int(users_weight * 0.5)
answer = input("K(g) or L(bs) k/l? ")
answer = answer.lower()

    
if answer == "k":
    print(f"\nthis is your answer in kilogram: {users_weight}")
elif answer == "l":
    print(f"\nThis is your answer in pounds: {convertion_lbs}")

else:
    print("make sure to type a number ")






