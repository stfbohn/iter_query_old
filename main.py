

class Qi: 

    def __init__(self, Iterable):
        self.data = Iterable
    def __iter__(self):
        return iter(self.data)
    def __reversed__(self):
        return self.data.__reversed__()

    def filter(self, condition): # or filter
        return Qi([e for e in self.data if condition(e)])
    def map(self, m):
        return Qi([m(e) for e in self.data])
    
    def to_list(self):
        return list(self)
    def to_set(self):
        return set(self)
    def to_dict(self, key_expr):
        return { key_expr(e):e for e in self }
    
    def count(self):
        return len(self.to_list())
    def first(self):
        return self.data.__iter__().__next__()
    def take(self, num):    
        it = self.data.__iter__()
        return Qi( (next(it) for i in range(num)) )
    def contains(self, e):
        return e in self.data
    
    def sum(self):
        return sum(self)
    def average(self):
        return self.sum()/self.count()
    
    def max(self, key=None, default=None):
        if key is None:
            return max(self)
        else: 
            return max(self, key=key) 
    def min(self, key=None, default=None):
        if key is None:
            return min(self)    
        else: 
            return min(self, key=key) 
        
    def distinct(self, key=None):
        def it():
            s = set()
            for e in self.data:
                k = e
                if key is not None:
                    k = key(e)
                if k in s:
                    continue
                s.add(k)
                yield e
        return Qi(it())
    
    def sort(self, key = None, reverse=False):
        return Qi(sorted(self, key=key, reverse=reverse))
    
# =============================================================================
#     TODO: think about this
# =============================================================================
    def reverse(self):
        return Qi(reversed(self))
    def last(self):
        return self.reverse().first().reverse()
    
    def groupby(self, expr):
        keys = self.map(expr).distinct().to_list()
        #print(keys)
        return Qi([ (k, Qi(self.data).filter(lambda e:expr(e) == k)) for k in keys ])
    def enumerate(self):
        return Qi(enumerate(self.data))
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        if self.count() > 5: 
            return '({}, ...)'.format(', '.join(self.take(4).map(lambda e:str(e))))
        else:
            return '({})'.format(', '.join(self.map(lambda e:str(e))))
            
    

