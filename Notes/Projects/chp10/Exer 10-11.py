#import json

#favourite_number = input('whats your favourite number chad: ')
#filename = 'fave_num.json'

#with open(filename, 'w') as f:
#    json.dump(filename, f)
#    print(f'your fav number as been saved chad')


#import json

#favourite_number = input('whats your favourite number chad: ')
#filename = 'fave_num.json'

#with open(filename) as f:
#    favourite = json.load(f)
#    print(f"i know your favourite number its {favourite_number} ")

#using the try block to execute it

import json

filename = 'favnum.json'

try:
    with open(filename) as f:
        favourite = json.load(f)
except FileNotFoundError:
    print("sorry i dont think we have your favourite number our database\n")
    favourite = input('whats your favourite number chad: ')
    
    with open(filename, 'w') as f:
        json.dump(favourite, f)
        print(f'your fav number as been saved chad')
else:
    print(f"your favourite number is {favourite}!")




















