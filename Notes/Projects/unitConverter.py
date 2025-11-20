def unitConvert(unit = 'm', number = 0, newNum = None, newUnit = None):
    """Unit convertion program"""
    print("----------------Welcome---------------\nConvert Mass to Weight and vice versal")

    while True:
        try:
            #if the user want to chang the unit or number
            newValue = input("\nDo you want to change the unit?(y/n) ").lower()
            if newValue == 'y':
                newUnit = input("Mass or weight?(m/w) ").lower()
                if newUnit not in ['m', 'w']:
                    print("❌ invalid selection...Try again ")
                    continue
                unit = newUnit

                newNum = float(input("Enter a new value: "))
                number = newNum

            #Perform the conversion
            if unit == 'm':
                result = number * 10
                print(f"\nYour result ==> {result}Kg\n")

            elif unit == 'w':
                result = number / 10
                print(f"\nYour result ==> {result}N\n")

            else:
                print("❌ Enter a valid input\n")
                continue


            convertAgain = input("Want to convert again?(y/n): ")
            if convertAgain != 'y':
                break

        except ValueError:
            print("\n❌ Enter a vaid number\n")
            continue


if __name__ == '__main__':
    unitConvert()
