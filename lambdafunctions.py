''' these are functions that do not have any name,also called anonymous or nameless functions
lambda is a keyword that specifies what follows if anonymous
#why are they used?
1)one time use - also known as throw away functions  as  they are needed just once, created wherever they are needed
2)I/O other functions - used with other functions , passed as inputs or returned as output
of other higher-order functions
3) reduce code size - the body of lambda functions is written in a single line'''

g =lambda a: a*a
print(g(3))
#comparing with
def func(n):
    return n*n
print(func(3))
#lambda is less code

#anonymous functions within  user defined functions
def steve(x):
    return (lambda y:x+y)
c = steve(3)
print(c(7))

def steve(x):
    return (lambda y:x+y)
c = steve(3)
print(c(7))
d= steve(6)
print(d(23))
#using lambda functions within filter(),map(),reduce()
'''filter()- used to filter  the given iterables(lists,sets,etc with the help
of another function passed as an argument to test all the elements to be true or false'''
mylist = [1,2,3,4,5,6,7]
newlist =list(filter(lambda a:(a/3 == 2),mylist))
print(newlist)

'''map() - applies a given  function to all iterables and returns  a new  list '''
mylist = [1,2,3,4,5,6,7]
p = list(map(lambda a:( a+3 ), mylist))
print(p)

'''reduce() - applies  some other function to a list of elements that are 
passed as a parameter to it  and finally returns a single value. `  '''
from functools import reduce
print(reduce(lambda a,b: a+b,[1,2,3,4,5]))

#solving algebric expression using lambda
s = lambda a: a*a
print(s(4))

#example2
s = lambda a,b:3*a + 4*b
print(s(2,3))
