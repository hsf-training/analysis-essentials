# Objects and operators

We can see that `math` somehow knows about `sin`, but how can we _use_ it? The 
answer is the dot _operator_ `.`.

```python
>>> math.sin
<function math.sin>
```

Operators are special pieces of the _syntax_ of a programming language.
Syntax is the way you express what you want to do.

In Python, an operator acts on the thing that’s on the right of it using the 
thing on the left. In the example we just saw, the dot operator `.` _acts_ on 
`math` in a way that, somehow, _retrieves_ a method called `math.sin`. We can 
then use that method straight away:

```python
>>> math.pi
3.141592653589793
>>> math.sin(math.pi)
1.2246467991473532e-16
```

Here we see there’s also a _property_ of `math` called `pi`, which seems to 
have the appropriate value.

We could also store the result of `math.sin` in a variable, and use it later.

```python
>>> twopi = 2*math.pi
>>> my_sin = math.sin
>>> my_sin(twopi)
-2.4492935982947064e-16
```

There are several symbols that can be used as operators, like `+`, `-`, `*`, 
and `/`. Certain things support the use of certain operators. For example, 
numbers support the plus operator:

```python
>>> 1 + 2
3
```

The plus operator acts on `1` with `2`, and, somehow, `1` knows how to deal 
with `2`, in this case by performing addition as we know it.

When we do `1 + 2`, what’s going on behind the scenes is _exactly_ the same as 
when do `math.sin`. Observe!

```python
>>> (1).__add__
<method-wrapper '__add__' of int object at 0x7fdc7ea75980>
>>> (1).__add__(2)
3
```

Numbers have a special `__add__` method attached to them, in the _same way_ 
that `math` has a `sin` method attached. The plus operator `+` is just a 
_shortcut_ for accessing this `__add__` method. The double underscores either 
side of the name tell you that there’s something special about it; in this case 
it means that you can use the plus operator `+` instead.

{% challenge "Methods for other operators" %}

The other operators that you can use with numbers have corresponding methods. 
What other operator methods are available? Try some of them out, and see how 
they compare with using the operator like normal.
{% solution "Solution" %}

We’ve already met two ways that you can find out what things are attached to 
something. In IPython, you can try `(1).__<tab>`, or you can always use the 
`dir` method.

```python
>>> dir(1)
['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 ...
 'to_bytes']
```

Then it’s just a case of scanning through this list and seeing what names look 
right. The `__sub__` name looks like ‘subtraction’, and similarly `__mul__` and 
`__truediv__` sound like multiplication and division.

```python
>>> (1).__mul__(5)
5
>>> (1).__truediv__(5)
0.2
```

{% endchallenge %}

Of course, there’s also a method for the dot operator! It’s called 
`__getattribute__`, and it takes the name of the thing you want to get.

```python
>>> (1).__add__
<method-wrapper '__add__' of int object at 0x7fdc7ea75980>
>>> (1).__getattribute__('__add__')
<method-wrapper '__add__' of int object at 0x7fdc7ea75980>
```

So, of course, we can do this horrible one-liner:

```python
>>> (1).__getattribute__('__add__')(3)
4
```

You would _never_ do something like this in your day-to-day programming, but 
we’ve done it here to illustrate how Python performs operations.

## Objects

The use of the dot operator is interesting because we’re manipulating the 
fundamental building block of Python: _objects_. Objects are containers of 
things, and we can access those things by name using the dot operator.
We can sometimes use other operators as a shorthand for accessing 
specially-named methods within objects, like using `+` for `__add__`.

Most things in Python are objects! Numbers, like we’ve seen, are objects, 
because we can retrieve things from them with `.`.  Of course, the object 
_itself_ is interesting because it can represent a value, like the number 
`999`.

It the next set of lessons, we’ll go through the different types of objects 
that come with the Python language.
