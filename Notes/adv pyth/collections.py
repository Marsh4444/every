#This implements special container datatypes and provides alternatives with some additional
#functionalities compared to the general boots and containers like list and tuples

#we would be talking about 5 diff types of the collection datatypes
#Counter, namedtuple,OrderedDict, defaultdict,   degue

#lets start with the container:
#first we import it

#from collections import Counter
#the counter is a container that stores the element as dictionary keys and are counts as dictionary VAlues
 
#a = "aaaabbbnnndddfff" # we can use a list or any other iterable item
#myCounter = Counter(a)
#print(myCounter.values())
#print(myCounter.most_common(1))#this gives the most common element
#indexing makes it easier to access does index
#print(myCounter.most_common(2)[0][0])#this gives the 2 most common elements
#c = list(myCounter.elements())
 
#now lwts talk about the next collections namedtuple
#from collections import namedtuple
#the named tuple is an easy to create and light weight object type similar to a struct
#Point = namedtuple('Point','x,y') #defined our namedtuple it will create a class Point with the fields x and y
#pt = Point(1, -4)
#print(pt.x, pt.y)

#ordered dictionary
#they just like the ordinary dict but the remember the order in which the items wher put
#from collections import OrderedDict

#ordered_dict = {}#OrderedDict()
#ordered_dict['a'] = 1
#ordered_dict['b'] = 2
#ordered_dict['c'] = 3
#ordered_dict['d'] = 4

#print(ordered_dict)

#from collections import defaultdict
#This as a default value if the key as not been set yet. as similarities to a dict

#d = defaultdict(list)
#d['a'] = 1
#d['b'] = 2
#print(d['c'])

from collections import deque

#this is used to add and remove elements from both ends

d = deque()

d.append(1)
d.append(2)
d.append(3)

d.appendleft(3)
print(d)

d.popleft()
print(d)

#d.clear()
#print(d)

d.extendleft([4,5,6])
print(d)

#we can also rotate our deque
d.rotate(-2)
print(d)
















































































































