"""
Extended iterable unpacking is a tailor-made for unpacking iterables of unknown or arbitrary length. oftentimes,
these iterableshave some known component or pattern in their construction(e.g. "everything after element 1 is a
a phone number"), and star unpacking lets the developer lets the developer leverage those patterns easily
instead of performing acrobatics to get the relevant elements in the iterable.

it is worth noting that the star syntax can be especially useful when iterating over a squence of tuples of
varying length.A sequence of tagged tuples:
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo',3, 4),
    ]
def do_foo(x,y):
    print('foo', x, y)
    def do_bar(s):
        print('bar', s)
        for tag, *args in records:
            if tags == 'foo':
                do_foo(*args)
                if tag == 'bar':
                    do_bar(*args)
"""
Star unpacking can also be useful when combined with certain kinds of string processing operations, such as
splitting
"""
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print (uname)
print(fields)
print(homedir)
print(sh)
print()
print()

"""
Sometimes you might want to unpack values and throw them away. You can't just specify a bare * when unpacking,
but you could use a common use a common throwaway variable name, such as _origin(ignored).
"""
record = ('Esther', '23', 123.45, (3, 4, 2023))
name, *_, (*_, year)=record
print ("My name is: ",name)
print ("year: ", year)
print()
print()

"""
There is a certain similarity between star unpacking and list-processing features of various functional
languages. For example, if you have a list, you can easily split it into head and tail components
"""
items = [1, 10, 7, 4, 5, 9]
head, *tail=items
print("Head:",head)
print("Tail:",tail)
print()
print()

"""
One could imagine writing function that perform such splitting in order to carry out some kind of clever
recursive algorithm.
"""
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print("Sum = ", sum(items))
print()
#Recursion isn't a strong python feature due to the inherent recursion limit.

#Keeping the last N items
"""
problem
You want to keep a limited history of the last few items seen during iteration or during some other kind of
processing.

solution
keeping a limited history is a perfect use for a collection .deque. The following code performs a simple text
match on a sequence of lines and yields the matching line along with the previous N lines of context when found:
"""
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
if __name__ == '__main__':
    with open('p.txt') as f:
        for previous_lines in search(f, 'python', 5):
            for pline in previous_lines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
print()
print()
"""
When writing code to search for items, it is common to use a generator function involving yield. This decouples
the process of searching from the code that uses the results.

Using deque(maxlen= N)creates a fixed-sized queue. When new items are added and the queue is full, the oldest
item is automatically removed.
"""
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
print()
"""
Although the operation can be performed manually on a list(eg appending, deleting, etc), deque solution is far
more elegant and runs alot faster.
A deque can be used whenever you need a simple queue structure. If you don't give it a maximum size, you get an
unbounded queue that lets you append and pop items on either end.
"""
q = deque()
q.append(1)
q.append(2)
q.append(3)
print (q)
q.appendleft(4)
print(q)
print(q.pop())
print(q)
print(q.popleft())
"""
Adding or popping items from either end of a queue has O(1)complexity. this is unlike where inserting or
removing items from the front pf the list is O(N).
"""
print()

# Finding the largest or smallest N items
"""
Problem
Make a list of the largest or smallest N items in a collection
Solution
The heapq module has two functions-nlargest() and nsmallest() -that do exactly what we want.
"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3,nums))
print()
#both functions also accepts a key parameter that allows them to be used with more complicaated data structures
portfolio = [
    {'name' : 'IBM', 'shares' : 100, 'price' : 91.1},
    {'name' : 'AAPL', 'shares' : 50, 'price' : 543.22},
    {'name' : 'FB', 'shares' : 200, 'price' : 21.09},
    {'name' : 'HPQ', 'shares' : 35, 'price' : 31.75},
    {'name' : 'YHOO', 'shares' : 45, 'price' : 16.35},
    {'name' : 'ACME', 'shares' : 75, 'price' :115.65}
    ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print("cheap: ",cheap)
print()
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print("expensive: ",cheap)
print()
"""
If you are looking for the N smallest or largest items and N is small compared to the overall size of the
collection, these functions provide superior performance. Underneath the covers, they work by first converting
the data into a list where items are ordered as a heap.
"""
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
'''
The most important feature of a heap is that heap[0] is always the smallest item. Subsequent itms can be easily
found using the heapq.heappop() method, which pops off the first item and replaces it with the next smallest
item ( an operation that requires O(logN) operations where N is the size of the heap). To find the three
smallest items
'''
print("The first smallest number: ", heapq.heappop(heap))
print("The second smallest number: ",heapq.heappop(heap))
print("The third smallest number: ",heapq.heappop(heap))
"""
The nlargest() and nsmallest() functions are most appropriate if you are trying to find a relatively small
number of items. If you are simply trying to find the single smallest or largest item (N=1), It is faster to
use min() and max(). Similarly, If N is about the same size as the collection itself, it is ususlly faster to
sort it first and take a slice (i.e. use sorted(items)[:N] or sorted(items)[-N:]).It should be noted that the
actual implementation of nlargest() and nsmallest() is adaptive in how it operates and will carry out some of
these optimizations on your behalf (e.g., using sorting if N is close to the same size as the input).
Although it's not necessary to use this recipe, the implementation of a heap is an interesting and worthwhile
subject of study. this can usually be found in any decent book on algorithms and data structures. the
documentation for the heapq module also discusses the underlying implemntation details.
"""

