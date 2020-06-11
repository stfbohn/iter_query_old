import unittest
from iter_query import Qi
from collections import defaultdict



def yield_trace(trace):
    for i in 'MyExampleList':
        print('trace {}'.format(i))        
        trace[i]+= 1 
        yield i
        
trace = defaultdict(int)        
Qi(yield_trace(trace)).to_list()

trace = defaultdict(int)        
Qi(yield_trace(trace)).take(5).to_list()

trace = defaultdict(int)        
Qi(yield_trace(trace)).take(5).count()

trace = defaultdict(int)        
Qi(yield_trace(trace)).max()

'a'.upper()

trace = defaultdict(int)        
Qi(yield_trace(trace)) \
        .filter(lambda e: e==e.upper()) \
        .map(lambda e: e.lower()) \
        .to_list()

trace = defaultdict(int)        
Qi(yield_trace(trace)) \
        .map(lambda e: e.lower()) \
        .distinct() \
        .sort()

class Student:
    def __init__(self, name, age, major, level):
        self.name = name
        self.age = age
        self.major = major
        self.level =level
    def __str__(self):
        return '{} ({})'.format(self.name, self.age)
    def __repr__(self):
        return '{} ({})'.format(self.name, self.age)
        
students = [Student('Peter', 19, 'english', 13), 
            Student('Heidi', 23, 'English', 15), 
            Student('Karl',  20, 'History', 8 ), 
            Student('Lisa',  19, 'Physics', 18), 
            Student('Karl',  21, 'Physics', 9),   ]        
        

Qi(students).filter(lambda s: s.age >= 20)




l_test = lambda x: (x, x**x)
l_test(2)