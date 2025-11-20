#Lists: ordered, mutable, allows duplicate elements

#created a list
mylist = ['rice','mango','yam']
print(mylist)

#created an empty list
mylist2 = []
print(mylist2)

#changed the first item of the list
mylist[0] = 'food'

#printed the first item of the list
item = mylist[0]
print(item)

#iterate through a list
for _ in mylist:
    print(_)

#checking if an item is in a list
if 'mango' in mylist:
    print('available')
else:
    print('not available')

#methods in a list
#len() method checks how many element we have in a list
print(len(mylist))
#append() method use to add item to the list
mylist.append('fish')
print(mylist[3])
#insert() method used to insert object to a specific index
mylist.insert(1,'fruit')
print(mylist)
#pop() used to rmove item , returns our last object and also removes it
pep = mylist.pop()
print(pep)
print(mylist)
#remove() collects an item  and removes that item
item = mylist.remove('food')
print(mylist)

#clear() removes all element
#mylist.clear()
#reverse a list with reverse()
mylist.reverse()
print(mylist)
#sort the list with the sort method changes your list entirely 
mylist.sort()
print(mylist)
#sometimes its better to use the sorted() method

#tricks with list
mylist = [0] * 5 #creates a list with 5 zeros
print(mylist)
#concatenate list
mylist2 = [1,2,3,4,5,6]
new_list = mylist + mylist2
print(new_list)

#slicing a list

mylist = [1,2,3,4,5,6,7,8,9,0]
#a = mylist[::-1]nice trick to reverse your list
a = mylist[::2]#using the step to slice a list
print(a)

#copying a list
org_list = ['phone','house','lamp']

list1 = org_list#this gives exact copy of a list and whenevr the original list is modified the copy also gets modified
list1 = org_list.copy() #now this makes the difference
list1 = org_list[:]# slicing this also makes the diff
list1 = list(org_list)
list1.append('opol')
print(list1)
print(org_list)

#list comprehension
mylist = [1,2,3,4,5,6,7]
b = [a*a for a in mylist]
print(b)

#--------------------------------------------------------
# List comprehension
#A elegant and fast way to create a new list from an existing list.

#List comprehension consists of an expression followed by a for statement inside square brackets.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)

#[1, 4, 9, 16, 25, 36, 49, 64] <--- output




















































































































































































