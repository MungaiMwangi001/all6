"""DECORATERS -in python are very powerful which modify  the behaviour  of a function
 without mdifying it permanently . it basically wraps another function and since
  both functions are callable, it returns a callable"""

def func1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to my humble abort")
    return  wrapper()

def function2():
    print('Moohngai')

function2 =func1(function2)

#or
'''def func1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to my humble abort")
    return  wrapper()
#add a syntax sugar
@func1
def function2():
    print("moohngai")
function2()'''

#more examples
# when using arguments
def function1(function):
     def wrapper(*args, **kwargs):
         print("hello")
         function(*args, **kwargs)
         print("welcome back. majiiiii")
     return wrapper

@function1
def function2( name):
    print(f"{name}")
function2("waseem")

# returns value from decorated function
def function(function1):
     def wrapper(*args, **kwargs):
         print("it worked")
     return  wrapper
@function
def function2(name):
     print(f"{name}")

function2("pythonzilla")


