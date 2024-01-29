'''fancy decoraters- class decoraters , stateful decoraters, classes as decoraters
there are two ways to decorate a class in python,
firt one is where you can decorate a method inside a class and  there are built in methods like class,
stateful and property in python.'''
 #class and stateful methods define  methods inside a class  that is not connected to any other of the class
 #and property is  normally used to customize the getters and setters of a   class attribute

'''class Square:
    def __init__(self,side):
        self._side = side
    @property
    def side(self):
      return  self._side
    @side.setter
    def side(self,value):
       if value >= 0:
         self._side = value
       else:
          print("error")
    @property
    def area(self):
      return  self._side **2
    @classmethod
    def  unit_square(cls):
        return cls(1)
s = Square(5)
print(s.side)
print(s.area)'''

#singleton class

import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not  wrapper.instance:
         wrapper.instance = cls(*args, **kwargs)
        return  wrapper.instance
    wrapper.instance = None
    return wrapper
@singleton
class one:
    pass

first  =one()
second = one()

print(first is second)

#nested decoraters

import functools
def repeat (num):
    def decorater_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorater_repeat

@repeat(num =5)
def function(name):
    print(f'{name}')

function('mungai')

