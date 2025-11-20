filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


#working with millions

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


#writing to an empty file

filename = 'program.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#in append mode

filename = 'program.txt'

with open(filename, 'a') as file_object:
    file_object.write("\tI love playin soccer.\n")
    file_object.write("I love cooking rice and beans.\n")
    file_object.write("I love scoring goals.\n")
    









