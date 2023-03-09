#Mapping keys to multiple values in a dictionary
"""
Problem
Make a dictionary that maps key to more than one value (a so-called "multidict")
Solution
A dictionary is a mapping where each key is mapped to a single value. If you want to map keys to multiple values,
you need to store the multiple values in another container such as a list or set.
"""
d = {
    'a' : [1, 2, 3],
    'b' : [4,5]
    }
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5},
    }
"""
The choice of whether or not to use lists or sets depends on intended use. Use a list if you want to preserve
the insertion order of the items. Use a set if you want to eliminate duplicates.
To easily construct such dictionaries, you can use defaultdict in the collections module. A feature of
defaultdict is that it automically initiates the first value so you can simply focus on adding items.
"""
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

"""
One caution with defaultdict is that it will automatically create dictionary entries for keys accessed later on
(even if they aren't current found in the dictionary). If you don't want this behaviour, you might use the
setdefault() on an ordinay dictionay instead.
"""
d ={} # A regular dictionay
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('a',[]).append(4)
"""
However, many programmers find setdefault() to be a little unnatural-not to mention the fact that it always
creates a new instance of the initial value on each invocation (the empty list [])

In principle, constructing a multivalued dictionary is simple. 
"""
pairs = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
#Using a defaultdict simply leads to much cleaner code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
    