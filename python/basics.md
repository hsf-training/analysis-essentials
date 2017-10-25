# Python basics

In these lessons, we’ll walk through the fundamentals of the Python programming 
langauge. These includes its syntax (how you express your problem in terms of 
code), and its data structures (what containers are available for you to store 
your values in).


## Strings

Strings are

## Core types/objects

* Numbers with `int` and `float`
  * Show that they are functions, i.e. `a = int()` and `b = float()`
  * Demonstrate arithmetic `+`, `-`, `/`, and `*`
  * Show pitfalls of integer division, e.g. `11/3` and how to avoid it (11./3 or float(11)/3 or `from __future__ import division`)
* Strings with `str`
  * Also a function, `a = str()`, but use shorthand syntax `a = ''` or `a =
    ""`
  * Can do all sorts with them: `len(a)`, `a*5`, `a.upper()`, `'Hello '+'World!'`
  * Formatting (inserting things in to strings) with `str.format`, e.g. `'Hello
    {0}! I am {1}, and you are still {0}'.format('Bob', 'Alice')` and `Pi to 2
    d.p.: {0:.2f}'.format( math.pi)`
  * Strings are immutable: any ‘change’ will create a copy: `a = 'hello'; b =
    a; b.upper(); print a; print b`
* Ordered collection with `list`
  * Also a function, `a = list()`, but use shorthand syntax `a = []`
  * They're not called ‘arrays’ as they can contain many different types
    (unlike a `std::vector` in C++, for example)
  * Create a simple list `a = [1, 6, 'hello', 4.5]`
  * Creation with list comprehension explained below
  * Indexing with `a[0]` and `a[-1]`
  * Slicing with `a[:2]`, `a[-1:]`
  * Mutation with `list.append`, `del a[0]`
  * Lists are mutable: `a = [1, 2, 3]; b = a; del b[0]; print a; print b`
  * Function `len`
* Tuples
  * Very similar to lists, but immutable after creation, so cannot e.g. add
    or remove elements
  * Also a function: `a = tuple()` (not very useful as it's a empty and
    immutable), but use shorthand `a = (1, 2)`
  * Usually used when the elements have some semantic meaning, e.g. for
    Cartesian coordinatesÂ one might use `x = 1; y = 2.5; coord = (x, y)`

    > **Challenge:**

    > Make a list, `a = [1, 2, 3]`, then copy it to the variable `b` by value so that when you change `a`, `b` stays the same.

    > _Hint:_ use slicing


## for/if and friends

* in python there are no curly braces or `begin` and `end` to separate code blocks. The only delimiter is a colon `:` and the indentation of the code.
* Indentation to use (4/8 spaces, tabs) is the same as long it is consistent (best practice is to use 4 spaces)
* example `if` (then, else, elif)
  * oneline if: `spam = 1 if answer==42 else 0`

* example 'while'
* example `for`
    * with `list`
        * Iteration with `for item in list:`
    * with `dict` (aka on list keys)
    * with `dict.items()`
    * with `range` (a list like any other)
    * `break` and `continue`
    * with `xrange` (is an iterator, does not have to compute all the list before making the loop, useful for loops over lot of events but that can exit before the end of the loop)
    * `zip` and `enumerate`

## list comprehension
* Imagine you want to make a list with the squares of the first 5 integers. A way to do it is

```python
ll = []
for i in range(5):
  ll.append(i**2)
```

But it is 3 lines, and in your life you would do it often so in python there is a nice syntax do do it in one lines

```python
ll = [i**2 for i in range(5)]
```

You can also do more complex things as:
```python
ll = [i**2 for i in range(5) if i%2==0]
```

> **Challenge:**

> Use a list to save the 3 coordinates of a vector. Make 2 vectors and then use list comprehension and `zip` to make the sum vector


