#unorded and mutable consist of a collection value pairs

myDict = {
        'name':'Marsh', #always remeber to add that coma(,)
        'age':27,
        'country':'Nigeria'
        }
print(myDict)

#we can also create a dictionary by using the dict function
#to create a dictionary

myDict = dict(name='Marsh', age=27, country='Nigeria')
print(myDict)

#acccessing the values of a dictionary
value = myDict['name']
print(value)
value = myDict['age']
print(value)
value = myDict['country']
print(value)
help1 = help(myDict)
print(help1)

#DIctionary are mutable so we can add , change items on it etc

#adding item to the dictionary
myDict['email'] = "holyfield444@gmail.com"
print(myDict)

#deleting item in a dictionary
#2 common ways to do this is the del statement and also the pop() method
#del myDict['name']
#print(myDict)
myDict.pop('email')
print(myDict)
myDict.popitem() #the popitem() removes the last item of the dictionary.

#checking for a key in a dictionary
#2 common ways to do this
#1) Using the if in statement.
if "name" in myDict:
    print(myDict["name"])
#2) Using the try except statement.






































