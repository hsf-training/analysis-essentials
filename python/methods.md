# Methods

Methods, also called functions, take some input and return some output. We have
already used lots of methods, like `dir`, `help`, and `len`, and in this lesson
we will start creating our own.

As we have seen, methods can do a lot of stuff with very little typing. Methods
are normally used to encapsulate small pieces of code that we want to reuse.

Let’s rewrite `len` as an example.

```python
>>> def length(obj):
...     """Return the number of elements in obj.
...
...     obj must be iterable.
...     """
...     i = 0
...     for _ in obj:
...         i += 1
...     return i
>>> length
<function length at 0x7f83b2bc56e0>
>>> help(length)
Help on function length in module __main__:

length(obj)
    Return the number of elements in obj.

    obj must be iterable.
>>> length('A b c!')
6
>>> length(range(5))
5
```

There’s a lot going on here, so we will break it down line-by-line.

1. `def length(obj)`: methods are _defined_ using `def`, followed by a space,
   and then the name you want to give the method.[^1] Inside the parentheses
   after the name, we list the inputs, or _arguments_, that we want our method
   to accept.  In this case, we only need a single input: the thing we want to
   compute the length of.  Finally, there’s a colon at the end, just like with
   a `for` or `if`, which means a _block_ of code follows (which must be
   indented).
2. `"""Return the number of elements in obj."""`: This is the _docstring_. It’s
   just a documentation string, defined literally with three double quotes so that we can
   include linebreaks. By placing a string here, Python makes the string
   available to use when we pass our function to `help`. Documenting your
   functions is a very good idea! It makes it clear to others, and to
   future-you, what the method is supposed to do.
3. The method block. This is the code that will run whenever you _call_ your
   method, like `length([1])`. The code in the block has access to the
   arguments and to any variables defined _before_ the method definition.
```python
>>> x = 1
>>> def top_function():
...    """Do something silly."""
...    print(x)
...    print(y)
...
>>> y = 2
>>> top_function()
1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in top_function
NameError: global name 'y' is not defined
```
  In general, you should try to minimise the number of variables outside your
  method that you use inside. It makes figuring out what the method does much
  harder, as you have to look elsewhere in the code to find things out.
4. `return i`: This defines the _output_ of the method, the thing that you get
   back when you call the method. You don’t have to return anything, in which
   case Python will implicitly make your function return `None`, or you can
   return multiple things at once.
```python
>>> def no_return():
...     1 + 1
...
>>> no_return()
>>> no_return() == None
>>> def such_output():
...     return 'wow', 'much clever', 213
...
>>> such_output()
('wow', 'much clever', 213)
>>> a, b, c = such_output()
>>> b
'much clever'
```
  You can see that returning multiple things implicitly means returning a
  tuple, so we can choose to assign one variable per value while calling the
  method.

[^1]: Names are conventionally in lowercase, with underscores separating words.

Methods can be called in several ways.

```python
>>> def add(x, y):
...    """Return the sum of x and y."""
...    return x + y
...
>>> add(1, 2)
>>> add(x=1, y=2)
>>> add(1, y=2)
>>> add(y=2, x=1)
>>> add(y=2, 1)
  File "<stdin>", line 1
SyntaxError: non-keyword arg after keyword arg
>>> add(y=2, =1)
  File "<stdin>", line 1
    add(y=2, =1)
             ^
SyntaxError: invalid syntax
```

Specifying the argument’s name explicitly when calling a method is nice because
it reminds you what the argument is supposed to do. It also means you don’t
have to remember the order in which the arguments were defined, you can specify
_keyword arguments_ in any order. You can even mix _positional arguments_ with
keyword arguments, but any keyword arguments must come last.

Using keyword arguments is particularly useful for arguments which act as
on/off flags, because it’s often not obvious what your `True` or `False` is
doing.

