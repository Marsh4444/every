#tuples: ordered, imutable, allows duplicate elements

#you can use the turple with a paranthesis of better still with out
mytuple1 = 'hope',
mytuple = 'orange',34,'green',5
print(type(mytuple))
print(type(mytuple1))

#you can covert a list to a tuple
mytuple2 = tuple(['face',20,'leg'])

#Accesing the item of a tuple
item = mytuple[0]
print(item)

#iterate ove a tuple
for _ in mytuple:
    print(_)

if 3 in mytuple:
    print('correct')
else:
    print('incorrect')
    
#methods to use with Tuples
print(len(mytuple1))#len() method
#counting element in a tuple
print(mytuple.count(5))
#finding the index of certain turple actually the first index
print(mytuple.index('green'))
#we get a value error for elements not in our tuple

#we can also convert a tuple to a list
mylist = list(mytuple) 
print(mylist)

#we can also convert a list back to a tuple
mytuple = tuple(mylist)
print(mytuple)

#slicing with tuple
mytuple1 = 1,2,3,4,5,6,7,8,9,10

b = mytuple1[2:5]
print(b)

#unpacking
my_tuple = 'Marsh',34,'green'
name, age, colour = my_tuple
print(name)
print(age)
print(colour)

mytuple1 = 1,2,3,4,5,6,7,8,9,10
l1, *l2, l3 = mytuple1
print(l1)
print(l3)
print(l2)






































































