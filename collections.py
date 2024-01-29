
 #collections - container data types , there are four of them ,ie, dictionary, tuple,list,set
#specialised collections datatypes - namedtuple(),chainmap,deque,counter,orderedDict
#defaultdict,userdict,userlist,userstring

#namedtuple()-returns a tuple with a named value for each element in the tuple
'''from collections import  namedtuple
a = namedtuple('courses','name','technology')
s = a._make(['data science','python'])
assert isinstance(s, object)
print(s)

#deque pronounced as 'deck'is an optimised list to perform insertion deletion easily
from collections import deque
a = ['e''d''u''r''e''k''a']
d = deque(a)
print(d)
d.appendleft('python')
print(d)
d.popleft()
print(d)'''

'''chainmap is  a dictionary like class for creating a single view of 
multiple mappings,its like adding multiple  dictionary

from collections import Chainmap
a = (1:'edureka', 2:'python')
b = (3:"ml", 4 :"")
al = chainMap(a,b)
print(al)'''
'''counter is a dictionary subclass for counting hashable objects..

f '''

'''OrderedDict is a dictionary subclass which remembers the order in 
which the entries were done
from collections import OrderedDict
d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'

print(d)

'''
'''defaultdict is a dictionary subclass which calls a factory 
function to supply missing values
from collections import defaultdict
d =defaultdict(int)
d[1] = 'python'
d[2] ='edureka'

print(d[3])
a = {1:'python',2:"edureka"}
print(a[3])'''

'''UserDict is a wrapper around dictionary objects for easier
dictionary sub-classing'''
'''Userlist is a wrapper around list objects for easier list
 subclassing'''
'''Userstring is a wrapper around string objects for easier
string subclassing'''

