#FUNCTIONS IN PYTHON AND ALSO DECORATERS
'''FIRST CLASS OBJECT- in python everything is treated  as an object
including all the data types. functions too .Therefore, a function
 is also known as a first class object and can be passed around as arguments
 INNER FUNCTIONS - it is possible to define functions inside a function
 that function is called a inner function'''

#first clas object

'''def func1(name):
    return f"hello {name}"

def func2(name):
     return f"{name} , how you doing?"

def func3(func4):
    return func4('dear learner')

print(func3(func1))
print(func3(func2 ))'''

#inner function
def func():
    print("first function")
    def func1():
        print("first child function")
    def func2():
            print("second child function")
    func1()
    func2()
func()


import functools
def repeat(num):
    def repeat_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for x in range(num):
                value = func(*args, **kwargs)
                return value
            return wrapper


        return repeat_deco

    @repeat(num=5)
    def function(name):
        print({name})
        function('python')


