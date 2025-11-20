#json-- javascript object notation, a light weight data format that is used for data exchange.
#they are heavily used in web application.
#python already as a built in json module for encoding and decoding JSON data that makes working with json very easy.
#json data looks similar to a dictionary consist of several key value pairs and its value can take
#strings or numbers or booleans or also nested types like ,nested array or a nested dictionary

import json

#Some advantages of JSON: - JSON exists as a "sequence of bytes" which is very useful in the case we need to transmit (stream) data over a network.
#- Compared to XML, JSON is much smaller, translating into faster data transfers, and better experiences. - JSON is extremely human-friendly since
#it is textual, and simultaneously machine-friendly.

#JSON format¶

{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}

#JSON supports primitive types (strings, numbers, boolean), as well as nested arrays
#and objects. Simple Python objects are translated to JSON according to the following
#conversion:
#Primitive data types are predefined, lightweight, and essential for basic operations in
#any programming language. int , str ,char Single letters, digits, or symbols, bool
#Python	-----      | JSON
#dict	           | object
#list, tuple	   | array
#str	           | string
#int, long, float  | number
#True	           | true
#False	           | false
#None	           | null

#--------------------------------------------------------
#From Python to JSON (Serialization, Encode)

#Convert Python objects into a JSON string with the json.dumps() method.
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

#convert into json
person_json = json.dumps(person)
print(person_json)
#use different formatting style
#the separator is a tuple with 2 values
#used the sort key to sort it alphabetically
person_json2 = json.dumps(person, indent=4, separators=("; ","= "), sort_keys=True)
print(person_json2)

#lets convert it and dump it to a file save them into a file with the json.dump() method.
#with open('JSON.py', 'w') as f:
#    json.dump(json, f) #u can also specify indent etc

#FROM JSON to Python (Deserialization, Decode)¶
#Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary.

import json
person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)

#Or load data from a file and convert it to a Python object with the json.load() method.

import json

#with open('person.json', 'r') as f:
#    person = json.load(f)
#    print(person)

#Working with Custom Objects
#Encoding a custom object with the default JSONEncoder will raise a TypeError. We can specify a custom encoding function that
#will store the class name and all object variables in a dictionary. Use this function for the default argument in the
#json.dump() method.


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 20)

#specifing a custom encoding function
def encode_user(o):
    if isinstance(o, User):
        # just the key of the class name is important, the value can be arbitrary.        
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError(f"Object of type '{o.__class__.__name__}' is not JSON serializable")

userJSON = json.dumps(user, default=encode_user, indent=4)
print(userJSON)

#alternative method
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {o.__class__.__name__: True, "name":o.name, "age":o.age}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)

user = User("Max", 20)
userJSON = json.dumps(user, cls=UserEncoder, indent=4)
print(userJSON)
# or use encoder directly:
userJson = UserEncoder().encode(user)
print(userJSON)

#Decoding
#Decoding a custom object with the defaut JSONDecoder is possible, but it will be decoded into a dictionary. Write a custom decode function that will take a dictionary
#as input, and creates your custom object if it can find the object class name in the dictionary. Use this function for the object_hook argument in the json.load() method.

#possible but decoded as a dictionary

#if we want to decode this to a user object we need to write a custom decode message

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)





















































































































































































































