```python
>>> def add(x, y, show):
...    """Return the sum of x and y.
...
...    Optionally print the result before returning it.
...    """
...    if show:
...        print(x + y)
...    return x + y
...
>>> _ = add(1, 2, True) # Hmm, what is True doing again?
3
>>> _ = add(1, 2, show=True) # Aha! Much clearer
```

Always having to specify that flag is annoying. It would be much nicer if
`show` had a _default value_, so that we don’t _have_ to provide a value when
calling the method, but can optionally override it.

```python
>>> def add(x, y, show=False):
...    """Return the sum of x and y.
...
...    Optionally print the result before returning it.
...    """
...    if show:
...        print(x + y)
...    return x + y
...
>>> _ = add(1, 2) # No printing!
>>> _ = add(1, 2, show=True)
3
```

Perfect.

Of course, function arguments can be anything, even other functions!

```python
>>> def run_method(method, x):
...     """Call `method` with `x`."""
...     return method(x)
...
>>> run_method(len, [1, 2, 3])
3
```

{% challenge "Methods returning methods" %}

What does this method do?

```python
>>> def make_incrementor(increment):
...     def func(var):
...         return var + increment
...     return func
```

{% solution "Solution" %}

It returns a function whose `increment` value has been filled by the argument
to `make_incrementor`. If we called `make_incrementor(3)`, then `increment` has
the value 3, and we can fill in the returned method in our heads.

```python
def func(var):
    return var + 3
```

So when we call _this_ method, we’ll get back what we put in, but plus 3.

```python
>>> increment_one = make_incrementator(1)
>>> increment_two = make_incrementator(2)
>>> print increment_one(42), increment_two(42)
43 44
>>> print make_incrementator(3)(42) # Do it in one go!
45
```

{% endsolution %}

{% endchallenge %}

What if you like to accept an arbitrary number of arguments? For example, we
can also write a `total` method that takes two arguments.

```python
>>> def total(x, y):
...     """Return the sum of the arguments."""
...     return x + y
...
>>>
```

But what if we want to allow the caller to pass more than two arguments? It
would be tedious to define many arguments explicitly.

```python
>>> def total(*args):
...     """Return the sum of the arguments."""
...     # For seeing what `*` does
...     print('Got {0} arguments: {1}'.format(len(args), args))
...     return sum(args)
...
>>> total(1)
Got 1 arguments: (1,)
1
>>> total(1, 2)
Got 2 arguments: (1, 2)
3
>>> total(1, 2, 3)
Got 3 arguments: (1, 2, 3)
6
```

The `*args` syntax says “stuff any arguments into a tuple and call it `args`”.
This let’s us capture any number of arguments. As `args` is a tuple, one could
loop over it, access a specific element, and so on.

We can also _expand_ lists into separate arguments with the same syntax when
_calling_ a method.

```python
>>> def reverse_args(x, y):
...     return y, x
...
>>> l = ['a', 'b']
>>> reverse_args(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: reverse_args() takes exactly 2 arguments (1 given)
>>> reverse_args(*l)
('b', 'a')
```

A similar syntax exists for keyword arguments.

```python
>>> def ages(**people):
...     """Print people's information."""
...     # For seeing what `**` does
...     print('Got {0} arguments: {1}'.format(len(people), people))
...     for person in people:
...         print('Person {0} is {1}'.format(person, people[person]))
...
>>> ages(steve=31)
Got 1 arguments: {'steve': 31}
Person steve is 31
>>> ages(steve=31, helen=70, zorblax=9963)
Got 3 arguments: {'steve': 31, 'zorblax': 9963, 'helen': 70}
Person steve is 31
Person zorblax is 9963
Person helen is 70
```

As you can see from the debug print statement, `**people` is a dictionary
containing the keyword arguments we passed to the `ages` method. The keys of
the dictionary are the names of the argument as strings, and the values are the
values of the arguments. Just like for the `*` syntax, `**` can also be used to
expand a dictionary into keyword arguments.

```python
>>> d = {'thor': 5000, 'yoda': -1}
>>> ages(**d)
Got 2 arguments: {'yoda': -1, 'thor': 5000}
Person yoda is -1
Person thor is 5000
```

