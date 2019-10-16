# Lists and looping

Now things start to get _really_ interesting! Lists are collections of things 
stored in a specific order. They can be defined literally by wrapping things in 
square brackets `[]`, separating items with commas `,`.

```python
>>> a = [4, 2, 9, 3]
>>> a
[4, 2, 9, 3]
```

Python lists can contain collections of whatever you like.

```
>>> excellent = [41, 'Hello', math.sin]
```

Each item in the list can be accessed by its _index_, its position in the list, 
which starts at zero for the first item. Indexing by negative numbers starts 
from the _last_ item of the list.

```python
>>> a[0]
4
>>> a[2]
9
>>> a[-1]
3
```

We’ll get an error if we try to access an index that doesn’t exist:

```python
>>> a[99]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Like strings, lists have a length which can be found with the `len` method.

```python
>>> len(a)
4
```

Unlike strings, lists are _mutable_, which means we can modify lists in-place, 
without creating a new one.

```python
>>> a.append(45)
>>> a
[4, 2, 9, 3, 45]
>>> len(a)
5
```

We can see that lists are mutable because using the `append` method didn’t 
print anything, and our variable `a` now has a different value.

Because lists are mutable, we can use the special `del` keyword to remove 
specific indices from the list.

```python
>>> del a[-2]
>>> a
[4, 2, 9, 45]
```

{% callout "Functions and keywords" %}

`del` is a language keyword representing an action, and not a function. The
syntactic difference is that functions take their arguments between parentheses,
such as `my_function(1, 2, 3)`, whereas `del` does not.

{% endcallout %}

You can retrieve sub-lists by using _slice_ notation whilst indexing.

```python
>>> a[1:-1]
[2, 9]
```

This retrieves the part of list `a` starting from index `1` until _just before_ 
index `-1`. The indexing is ‘exclusive’ in that it excludes the item of the 
last index. This is the convention of indexing in Python.

You can omit a number in the first or second indexing position, and Python will 
assume you mean the first element (index zero) and last element (index 
`len(array)`).

```python
>>> a[:-2]
[4, 2
>>> a[1:]
[2, 9, 45]
>>> a[:]
[4, 2, 9, 45]
```

Slicing returns a copy of the array, so modifying the return value doesn’t 
affect the original array.

```python
>>> b = a[1:]
>>> b
[2, 9, 45]
>>> b[0] = 3
>>> b
[3, 9, 45]
>>> a
[4, 2, 9, 45]
```

We did something cool there by assigning a value to a specific index, `b[0] =
3`. The same trick works with slices.

```python
>>> b[:2] = [99, 2, 78]
>>> b
[99, 2, 78, 45]
```

This is equivalent of _replacing_ a certain range (`:2`, or items at position 0
and 1) of the list `b` with other items from another list. Note that in our
example we replace 2 elements with 3. The same syntax might be used for
inserting elements at an arbitrary position in the list. If we want to insert
the number 6 between the 2 and the 78 in the list above, we would use:

```python
>>> b[2:0] = [6]
>>> b
[99, 2, 6, 78, 45]
```

meaning _take out 0 elements from the list starting a position 2 and insert the
content of the list `[6]` in that position_.

{% challenge "Copying a list" %}

Slicing creates a copy, so what notation could you use to copy the full list?

{% solution "Solution" %}

You need to slice from the very beginning to the very end of the list.
```python
>>> a[:]
[4, 2, 9, 45]
```
This is equivalent to specifying the indices explicitly.
```python
>>> a[0:len(a)]
[4, 2, 9, 45]
```

{% endsolution %}

{% endchallenge %}

## Looping

When you’ve got a collection of things, it’s pretty common to want to access 
each one sequentially. This is called looping, or iterating, and is super easy.

```python
>>> for item in a:
...     print item
...
4
2
9
45
```

We have to indent the code inside the `for` loop to tell Python that these
lines should be run for every iteration.

{% callout "Indentation in Python" %}

The `for` loop is a block, and every Python block requires indentation, unlike
other "free-form" languages such as C++ or Java. This means that Python will
throw an error if you don't indent:

```python
>>> for i in b:
... print(i)
  File "<ipython-input-56-11d6523211c0>", line 2
    print(i)
        ^
IndentationError: expected an indented block
```

Indentation must be consistent within the same block, so if you indent two lines
in the same `for` loop using a different number of spaces, Python will complain
once again:

```python
>>> for i in b:
...   print("I am in a loop")
...     print(i)
  File "<ipython-input-57-5c3d29e65ad9>", line 3
    print(i)
    ^
IndentationError: unexpected indent
```

Indentation is necessary as Python does not use any keyword or symbol to
determine the end of a block (_e.g._ there is no `endfor`). As a side effect,
indentation forces you to make your code more readable!

Note that it does not matter how many spaces you use for indentation. **As a
convention, we are using four spaces.**

{% endcallout %}

The variable name `item` can be whatever we want, but its value is changed by 
Python to be the element of the item we’re currently on, starting from the 
first.

Because lists are mutable, we can try to modify the length of the list whilst 
we’re iterating.

```python
>>> a_copy = a[:]
>>> for item in a_copy:
...     del a_copy[0]
...
>>> a_copy
[9, 45]
```

Intuitively, you might expect `a_copy` to be empty, but it’s not! The technical
reasons aren’t important, but this highlights an important rule: **never
modify the length of a list whilst iterating over it!** You won’t end up with
what you expect.

You can, however, freely modify the _values_ of each item in the list whilst 
looping. This is a very common use case.

```python
>>> a_copy = a[:]
>>> i = 0
>>> for item in a_copy:
...     a_copy[i] = 2*item
...     i += 1
...
>>> a_copy
[8, 4, 18, 90]
```

Keeping track of the current index ourselves, with `i` is annoying, but luckily 
Python gives us a nicer way of doing that.

```python
>>> a_doubled = a[:]
>>> for index, item in enumerate(a_doubled):
...     a_doubled[index] = 2*item
...
>>> a_doubled
[8, 4, 18, 90]
```

There’s a lot going on here. Firstly, note that Python lets you assign values 
to multiple variables at the same time.

```python
>>> one, two = [34, 43]
>>> print(two, one)
43 34
```

That’s already pretty cool! But then think about what happens if you had a list 
where each item was another list, each containing two numbers.

```python
>>> nested = [[20, 29], [30, 34]]
>>> for item in nested:
...     print(item)
...
[20, 29]
[30, 34]
```

So, we can just assign each item in the sublist to separate variables in the 
`for` statement.

```python
>>> for one, two in nested:
...     print(two, one)
...
29 20
34 30
```

Now we can understand a little better what `enumerate` does: for each item in 
the list, it returns a new list containing the current index and the item.

```python
>>> enumerate(a)
<enumerate object at 0x7f5abe5b1190>
>>> list(enumerate(a))
[(0, 4), (1, 2), (2, 9), (3, 45)]
```

For performance reasons `enumerate` doesn’t return a list directly, but instead
something that the `for` statement knows how to iterate over (this is called a
[generator](https://wiki.python.org/moin/Generators) and for the moment you
don't need to know how it works). We can convert it to a list with the `list`
method when we want to see what’s it doing.

This technique of looping over lists of lists lets us loop over two lists 
simultaneously, using the `zip` method.

```python
>>> for item, item2 in zip(a, a_doubled):
...     print(item2, item)
...
8 4
4 2
18 9
90 45
```

Neat! As before, we can see what `zip` is doing explicitly by using `list`.

```python
>>> list(zip(a, a_doubled))
[(4, 8), (2, 4), (9, 18), (45, 90)]
```

You can see that the structure of the list that’s iterated over, the output of 
`zip`, is identical to that for `enumerate`.

Finally, we’ll take a quick look at the `range` method.

```python
>>> for i in range(0, 10):
        print(i)
0
1
2
3
4
5
6
7
8
9
```

The arguments to `range` work just like slicing, the second argument is treated 
exclusively, as its value is excluded from the output. Again like slicing, we 
can specify a third argument as the step size for the iteration.

```python
>>> for i in range(0, 10, 2):
        print(i)
0
2
4
6
8
```

If you only give a single argument to `range`, it assumes you’ve given the end 
value, and want a starting value of zero.

```python
>>> for i in range(5)
        print(i)
0
1
2
3
4
```

This reads “give me a list of length 5, in steps of 1, starting from zero”.

Now that we know how to easily generate sequences of numbers, we can write 
`enumerate` by hand!

```python
>>> for index, item in zip(range(len(a)), a):
...     print(index, item)
...
0 4
1 2
2 9
3 45
```

Just like before! When you see something cool like `enumerate`, it can be fun 
trying to see how you’d accomplish something similar with different building 
blocks.

## List comprehension

We’ve already made a new list from an existing one when we created `a_doubled`.

```python
>>> a_doubled = a[:]
>>> for index, item in enumerate(a_doubled):
...     a_doubled[index] = 2*item
```

Creating a new list from an existing one is a common operation, so Python has a 
shorthand syntax called _list comprehension_.

```python
>>> a_doubled = [2*item for item in a]
>>> a_doubled
[8, 4, 18, 90]
```

Isn’t that beautiful?

We can use the same multi-variable stuff we learnt whilst looping.

```python
>>> [index*item for index, item in enumerate(a)]
[0, 2, 18, 135]
```

We’re not restricted to creating new lists with the same structure as the 
original.

```python
>>> [[item, item*item] for item in a]
[[4, 16], [2, 4], [9, 81], [45, 2025]]
```

We can even filter out items from the original list using `if`.

```python
>>> [[item, item*item] for item in a if item % 2 == 0]
[[4, 16], [2, 4]]
```

List comprehensions are a powerful way of succinctly creating new lists. But be 
responsible; if you find you’re doing something complicated, it’s probably 
better to write a full `for` loop.

## Tuples

A close relative of lists are tuples, which differ in that they cannot be 
mutated after creation.  You can create tuples literally using parentheses, or 
convert things to tuples using the `tuple` method.

```python
>>> a = (3, 4)
>>> del a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> a.append(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> a[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> b = tuple([65, 'yes'])
>>> b
(65, 'yes')
```

Tuples are usually used to describe data whose length is meaningful in and of 
itself. For example, you could express coordinates as a tuple.

```python
>>> coords = (3.2, 0.1)
>>> x, y = coords
```

This is nice because it doesn’t make sense to append to an `$ (x, y) $` 
coordinate, nor to ‘delete’ a dimension. Generally, it can be useful if the 
data structure you’re using respects the _meaning_ of the data you’re storing.

If you can’t think of a use for tuples yourself, its worth keeping in mind that 
Python creates tuples for groups of things by default. We saw that 
earlier when we used `enumerate`.

```python
>>> list(enumerate([4, 9]))
[(0, 4), (1, 9)]
```

Each element of the list is a tuple.

{% challenge "Write a list comprehension yourself" %}

Compute the square of the magnitude of the sum of the following two 
three-vectors, using a single list comprehension and the global `sum` method.
```python
>>> kaon = [3.4, 4.3, 20.0]
>>> pion = [1.4, 0.9, 19.8]
```
It might help to first think about how you’d compute the quantity for a single 
vector.

{% solution "Solution" %}

Not sure what the `sum` method does? Ask for `help`!
```python
>>> help(sum)
```
The square magnitude is the sum of the squares of the components, where the 
components are the sum of the two input vectors.
```python
>>> magsq = sum([(k + pi)**2 for k, pi in zip(kaon, pion)])
```
The square root of this is around 40.42.

{% endsolution %}

{% endchallenge %}
