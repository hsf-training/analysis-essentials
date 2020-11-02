# Numbers

There’s nothing magical about numbers in Python, and we’ve already discovered 
how we perform operations on them.

```python
>>> (2*(1 + 3) - 5)/0.5
2
>>> 11 % 4
3
```


{% callout "Integer division in Python 2" %}


If for any reason (e.g. you want to use LHCb or Alice software) you have to use Python 2, 
beware of that Python 2 has a few different _types_ of numbers, and they can 
behave differently.

```python
>>> 10/3
3
>>> 10.0/3.0
3.3333333333333335
```

Interesting. Something different happens when we use numbers with and without 
decimal places! This occurs because numbers given with decimal places, like 
`3.14`  are _floats_, while those without, like `3`, are _integers_.

For historical reasons, dividing two integers in Python 2 returns an integer, 
where the intermediate result is always rounded down. Division using _at least 
one_ float gives us the more intuitive answer.

In Python 3, division with integers works the same way as with floats. You can 
ask to have this behaviour in Python 2.

```python
>>> from __future__ import division
>>> 3/4
0.75
>>> 3.0/4.0
0.75
```

Because the default behaviour in Python 2 is quite unintuitive, we recommend 
using the `from __future__ import division` line everywhere. We’ll come to what exactly this 
line is doing shortly.

If you _do_ want a rounding division, you then can ask for it explicitly with 
the `//` operation:

```python
>>> 10/3
3.3333333333333335

>>> 10//3
3
```

{% endcallout %}

{% callout "Operators" %}

This behaviour can be explained in terms of operators and the double-underscore 
methods. You can see that numbers have two methods for division:

```python
>>> dir(1)
[...,
 '__floordiv__',
 ...
 '__truediv__',
 ...]
```

In Python 2, the `/` operator corresponded to the `__floordiv__` method when 
used with integers, but the `__truediv__` operator when used with floats. In 
Python 3, and when using the `from __future__ import division` line, the `/` 
operator always uses the `__truediv__` method.

{% endcallout %}

Python also lets you manipulate complex numbers, using `j` to represent the 
complex term.

```python
>>> a = 1 + 4j
>>> b= 4 - 1j
>>> a - b
(-3+5j)
```

Complex numbers are objects, of course, and have some useful functions and 
properties attached to them.

```python
>>> a.conjugate()
(1-4j)
>>> a.imag
4.0
>>> a.real
1.0
```

Somewhat confusingly, computing the magnitude of a complex number can be done 
with the `abs` method, which is available globally.

```python
>>> abs(a)
4.123105625617661
>>> import math
>>> math.sqrt(a.real**2 + a.imag**2)
4.123105625617661
```

This also demonstrates the `**` operator, which for real numbers corresponds to 
exponentiation.

Each type of number can be created _literally_, like we’ve been doing, by just 
typing the number into your shell or source code, and by using the correspond 
methods.

```python
>>> int()
0
>>> float()
0.0
>>> complex()
0j
```
