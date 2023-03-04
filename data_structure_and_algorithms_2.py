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