The order of the keyword arguments used to call the method are not necessarily
the same as those that the function block sees!
This is because dictionaries are unordered, and the `**` syntax effectively creates a dictionary.


{% challenge "The most generic method" %}

The most generic method would take any number of positional arguments _and_ any
number of keyword arguments. What would this method look like?

{% solution "Solution" %}

It would use both `*` and `**` syntax in defining the arguments.
```python
>>> def generic(*args, **kwargs):
...     print('Got args: {0}'.format(args))
...     print('Got kwargs: {0}'.format(kwargs))
...
>>> d = {'bing': 'baz'}
>>> generic(1, 2, 'abc', foo='bar', **d)
Got args: (1, 2, 'abc')
Got kwargs: {'bing': 'baz', 'foo': 'bar'}
```

{% endsolution %}

{% endchallenge %}

## Inline methods

Some methods take other methods as arguments, like the built-in `map` method.

```python
>>> map(str, range(5))
['0', '1', '2', '3', '4']
```

`map` takes a function and an iterable, and applies the function to each element in
the iterable. It returns a new list with the results. We can define and then pass
our own functions.

```python
>>> def cube(x):
...     """Return the third power of x."""
...     return x*x*x
...
>>> map(cube, range(5))
[0, 1, 8, 27, 64]
```

For such a simple method, this is a lot of typing! We can use a `lambda` function to
define such simple methods inline.

```python
>>> map(lambda x: x*x*x, range(5))
[0, 1, 8, 27, 64]
```

The syntax of defining a `lambda` is like this:

```
lambda <args>: <return expression>
```

`<args>` is a command-separate set of variables that the `lambda` can take as
arguments, and `<return expression>` is the code that is run. A `lambda`
automatically returns whatever the result of the expression is, you don’t need
a `return` (the `return` is _implicit_).

Writing a `lambda` statement defines a method, which you can capture as a
variable just like any other object.

```python
>>> div2 = lambda x: x/2
>>> div2
<function <lambda> at 0x7fc6b2207758>
>>> map(div2, range(5))
[0.0, 0.5, 1.0, 1.5, 2.0]
```

Note that we got real numbers back because we are using Python 2 with `from __future__ import division`.

{% challenge "Sum in quadrature" %}

Write a method that accepts an arbitrary number of arguments, and returns the
sum of the arguments computed in quadrature. A “sum in quadrature” is the
square root of the sum of the squares of each number. You should use `lambda`
to define a squaring and a square root function, and `map` to apply the
squaring method.

{% solution "Solution" %}

We need a little square root method and a method to square its input.
```python
>>> square = lambda x: x*x
>>> sqrt = lambda x: x**0.5
```
We then define a method that can accept any number of arguments using the
`*args` syntax, and use `map` to call the `square` method on the list of
arguments. Then we can call `sum` on the result, and then `sqrt`.
```python
>>> def quadrature(*args):
...     """Return the sum in quadrature of the arguments."""
...     return sqrt(sum(map(square, args)))
...
>>> quadrature(1, 1) # should be equal to sqrt(2)
1.4142135623730951
>>> 2**0.5
1.4142135623730951
```

{% endsolution %}

{% endchallenge %}

Another use case for `lambda` is the built-in `filter` method (see:
`help(filter)`).

```python
>>> filter(lambda x: x % 2 == 0, range(10))   # filter and return the even numbers only
[0, 2, 4, 6, 8]
```

{% challenge "List comprehension" %}

How would you rewrite the `filter` example above using a list comprehension?
{% solution "Solution" %}

```python
>>> [ x for x in range(10) if x % 2 == 0 ]
[0, 2, 4, 6, 8]
```

{% endsolution %}

{% endchallenge %}

Generally, you should only use `lambda` methods to define little throw-away
methods. The main downside with using them is that you can’t attach a docstring
to them, and they become unwieldy when there’s complex logic.
