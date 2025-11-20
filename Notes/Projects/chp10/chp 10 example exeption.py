#try:
#    print(6/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")
#this is the main code
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    if second_number == 'q':
#        break
#    answer = int(first_number) / int(second_number)
#    print(answer)
#will be modifying the code with the try and error block
#print("Give me two numbers, and I'll divide them.")
#print("Enter 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print('you cannot dive by zero!')
#    else:
#        print(answer)

#Analyzing text

#filename = 'reasons.txt'

#try:
#    with open(filename, encoding='utf-8') as f:
#        contents = f.read()
#except FileNotFoundError:
#    print(f"Sorry, the file {filename} does not exist.")
#else:
#    # Count the approximate number of words in the file.
#    words = contents.split()
#    num_words = len(words)
#    print(f"The file {filename} has about {num_words} words.")

#with out the try block
#with open(filename, encoding='utf-8') as f:
#        contents = f.read()

#words = contents.split()
#num_words = len(words)
#print(f"The file {filename} has about {num_words} words.")
#print(contents.split())

#created a function to keep the code so we can reuse any other time with any other file.
def count_words(filename):
    """Count the approximate number of wors in a file"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass #this tells python to fail silently
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#filename = 'pi_digits.txt'
#count_words(filename)
#now wemake a loop to give us the no of words by creating a list with the files there 
filenames = ['reasons.txt', 'guest.txt', 'program.txt', 'pi_digits.txt','more.txt']
for filename in filenames:
    count_words(filename)























































