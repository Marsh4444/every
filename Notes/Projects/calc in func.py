#using function to create a calculator

def calculate(num1, operator, num2):

    while True:
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
        break

calculate(50, '-', 27)
