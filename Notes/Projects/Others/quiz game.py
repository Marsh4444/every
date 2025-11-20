print('welcome to marsh quiz game do well to have fun!')

prompt = 'Do you wanna play the game? '
prompt += "\ntype 'no' if you want to quit "

game = input(prompt)

if game.lower() == 'yes':
    print('alright buddy lets go')
else:
    quit()

score = 0

answer = input('what does GO stands for? ')
if answer.lower() == "getting over":
    print('you are correct congratulations')
    score += 1
else:
    print('try again buddy you are incorrect')


answer = input('what does SO stands for? ')
if answer.lower() == "scoring over":
    print('you are correct congratulations')
    score += 1
else:
    print('try again buddy you are incorrect')

answer = input('what does FO stands for? ')
if answer.lower() == "falling over":
    print('you are correct congratulations')
    score += 1
else:
    print('try again buddy you are incorrect')

answer = input('what does PO stands for? ')
if answer.lower() == "puting over":
    print('you are correct congratulations')
    score += 1
else:
    print('try again buddy you are incorrect')

answer = input('what does NO stands for? ')
if answer.lower() == "not over":
    print('you are correct congratulations')
    score += 1
else:
    print('try again buddy you are incorrect')


print(f"you got {score} question correct")
print(f"you got {score/5 * 100}%")


