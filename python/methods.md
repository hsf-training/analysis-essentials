# Methods

Methods, also called functions, take some input and return some output. We’ve 
already used lots of methods, like `dir`, `help`, and `len`, and in this lesson 
we’ll start creating are own.

As we’ve seen, methods can do a lot of stuff with very little typing. Methods 
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
Help on function foo in module __main__:

foo(x)
    Return the number of elements in obj.

>>> length('A b c!')
6
>>> length(range(5))
5
```

There’s a lot going on here, so we’ll break it down line-by-line.

1. `def length(obj)`: methods are _defined_ using `def`, followed by a space, 
   and then the name you want to give the method.[^1] Inside the parentheses 
   after the name, we list the inputs, or _arguments_, that we want our method 
   to accept.  In this case, we only need a single input: the thing we want to 
   compute the length of.  Finally, there’s a colon at the end, just like with 
   a `for` or `if`, which means a _block_ of code follows (which must be 
   indented).
2. `"""Return the number of elements in obj."""`: This is the _docstring_. It’s 
   just a string, defined literally with three double quotes so that we can 
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
...    print x
...    print y
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
>>> add(y=2, 1)
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

Using keyword arguments is particularly useful for arguments with act as flags, 
because it’s often not obvious what your `True` or `False` is doing.

```python
>>> def add(x, y, show):
...    """Return the sum of x and y.
...
...    Optionally print the result before returning it.
...    """
...    if show:
...        print x + y
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
...        print x + y
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
>>> increment_two = make_incrementator(1)
>>> print increment_one(42), increment_two(42)
43 44
>>> print make_incrementator(3)(42) # Do it in one go!
45
```
{% endchallenge %}

TODO: Lambdas, `*args`, `**kwargs`.
