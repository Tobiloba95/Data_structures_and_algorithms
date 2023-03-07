#implementating a priority queue
"""
Problem
You want to implement a queue that sorts items by a given priority and always returns the item with the highest
priority on each pop operation.
Solution
The following class uses the heapq module to implement a simple priority queue:
"""
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q.pop())
#Output: Item('bar')
print(q.pop())
#Output: Item('spam')
print (q.pop())
#Output: Item('foo')
print (q.pop())
#Output: Item('grok')

"""
The core of this recipe concerns the use of the heapq module. The functions heapq. heap push() and heapq.heapp-
op insert and remove items from a list _queue in a way such that the first item in the list has the smallest
priority. the heappop() method always returns the "smallest" item, so that is the key to making the queue pop
the correct items. Moreover, since the push and pop operations have O(log N) complexity where N is the number
of items in the heap, they are fairly efficient even for fairly large values of N.

In this recipe, the queue consists of tuples of the form (-priority, index, item).the priority value is negated
to get the queue to sort items from highest priority to lowest priority. this is the opposite of the normal
heap ordering, which sort from lowest to highest value.

The role of the index variable is to properly order items with the same priority level. By keeping a constantly
increasing index, the items will be sorted according to the order in which they were inserted.However, the
index also serves an important role in making the comparison operations work for items that have the same
priority level. To elaborate instances of items can't be ordered:
"""
a = Item('foo')
b = Item('bar')
#print (a < b)
#Output: Traceback (most recent call last):
  #File "<pyshell>", line 1, in <module>
#TypeError: '<' not supported between instances of 'Item' and 'Item'
"""
If you make (priority, Item) tuples, they can be compared as long as the priorities are different. However, if
two tuples with equal priorities are compared, the comparison fails as before.
"""
a = (1, Item('foo'))
b = (5, Item('bar'))
print (a < b)
#output: True
c = (1, Item('grok'))
#print(a < c)
#Output: Traceback (most recent call last):
  #File "<pyshell>", line 1, in <module>
#TypeError: '<' not supported between instances of 'Item' and 'Item'
"""
By introducing the extra index and making(priority, index, item) tuples, you avoid this problem entirely since no
two tuples will ever have the same values for index (and Python never bothers to compare the remaining tuple values
once the result of comparison can be determined):

"""
a = (1, 0, Item('foo'))
b = (5, 1, Item ('bar'))
c = (1, 2, Item('grok'))
print("a < b: ",a < b)
#Output: True
print("a < c: ", a < c)
#Ouput: True
#If you want to use this queue for communication between threads, you need to add appropriate locking and signaling


