# Dictionaries

You can think of lists as a _mapping_ from indices to values. The indices are
always integers and go from `0` to `len(the_list)`, and the values are the
items.

Dictionaries are collections, just like lists, but they have important
differences:

* lists map sequential numeric indices to items, whereas dictionaries can map
  most object types to any object,
* lists are _ordered_ collections of items, whereas dictionaries have no
  ordering.

Since anything can be used as index for an item, indices must be always
specified when creating a dictionary:

```python
>>> d = {1: 0.5, 'excellent index': math.sin, 0.1: 2}
>>> d[1]
0.5
>>> d['excellent index']
<built-in function sin>
>>> d[0.1] = 3
```

The "indices" of a dictionary are called **keys**, and the things they map to
are **values**. Together, each key-value pair is an **item**.

```python
>>> d.keys()
dict_keys([1, 0.1, 'excellent index'])
>>> d.values()
dict_values([0.5, 2, <function math.sin>])
>>> d
{0.1: 2, 1: 0.5, 'excellent index': <function math.sin>}
```

As you can see, the values of a dictionary can be whatever we like, and need not
be the same type of object.

You can see that the order of the keys, values and items we get back are not the
same as the order we created the dictionary with. If you run the same example on
your own you might get a different ordering. This is what we mean when we define
dictionaries as _unordered collections_: when you iterate over its content, you
cannot rely on the ordering.

It is however guaranteed that the _n_-th item returned by `keys()` corresponds
to the _n_-th item returned by `values()`. This allows the following example
to work flawlessly:

```python
>>> for key, value in zip(d.keys(), d.values()):
...     print(key, ':', value)
...
1 : 0.5
0.1 : 3
excellent index : <built-in function sin>
```

Of course, this could be considerably simpler just by using `items()`, which
gives us _tuples of key-value pairs_.

```python
>>> for key, value in d.items():
...     print(key, ':', value)
...
1 : 0.5
0.1 : 3
excellent index : <built-in function sin>
```

We can create dictionaries from lists of 2-item lists.

```python
>>> dict(enumerate(['a thing', 'another']))
{0: 'a thing', 1: 'another'}
```

And also with _dictionary comprehensions_, in a similar manner to list
comprehensions, with the additional specification of the key.

```python
>>> {i: i**i for i in range(5) if i != 3}
{0: 1, 1: 1, 2: 4, 4: 256, 5: 3125}
```

Note that dictionary comprehensions require at least Python 2.7 to work.


## Dictionary keys

There’s no restriction on values a dictionary might hold, but there is on keys.

```python
>>> l = [1, 4, 3]
>>> dd = {}
>>> dd[l] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

In essence, keys must not be mutable. This includes numbers, strings, and
tuples, but not lists. This restriction is a trade-off that allows Python to
make accessing values in a dictionary by key very fast.

{% callout "Hashing" %}

Immutable data types in Python have a `__hash__()` function, you can test it
yourself:

```python
>>> s = "a string"
>>> s.__hash__()
-8411828025894108412
```

[A hashing function](https://en.wikipedia.org/wiki/Hash_function) creates an
encoded (but not unique) representation of the object as a number. When you
look up an item in a Python dictionary with `my_dict["my_key"]`, what happens
internally is:

* hash of `"my_key"` is calculated,
* this number is compared to every hash of every key in the dictionary, until a
  match between the hashes is found,
* if two hashes match, _and_ the two objects are really identical, the
  corresponding dictionary item is returned.

Looking up numbers instead of strings or tuples is considerably faster, but
since two different strings can have the same hash, their content has to be
compared as well to really tell whether they are equal. If two hashes are
different on the other hand we are sure that the objects are different as well.

{% endcallout %}

Iteration over dictionaries is over their keys.

```python
>>> for key in d:
...     print key, ':' d[key]
...
1 : 0.5
0.1 : 3
excellent index : <built-in function sin>
```

We have already seen how to iterate over values (using `d.values()`) or keys
and values simultaneously (using `d.items()`).

{% callout "On the efficiency of items()" %}

In Python 2, using items copies the keys and values of a dictionary, and gives
you back those copies. This can be problematic for large dictionaries as the
amount of memory your program uses can double. Python 3 uses a much more
memory-efficient way of implementing items so that you don't have to worry.

If you're having memory problems with using items in Python 2, you can use
`viewitems()` instead, which behaves the same way as items does in Python 3.

Note that there are also similar methods for keys and values, called
`viewkeys()` and `viewvalues()`, and that all of these view methods are only
available from
Python 2.7.

{% endcallout %}

{% challenge "Alphabet mapping" %}

Map each letter of the alphabet to a number with a dictionary comprehension,
starting with `0` for `a` and ending with `25` for `z`.

You can get a string containing the letters of the alphabet like this:

```python
>>> import string
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
```

You can iterate over a string exactly like a list.

```python
>>> for character in string.ascii_lowercase:
...     print character
...
a
b
...
z
```
Then, create the "reverse" dictionary, again with a comprehension, mapping
letters to numbers.

{% solution "Solution" %}

You need to have a list containing one number per letter, and to loop over that
list along with the characters in the string. This is exactly the same as
looping over items in a list alongside the index, so we can use `enumerate`.

```python
>>> alphabet_map = {i: c for i, c in enumerate(string.ascii_lowercase)}
```

We can create the inverse map by swapping the key and value in the
comprehension.

```python
>>> reverse_map = {c: i for i, c in alphabet_map.items()}
```

{% endsolution %}

{% endchallenge %}
