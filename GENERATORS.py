# generators: are  functions that return  traversable objects
#           -   produce  items one at a time and only  when required
#           - are run along with  "for" loops
'''
1. easy to implement(implement_iter_()._next_()automatically)
2.better memory management and utilization
3.can be used to  produce  infinite items
4. can also be used to pipeline  a number of operations

#difference between  normal functions and  generator functions
gen- make  use of "yield" keyword
norm - make use of "return" key word

gen - run when "next()" method is called
norm -  run when  name of the method is called

gen - produce items  one at a time and only when required
norm - produce all the items at once
'''

# generators created  using the  "def"  keyword make  use of yield keyword instead of return
def new(dict):
    for x,y in dict.items():
        yield x,y
a = {1:"hi", 2:"welcome"}
b  = new(a)
c = next(b)
print(c)
d = next(b)
print(d)

def myfunc(i):
    while i <= 3:
        yield  i
        i+=1
j = myfunc(2)
print(next(j))
print(next(j))

#generators with loops
#- to execute the generator function at once .iterates over
#  all  the objects  and after all implementations. it executes  stopiteration
def ex():
    n = 3
    yield n
    n = n*n
    yield n
v = ex()
for x in v:
     print(x)

def new():
    a = {1: "hi", 2: "welcome"}
    yield a
g = new()
for x in g:
 print(x)

#generator functions
#-resemble list  comprehessions and like  lambda functions
#generator expressions create anonymous generator functions

f = range(6)
print("list  comp" ,end=":")
q = [x+2 for x in f]
print(q)

print("gen exp",  end=":")
r = (x+2 for x in f)
print(r)

print("gen exp",  end=":")
r = (x+2 for x in f)
for x in r:
 print(x)

print("gen exp",  end=":")
r = (x+4 for x in f)
print(min(r))



