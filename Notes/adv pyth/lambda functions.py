#this is a  small one line, anonymous  function thats defined without a name
#It as the lambda arguments: expression

#E.G
add10 = lambda x: x + 10
print(add10(5))

#this is practically the same as defining normal function

def add10(num):
    return num + 10

print(add10(10))

#wow actually EG1 and EG2 is the same thing. But the lambda function is more shorter and only in one line
#lambda function can also have multiple arguements
 
mult = lambda x,y: x*y
print(mult(3,4))

#lambda function is used when you need a simple function that is used
#only once in your code, or it is used as an argument to higher-order
#meaning functions that take in other functions as arguement
#E.g  they are used along with the built in functions, sorted, map,filter
#and reduce 
#lets sort according with index

point2D = [(1,2),(15,1),(5,-1),(10,4)]
#this list as a tuple , lets say its the x and y value of our points
point2D_sorted = sorted(point2D)
#the sorted function is built in so we dont need to import
print(point2D_sorted)
#we can specify a key
point2D_sorted = sorted(point2D, key=lambda x: x[1])
print(point2D_sorted)











































































































