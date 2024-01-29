#fibonacci series-  A series  of numbers  where each number is
# also  called the fibonnaci  number  is the sum of the two preceding numbers
# eg - 0,1,1,2,3,5,8,13,21,34,55,89

def func():
    f,s = 0,1
    while True:
        yield f
        f,s=s,f+s
for x in func():
    if x>50:
        break
        print (x, end="\n ")

#number stream - any number from zero
a = range(10)
b = (x for  x in a)
print(b)
for y in b:
     print(y)
#odd number
a = range(1,20,2)
b = (x for  x in a)
print(b)
for y in b:
     print(y)

#even numbers
a = range(0,20,2)
b = (x for  x in a)
print(b)
for y in b:
     print(y)