## Core types/objects 2: dictionaries:  
* Dictionaries/maps with `dict`
  * Define them, as they are not as intuitive as `str` and `list`: they are
    lists indexed by ‘keys’ which don't have to be integers
    (and are more-often-than-not strings), must be `immutables` (So tuples ok lists not ok!)
  * Also a function: `a = dict()`, `b = dict(hello=[1, 4, 3], abc=4)`, but
    can use syntax `c = {'hello': [1, 4, 3], 'abc': 4}`
  * Accessing with `a['hello']`
  * Assignment with `a['hello'] = 'something completely different'`,
    `a['bar'] = 2`
  * Error if want to access key that is not there, can use `get` in that case and also set a default
  * Query contents with `key in d` (this returns a boolean)
      * Now show that this works in an identical manner for strings and
        lists, e.g. `'lo' in 'hello there'`, `1 in [4, 8, 1, 1]`
  * Can query content also with `d.has_key(key)`
  * Iteration over keys with `for key in d`, iteration over keys and values
    simultaneously with `for key, value in d.items(): print key, value`
  * Dictionaries are mutable: `a = dict(foo=4, bar=[3, 3]); b = a; del
    b['b']; print a; print b`
  * They are not ordered, iteration will probably not be the same as the
    definition order

    > **Challenge:**

    > make a dictionary {0: a, 1: b, ...} starting from the string 'abcdefghijklmnopqrstuvwxyz'

    > Then starting from that dictionary make another dictionary inverting keys and values

## Import external modules
* `import math; math.sqrt(4)`
* `from math import sqrt; sqrt(4)`
* `import math as mm; mm.sqrt(4)`
* `from math import *; sqrt(4)` Avoid as long as possible: risk to overwrite variables!


