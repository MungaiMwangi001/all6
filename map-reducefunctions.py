'''map() - applies a given  function to all iterables and returns  a new  list '''
#map(func,iterables)
def new(a):
    return a*a
x = map(new,[1,2,3,4,5])
print(x)
print(list(x))

def new(a,b):
    return a*a, b*b
x = map(new,[1,2,3,4,5,9],[4,5,6,7,8,9])
print(x)
print(list(x))
#using lambda functions
mylist = [1,2,3,4,5,6,7]
p = list(map(lambda a:( a+3 ), mylist))
print(p)

 #using two lists
mylist1 = [1,2,3,4,5]
mylist2 = [4,5,6,7,8]
g =list(map(lambda a,b:(a*a,b*b),mylist1,mylist2 ))
print(g)

'''filter()- used to filter  the given iterables(lists,sets,etc with the help
of another function passed as an argument to test all the elements to be true or false'''
def new(i):
    if i >= 3:
        return i
j = filter(new,[1,2,3,4,5,6,7,9])
print(tuple(j))

#using lambda function

g =filter(lambda a:a<=3,[1,2,3,4,5,6,7,9])
print(list(g))

'''reduce() - applies  some other function to a list of elements that are 
passed as a parameter to it  and finally returns a single value. `  '''
from functools import reduce
def func(n,m):
    return  n+m

a = reduce(func,[11,12,13,14,15])
print(a)

from functools import reduce
g = reduce(lambda a,b:a*b,[11,12,13,14,15])
print(g)


#functions within functions
#filter within map
c=map(lambda a:a+a,filter(lambda a:a<=3,[1,2,3,4,5]))
print(list(c))

#map within filter
f = filter(lambda a:a>=12,map(lambda a: a+a,[1,2,3,4,5,6,7,8,9,10]))
print(list(f))

#map and filter witin reduce
d = reduce(lambda x,y:x+y,map(lambda x:x+x, filter(lambda x: x>=4,[4,5,6,7])))
print(d)
