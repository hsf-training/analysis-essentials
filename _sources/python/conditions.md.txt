# Conditions

Sometimes, often while looping, you only want to do things depending on
something’s value. Specifying _conditions_ like this is pretty simple in Python.

```python
>>> pizzas = ['Pineapple', 'Cheese', 'Pepperoni', 'Hot dog']
>>> for p in pizzas:
...     if p == 'Cheese':
...         print('Nice pizza!')
...     elif p == 'Pepperoni':
...         print('Amazing pizza!')
...     else:
...         print('Weird pizza.')
...
Weird pizza.
Nice pizza!
Amazing pizza!
Weird pizza.
```

Like the "body" of the `for` loop, called a _block_, the block in the `if`,
`elif`, and `else` statements must be indented. The convention we adopt is to
use four spaces for indentation.

The `if` statement starts with `if` (duh!) and what follows is a _condition_.
If this condition isn’t met, the next `elif` (for "else-if") condition is
evaluated. If this also isn’t met, the `else` block is run. You can use as many
`elif` conditions as you like, or none at all, and the `else` block is optional.

{% callout "Ternary conditional operator" %}

You can use a succinct one-line syntax for conditional assignments like this:

```python
>>> x = 'ok' if pizzas[0] == 'Cheese' else 'not ok'
>>> x
'not ok'
```

Make sure your line does not get too long in order not to impair its
readability!

{% endcallout %}


Python evaluates a condition and sees whether it is truth-like or not. If it is
truth-like, the code in the block is run.

```python
>>> if pizza[0] == 'Cheese':
...     print('It is cheese, my dudes.')
...
>>> pizza[0] == 'Cheese'
False
>>> pizza[1] == 'Cheese'
True
```

`False` and `True` are variables and they can actually be reassigned to some
other value (though it is quite pointless and dangerous to do that!) They
correspond to the possible values a boolean variable can have. Here is why you
should never touch those variables:

```python
>>> True = 1
>>> True
1
>>> True = False
>>> True == False
True
```

The result of a comparison is `True` or `False`, and we can perform comparisons
using several operators, like `==` for equality, `!=` for inequality, `>` and
`<` for relative magnitude, and so on.

```python
>>> True, False
(True, False)
>>> False
False
>>> True == False
False
>>> True != False
True
>>> 1 > 2
False
>>> (1 > 2) == False
True
```

This shows that we can combine comparison operators, just like with `+` and
friends. We can also use `and` to require multiple conditions, `or` to require
at least one, and `not` to negate a result.

```python
x = 2
>>> 1 < x and x < 3
>>> 3 < x or 1 < x
True
>>> not 1 < x
False
```

Note that `and`, `or` and `not` have lower precedence than `>`, `<` and `==`, but
you can use parentheses to be more explicit. 

Of course, we can compare everything we have played around with so far.

```python
>>> x = [1, 2]
>>> y = [1, 2]
>>> z = {'hero': 'thor'}
>>> x == y
True
>>> y == z
False
```

For collection objects like lists, tuples, and dictionaries, we can easily ask
them if they contain something in particular using the `in` operator.

```python
>>> 3 in x
False
>>> 2 in y
True
>>> 'thor' in z
False
```

The last statement is `False` because `in` queries a dictionaries _keys_, not 
its values. This is useful if you want to access a key in a dictionary that 
might not exist:

```python
>>> z['pizza']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> if 'pizza' in z:
...     print('We have pizza', z['pizza'])
... else
...     print('No pizza :(')
```

Note that `in` doesn’t dive into nested collections, but only looks at the top
level.

```python
>>> 1 in [[1, 2], [3, 4]]
False
>>> [1, 2] in [[1, 2], [3, 4]]
True
```

{% challenge "The `in` operator" %}

Find the double-underscore method on lists and dictionaries that corresponds to
the `in` operator, and check that it does the same thing as the operator.

{% solution "Solution" %}

Taking lists as an example, the `dir` method can tell us what methods are
available. The `__contains__` method sounds promising.

```python
>>> x= [1]
>>> x.__contains__(1)
True
>>> x.__contains__(2)
False
```

{% endsolution %}

{% endchallenge %}

Strings work a lot like lists, which makes sense because they are effectively
collections of single characters. This means we can also query string contents
with `in`.

```python
>>> fact = 'The best hero is Thor.'
>>> 'Thor' in fact
True
>>> 'Iron Man' in fact
False
```

## Truthiness

It’s conventional not to explicitly compare a condition to `True`, because the
`if` statement already does that for us.

```python
>>> if ('Pineapple' in pizzas) == True:
...     print('Weird.')
...
>>> if 'Pineapple' in pizzas:
...     print('Not weird.')
...
```

Likewise, rather than comparing for False, we just use `not`.

```python
>>> if ('Pineapple' in pizzas) == False:
...     print ('Weird.')
...
>>> if not 'Pineapple' in pizzas:
...     print ('Not weird.')
...
>>> not 'Pineapple' in pizzas:
>>> 'Pineapple' not in pizzas:
```

The last two lines show that we can use `not in` for checking that something
_is not_ in a collection. This reads more naturally.

All Python objects are truth-like unless they are the value `False`, the value
`None`, or are empty collections (such as `""`, `[]`, `()`, `{}`).

```python
>>> if list() or dict() or tuple() or str():
...     print ("You won’t see me!")
```

The value `None`, which is available as the variable named `None`, is often
used as placeholder for an empty value.

```python
>>> favourite = None
>>> for p in pizzas:
...     if 'Olives' in p:
...         favourite = p
...
>>> if favourite:
...     print ('Found favourite: {0}'.format(favourite))
... else:
...     print ('No favourite :(')
No favourite :(
```

It behaves as false-y value in conditions.

## Conditions in loops

`for` loops and comprehensions are the most common ways of iterating in Python.
We’ve already seen that using conditions in these can be useful.

```python
>>> not_cheesy = [p for p in pizzas if 'cheese' not in p.lower()]
>>> not_cheesy
['Pineapple', 'Pepperoni', 'Hot dog']
```

Another way of iterating is with `while`.

```python
>>> i = 5
>>> while i > 0:
...     print 'T-minus {0} seconds'.format(i)
...     # Equivalent to `i = i - 1`
...     i -= 1
... print ('Blast off!')
T-minus 5 seconds
T-minus 4 seconds
T-minus 3 seconds
T-minus 2 seconds
T-minus 1 seconds
Blast off!
```

The `while` loop checks the condition, runs the block, and then re-checks the
condition. If we don’t do something in the loop to change the result of the
condition, we will end up looping forever!

```python
>>> i = 5
>>> while i > 0:
...     print('All work and no play makes Jack a dull boy')
```

Because we do not change the value of `i` in the loop, the condition always
evaluates to `True`, so we’re stuck. You can stop Python running the code by
typing the `Ctrl-c` key combination.

Sometimes you want to stop iterating when some condition is met. You could
achieve this with a `while` loop.

```python
>>> ok = False
>>> i = 0
>>> while not ok:
...     ok =  'cheese' in pizza[i].lower()
...     # Equivalent to `i = i + 1`
...     i += 1
...
>>> i
2
>>> pizza[i - 1]
'Cheese'
```

It is not nice to have to keep track of these `ok` and `i` variables. Instead,
we can use a `for` loop, which feels much more natural when iterating over a
collection, and `break` to stop looping.

```python
>>> for pizza in pizzas:
...     if 'cheese' in pizza.lower():
...         yum = pizza
...         break
...
>>> yum
'Cheese'
```
