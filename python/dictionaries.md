# Dictionaries

You can think of lists as a _mapping_ from indices to values. The indices are 
always integers and go from `0` to `len(the_list)`, and the values are the 
items.

Dictionaries are like lists, but they can map from more than just integers.  
Because of this, you must always specify the index for every item when creating 
a dictionary.

```python
>>> d = {1: 0.5, 'excellent index': math.sin, 0.1: 2}
>>> d[1]
0.5
>>> d['excellent index']
<built-in function sin>
>>> d[0.1] = 3
```

The ‘indicies’ of a dictionary are called _keys_, and the things they map to 
are values. Together, each key-value pair is an _item_.

```python
>>> d.keys()
[1, 0.1, 'excellent index']
>>> d.values()
[45, 3, <built-in function sin>]
>>> d.items()
[(1, 45), (0.1, 3), ('excellent index', <built-in function sin>)]
```

As you can see, the values of a dictionary can be whatever we like, and need 
not be the same type of object.

Interestingly, the order of the keys, values, and items we get back are not the 
same as the order we created the dictionary with. (You might see a different 
order on your machine to the one above.) This is important: there is never a 
guarantee that your dictionary will be ordered in the same order you inserted 
items into it.  What _is_ guaranteed is that whatever order you get from 
`keys()` will be the same as with `values()`.  This allows you to do things 
like this without going crazy:

```python
>>> for key, value in zip(d.keys(), d.values()):
...     print key, ':', value
...
1 : 45
0.1 : 3
excellent index : <built-in function sin>
```

Of course, this could considerably simpler just by using `items()`, which gives 
us tuples of key-value pairs.

```python
>>> for key, value in d.items():
...     print key, ':', value
...
1 : 45
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

Iteration over dictionaries is over their keys.

```python
>>> for key in d:
...     print key, ':' d[key]
...
1 : 0.5
0.1 : 3
excellent index : <built-in function sin>
```

We’ve already seen how to iterate over values (using `d.values()`) or keys and 
values simultaneously (using `d.items()`).

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
Then, create the ‘inverse’ dictionary, again with a comprehension, mapping 
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
{% endchallenge %}
