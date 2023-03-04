#Unpacking a sequence into separate variables
"""
problem
you have an N-element tuple or sequence that you would like to unpack into a collection of N variables

solution
any sequence (or iterable) can be unpacke into variable using a simple assignment operation. The only
requirement is that the number and structure match the sequence.
"""
p = (4, 5)
x, y = p
print (x)
print (y)
print()
print()


data = ['Esther', 50, 91.1, (2023, 3, 4)]
name, shares, price, date = data
print ("My name is : " ,name)
print ("My shares are : ",shares)
print("The price of the goods is : $",price)
print("Today's date : ", date)
print()
print()


data = ['Esther', 50, 91.1, ("year=2023", "month=03", "day=04")]
name, shares, price, date = data
print ("My name is : " ,name)
print ("My shares are : ",shares)
print("The price of the goods is : $",price)
print("The year : ", data)
print()
print()

"""
Discussion
unpacking actually works with any object that happens to be iterable, not just tuples or lists. This include
strings, files, iterators, anf generators.
"""
s = 'Esther'
a, b, c, d, e, f =s
print ("My name starts with letter:",a)
print ("Followed by letter:",b)
print ("Then letter:",c)
print ("And then letter:",d)
print ("Then letter:",e)
print ("Latly letter:",f)
print()
print()

"""
When upacking, you may sometimes want to discard certain values. python has no special synatax for this, but
you can often just pick a throwaway variable name for it.
"""
data = ['Esther', 50, 91.1, (2023, 3, 4)]
_, shares, price, _ = data
print ("My shares are : ",shares)
print("The price of the goods is : $",price)
#however, make sure that the variable name you picked isn't being used for something else already.
print()
print()


#Upacking Elements from Iterable of Arbitrary Length
"""
problem
You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too
many values to unpack" exception.

solution
Python "star expressions" can be used to address this problem. For example, suppose you run a course and decide
at the end of the semester that you're going to drop the firsr and last homework grades, and only average the
rest of them. if there are only four assignments, maybe you simply unpack all four, but what if there are 24?
A star expression makes it effective.
"""
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
print()
print()
"""
A another use case, suppose you have user records that consist of a name and email address, followed by an
arbitary number of phone numbers. The record can be upacked this way
"""
record = ('Esther', 'oomolara40@gmail.com', '09138053132', '07045386154')
name, email, *phone_numbers = record
print("My name is: ",name)
print("Email: ",email)
print("My phone_numbers are: ",phone_numbers)
"""
The phone_numbers variable will always be a list, regardless of how many phone numbers are unpacked (including
none). thus, any code that uses phone_numbers won't have to account for the possiblity that it might not be a
list or perform any kind of additional type checking.
"""
print()
print()

"""
the starred variable can also be the first one in the list. A sequence of values representing you company's
salesfigures for the last eight quarters. If you want to see the most recent quarter stacks up to the average
of the first seven, you could do something like this:
"""

def drop_most_recent_quarter(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return avg_comparison(trailing_avg,current_qtr)
    
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
trailings_avg = sum(trailing) / len(trailing)
print("The previous average: ",trailings_avg)
print("The previous number:",*trailing)
print("The most recent:",current)
print()
print()


