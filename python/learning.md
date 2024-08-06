# Learning more

Learning Python is like learning… well, like learning a language! You must 
practice reading and writing regularly, and as you do you’ll become more and 
more comfortable, starting to get a _feeling_ for how things work, and how to 
effectively express yourself.

Programming is a career in and of itself, so as physicists we have twice as 
much work to do! It takes people many years to get comfortable with any 
language, so try not to get too frustrated if things seem complicated at the 
beginning. It gets better!

When you do get stuck, ask friends and colleagues for help. One of the great 
things about Python is that many people around the world use it, and it’s very 
popular in high energy physics, so you likely already know someone who can help 
solve your problem. Working on code with others is a great way to learn, as you 
can see how other people do things, and find out tricks you didn’t know about.

Beyond other people, Google is a powerful ally. Knowing how to express your 
problem is important in getting the best answers quickly. Generally, including 
a few words as possible is a good idea, like [“python dictionary delete 
key”][search_dict], or [“python read file lines”][search_read].

[Stack Overflow][stackoverflow] is an excellent resource, with 
community-provided answers for many programming-related questions. Most 
problems you encounter will already be answered there, and often the answers 
are quite didactic, providing context and further reading, beyond just posting 
the code that answers the question (these answers aren’t always the ones marked 
as the ‘best answer’, and don’t always have the most votes).

## Exploring Python

The Python standard library is a treasure-trove of useful objects and methods. 
We’ve gone through a tiny subset of them here, some others that might be useful 
to you are:

* `os`: Operating system functions to manipulate and query your machine and the 
  file system, like `os.mkdir` to make directories and `os.rename`.
* `tempfile`: create files and directories in a temporary location, like
`/tmp`, e.g. `tempfile.mkdtemp`.
* `glob`: File name matching, to be able to do things like `ls folder/*.txt` in 
  Python with `glob.glob('folder/*.txt')`.
* `subprocess`: Call shell commands with `subprocess.call(['ls', '-l', '-a'])`.
* `time`: Get the current time with `time.localtime().tm_hour`.
* `collections`: Use `collections.namedtuple` to create your own property-only
objects.
```python
>>> import collections
>>> Coordinate = collections.namedtuple('Coordinate', ['x', 'y'])
>>> coord = Coordinate(4.5, 2.0)
>>> coord.y
2.0
>>> x, y = coord
>>> x
4.5
```
Use `collections.OrderedDict` for ordered dictionaries.
```python
>>> d = {'foo': 'bar', 123: 321, 'hero': 'thor'}
>>> for key, value in d.items():
...     print key, value
...
123 321
foo bar
hero thor
>>> d = collections.OrderedDict([('foo', 'bar'), (123, 321)])
>>> d.update([('hero', 'thor')])
>>> for key, value in d.items():
...     print(key, value)
...
foo bar
123 321
hero thor
```
`collections.defaultdict` is useful for creating dictionaries that will create 
automatically create values when a previously undefined key is accessed.
```python
>>> d = collections.defaultdict(int)
>>> d['foo'] += 1
>>> print(d, d['foo'], d['bar'])
defaultdict(<type 'int'>, {'foo': 1}) 1 0
```

[search_dict]: https://www.google.com/search?q=python+dictionary+delete+key
[search_read]: https://www.google.com/search?q=python+read+file+lines
[stackoverflow]: https://stackoverflow.com

## Conventional coding

‘Pythonic code’ is code that follows the conventions of the wider Python 
community. Lots of people write Python, and by following certain stylistic 
conventions it makes it easier for everyone to read each other’s code (as they 
say: ‘you spend 90% of your time reading code, and 10% writing it’).

Pythonic style emphasises clean, readable code, with consistent formatting and 
useful comments. The most important thing is to be consistent. You can consult 
[PEP8][pep8], the official Python style recommendations, if you're unsure or
want to settle a dispute like `lower_case_functions` versus 
`upperCaseFunctions`. Which of these two methods is easier to read?

```python
import time


def myFunc(x,y,verbose = True, fast='yes'):
    """Do the thing."""
    z=( x *y ) /2
    if verbose == False:
        print(x,y, z)
    if not fast:
        time.sleep( 1 )
    return  z* z


def my_func(x, y, verbose=True, fast=True):
    """Return ((x*y)/2)**2.

    Keyword arguments:
    x, y -- Values used in the computation
    verbose -- Print computation information
    fast -- If True, sleep for 1 second before returning
    """
    z = (x*y)/2

    if verbose:
        print(x, y, z)
    # Should probably remove this functionality
    if not fast:
        time.sleep(1)

    return z*z
```

The Zen of Python summarises the ‘philosophy’ that the language tries to 
follow. See what you think!

```python
>>> import this
```
> “There should be one-- and preferably only one --obvious way to do it”

If there isn't, you might be trying to come at a problem the wrong way.

[pep8]: https://www.python.org/dev/peps/pep-0008/
