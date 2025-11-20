prompt = "welcome to Marsh car game make sure to enjoy yourself"
prompt = "\n\ntype in 'yes' to start, 'no' to stop and 'q' to quit"

command = input('\n\n\ntype in "help" to see the list of commands: ')
print(prompt)

game = True
started = False
while game:
    
    game = input('\ntype in a comand to begin choose a comand from the instruction above: ').lower().strip()
    if game == 'yes':
        if started:
            print('game is already started')
        else:
            started = True
            print('game have started')
    elif game == 'no':
        if not started:
            print('game is already stopped')
        else:
            started = False
            print('game have stoped')
    elif game == 'q':
        print('you quit the game')
        break

    else:
        print('i dont understand what you mean type in a valid command')


