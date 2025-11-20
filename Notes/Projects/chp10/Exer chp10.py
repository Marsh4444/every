#flename = 'learning_python.txt'

#Reading an entire file

with open('learning_python.txt') as file_object:
    summary = file_object.read()
print(f'\n{summary.upper()}')

#looping over the entire file object

summaryname = 'learning_python.txt '

with open(summaryname) as summary_object:
    for line in summary_object:
        print(line.rstrip())

#storing in a list

summaryname = 'learning_python.txt'

with open(summaryname) as summary_object:
    lines = summary_object.readlines()

for line in lines:
    print(line.rstrip())

#learning C

summaryname = 'learning_python.txt'


#with open(summaryname) as summary_object:
#    lines = summary_object.readlines()

#for line in lines:
#    print(line.rstrip().replace('journey','mission'))
#    #print(line.replace('journey','mission'))



#exer 10-3 Guest promting user ther name

#user_name = input('enter your name chad: ')

#username = 'guest.txt'
#with open(username, 'w') as file_object:
#    file_object.write(f'\nThis is your name {user_name}')

#10-4 Guest Book

#while True:
#    user_name = input('Enter your name: ')
#    print(f'\nWelcome {user_name}! \n')
#    with open(username, 'a') as file_object:
#        file_object.write(f'\n{user_name} Visted marsh culture\n')

#10-5 programming poll

reasons = 'reasons.txt'

while True:
    user_reason = input('Why Do you like programming: ')
    
    with open(reasons, 'a') as file_object:
        file_object.write(f"{user_reason}\n")












    
