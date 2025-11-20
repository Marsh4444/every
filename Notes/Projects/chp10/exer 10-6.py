#while True:

#    try:
#        number1 = int(input("Enter number 1: "))
#        number2 = int(input("Enter number 2: "))
#    except ValueError:
#        print("Enter a number please")

#    else:
#        result = number1 + number2
#        print(f'This is the result of the addition: {result}:')

#filename = "dogs.txt"

#try:
#    with open(filename, encoding='utf-8') as f:
#            contents = f.read()
#except FileNotFoundError:
#    pass
#    #print(f'THis file is not found, check the directory properly')
#else:
#    print(contents)

#words = contents.split()
#num_words = len(words)
filename = 'dogs.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    print(words.count('the'))
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

