## Numpy
[numpy](http://www.numpy.org/) is a cool library that among may things offers a
powerful N-dimensional array object. Particularly handy to make computations
with vectors and matrices.
``` python
import numpy as np
a = np.array([1,2,3])
```
* operations +,-, ..., sqrt

    > **Challenge:**

    > Do again the game of summing two vectors but this time use numpy arrays

* Arrays of different shapes: `a = np.random.rand(3,4)`, `a.shape`, `len(a)`,
`a.size`
* Cool functions already implemented `sum`, `mean`, `std`, ...

    > **Challenge:**

    > Compute norm of vector sqrt of sum of squares of components in one line

## Other useful types
Other useful types like, for example, ordered dictionaries can be found in the module [collections](https://docs.python.org/2/library/collections.html)

## Scripts in python

* How to execute a script and exit (`python script.py`) and how to execute
  interactively (`(i)python -i script.py`). Show how a variable defined in a
  file can be used in the REPL
* How to do `./script.py` (i.e. add a hashbang `#!/usr/bin/env python` and
  `chmod +x script.py`)
* open python and import the script as a modules
* `if __name__ == '__main__'`


## Functions
  * Defined with `def my_func(): <body>`, conventionally named lower case with
    underscores
  * Function name acts like any other variable, can `print my_func` and even
    pass `my_func` to other functions
  * Arguments
    * Mandatory arguments specify no default `def my_func(var1, var2)`
    * Can cpass arguments based on their order or/and by name: `my_func(1, 2)`
    or `my_func(var1=1, var2=2)`
    but even `my_func(var1=2, var2=1)` or `my_func(2, var2=1)`
    * Optional arguments have default values: `def greeting(var1, var2=42)`
    * Example function to play:
    ```python
     def my_func(var1, var2 = 42):
         return var1 + var2
    ```
    * Functions can take functions as variables:
    ``` python
    def one_number(ll, func=mean):
      return func(ll)
    ```

    * Functions can return other functions!

   > Challenge: what does this do?
    ```python
    def make_incrementator(increment):
        def func(var):
            return var+increment
        return func
    increment_one = make_incrementator(1)
    increment_two = make_incrementator(1)
    print increment_one(42), increment_two(42)
    # But also
    print make_incrementator(3)(42)
    ```
    This knowledges helps understand LoKi functors later.

    * You can also have inline definition of functions:
    ` g = lambda x: x+1; g(42)`
    * You can use lambdas anywhere you need a function, handy especially
    if you need a function just once
    ``` python
    myList = [(2,7),(6,3),(5,2),(8,9),(3,1)]
    def last(ll):
      return ll[-1]
    sorted(myList, key=last)
    sorted(myList,key=lambda x: x[-1])
    ```

    * `argv` and `**argk` both in passing variables to a function and in defining
    function

    > **Challenge:**

    > Make a function that takes a undefined number of positional arguments and then print
    each one in a new lines

    > Make a function that take as first argument a function, as further arguments
    the arguments of the function and then print the output of that function
    ``` python
    def printOutput(func,*argv, **akgk):
      print 'The output is:', func(*argv, **akgk)
      printOutput(sorted, [(2,5),(6,3),(4,8)], key=lambda x: x[-1])
    ```


## Objects
  * Defined by _classes_, which are blueprints for creating _instances_ of
    objects: a class is a function that returns a new instance of an object.
`list` returns a new list object for example
  * Objects are, in many ways, containers. They hold instance _properties_
    and _methods_ (functions):


 ```python

    class Vector(object):
        def __init__(self, x, y, z):
            """
            Create a new vector.

            The first argument, self, is a variable holding the instance that
            will been created. You don't need to pass this first argument.
            """
            # We will create a property on this object called `name`
            self.x = x
            self.y = y
            self.z = z

        def norm(self):
            """
            Return the norm of the vector

            Just like in `__init__`, self will be the instance of the
            class that 'receives' this method call, and does not need to
            be passed by the caller.
            """
            return math.sqrt(self.x**2 + self.y**2 + self.z**2)

        def __sum__(self, other):
          """
          Return the sum between two vectors, nice because il allows me to use
          the syntax v1+v2
          """
          return Vector(self.x+other.x,self.y+other.y,self.z+other.z)

      def __str__(self):
        """
        To have nice representation when I print (look also __repr__)
        """
        return '({0}, {1}, {2})'.format(self.x,self.y,self.z)


    v1 =Vector(1,2,3)
    v2 = Vector(3,4,5)
    print v1, v2, v1+v2
    # We don't need to pass 'self'!
    print alice.greet(bob)
    ```
  * Singletons: classes that remember the objects that have been created from
    them, only allowing a single instance to be created.
    Used in LHCb options files.

## Organisation

* Importing things from your files (import `greeting` from IPython)
* Grouping related files as modules (create a folder, move files in, create
  `__init__.py`, show `import thing from module_name` works in IPython)
* Writing scripts that accept arguments with the `argparse` module (advanced)

## Finding help

* Google your question, phrase it in a broad way e.g. `python divide two
  lists`
* StackOverflow has a very good Python community
* The official Python documentation is also good (partly accessible with `help`)
* List of modules that you may find useful in your programs:
  * `math`: functions like `math.sin` and constants like `math.e`
  * `os`: operating system functions like `os.mkdir` and `os.rename`
  * `tempfile`: create files and directories in a temporary location, like
    `/tmp`, e.g. `tempfile.mkdtemp`
  * `glob`: file name matching, like `ls folder/*.txt` with
    `glob.glob('folder/*.txt')`
  * `subprocess`: call shell commands with `subprocess.call(['ls', '-l', '-a'])`
  * `time`: getting the current time with `time.localtime().tm_hour`
  * `collections`: `collections.namedtuple` for compact, property-only
    classes, `collections.OrderedDict` for ordered dictionaries,
    `collections.defaultdict` for dictionaries that will create values when a
    previously undefined key is accessed, e.g. `d = collections.defaultdict(int);
    d['foo'] += 1; print d, d['foo'], d['bar']`

## Conventional coding

* ‘Pythonic code’ is code that follows the conventions of the wider Python
  community. It emphasises clean, readable code, with consistent formatting
  and useful comments
  * Be consistent in your coding and formatting style, consult PEP8 if you're
    unsure or to settle a dispute like 'lower_case_functions' vs
    'UpperCaseFunctions'
* `import this`
  * “There should be one-- and preferably only one --obvious way to do it”
  * If there isn't, you might be trying to come at a problem the wrong way
* Like having a feeling for how to solve an equation, and knowing when you're
  probably going down the wrong road, a programmer benefits immensely from
  having a good intuition, which comes from experience writing _and reading_
  code

[anaconda]: https://www.anaconda.com/download/
[ipython]: https://ipython.org/
