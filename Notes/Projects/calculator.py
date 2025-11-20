#simple CLI calculator

no_of_times = 0
print("\nwelcome, you can now calculate!\n")

while True:
    num1 = int(input('Enter the first number: '))

    operator = input('choose your operator "(+,-,*,/)" ')

    num2 = int(input('Enter the secound number: '))

    if operator == '+':
        result = (num1 + num2)
    elif operator == '-':
        result = (num1 - num2)
    elif operator == '*':
        result = (num1 * num2)

    elif operator == '/':
        try:
            result = (num1 / num2)
        except ZeroDivisionError:
            print('you cant divide by zero')
            continue


    print(f"The result is {result} ")

    ask = input("do you want to calculate again?(y/n) ").lower()

    no_of_times += 1
    
    if ask == 'y':
        continue
    else:
        print("\nThanks for using the calculator see you soon")
        print(f"you used the calc {no_of_times} times ")
        break
