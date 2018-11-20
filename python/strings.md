# Strings

Number objects are useful for storing values which are, well, numbers. But what 
if we want to store a sentence? Enter _strings_!

```python
>>> a = "What's orange and sounds like a parrot?"
```

Strings can be joined with `+`.

```python
>>> b = 'A carrot'
>>> a + ' ' + b
'What's orange and sounds like a parrot? A carrot'
```

And they can be multiplied by numbers, amazingly.

```python
>>> c = 'omg'
>>> 10*c
'omgomgomgomgomgomgomgomgomgomg'
```

We’ve specified strings _literally_, _in_ the source code, by wrapping the text 
with singles quotes or double quotes. There’s no difference; most people choose 
one and stick with it.

It can be useful to change if your text contains the quote character. If it 
contains both, you can _escape_ the quote mark by preceding it with a 
backslash. This tells Python that the quote is part of the string you want, and 
not the ending quote.

```python
>>> fact = "Gary's favourite word is \"python\"."
>>> fact
'Gary\'s favourite word is "python".'
```

Python prints strings by surrounding them with _single_ quotes, so it escapes 
the single quotes in our string. This is useful because we can copy-paste the 
string into some Python code to use it somewhere else, without having to worry 
about escaping things.

We can create multi-line strings by using three quotation marks. 
Conventionally, double quotations are usually used for these.

```python
>>> long_fact = """This is a long string.
...
... Quite long indeed.
... """
>>> print long_fact
This is a long string.

Quite long indeed.

>>>
```

Creating strings like this is useful when you want to include line breaks in 
your string. You can also use `\n` in strings to insert line breaks.

```python
>>> 'This is a long string\n\nQuite long indeed.\n'
```

We can convert things to strings by using the `str` method, which can also 
create an _empty_ string for us.

```python
>>> str()
''
>>> 'A number: ' + str(999 - 1)
'A number: 998'
```

Strings are objects, and have lots of useful methods attached to them. If you 
want to know how many characters are in a string, you use the global `len` 
method.

```python
>>> b.upper()
'A CARROT'
>>> b.upper().lower()
'a carrot'
>>> b.replace('carrot', 'parrot').replace(' ', '_')
'A_parrot'
>>> len(b)
8
>>> b
'A carrot'
```

Notice that none of these operations _modify_ the value of the `b` variable. 
Operations on strings _always_ return _new_ strings. Strings are said to be 
_immutable_ for this reason: you can never change a string, just make new ones.

## Formatting

One of the most common things you’ll find yourself doing with strings is 
interleaving values into them. For example, you’ve finished an amazing 
analysis, and want to print the results.

```python
>>> result1 = 123.0
>>> result2 = 122.3
>>> print('My results are: ' + str(result1) + ', ' + str(result2))
My results are: 123.0, 122.3
```

This is already quite ugly, and will only get worse with more results. We can 
instead use the `format` method that’s available on strings, and use the 
special `{}` placeholders to say where we want the values to go in the string.

```python
>>> template = 'My results are: {0}, {1}'
>>> print(template.format(result1, result2))
My results are: 123.0, 122.3
```

Much better! We define the whole string at once, and then place the missing 
values in later.

The numbers inside the placeholders, `{0}` and `{1}`, correspond to the indices 
of the arguments passed to the `format` method, where `0` is the first 
argument, `1` is the second, and so on. By referencing positions like this, we 
can easily repeat placeholders in the string, but only pass the values once to 
`format`.

```python
>>> template2 = 'My results are: {0}, {1}. But the best is {0}, obviously.'
>>> print(template2.format(result1, result2))
My results are: 123.0, 122.3. But the best is 123.0, obviously.
```

You can also use _named_ placeholders, then passing the values to `format` 
using the same name.

```python
>>> template3 = 'My results are: {best}, {worst}. But the best is {best}, obviously.'
>>> print(template3.format(best=result1, worst=result2))
My results are: 123.0, 122.3. But the best is 123.0, obviously.
```

This is nice because it gives more meaning to what the placeholders are for.

There’s [a lot you can do inside the placeholders][strformat], such as specifying that you want to format a number with a certain number of decimal places.

```python
>>> print('This number is great: {0:.3f}'.format(result1))
This number is great: 123.000
```

If you want to print a literal curly brace using `format`, you will need to
escape it by doubling it, so that `{{` will become `{` and `}}` will become `}`.
Here's an example:

```python
>>> print('This number will be surrounded by curly braces: {{{0}}}'.format(123))
This number will be surrounded by curly braces: {123}
```

The innermost `{0}` is replaced with the number, and `{{...}}` becomes `{...}`.

[strformat]: https://pyformat.info/
