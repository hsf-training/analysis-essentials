# Modules

Python comes with lots of useful stuff. We’ve already met the maths module, but 
didn’t talk about how we started using it.

```python
>>> import math
>>> math
<module 'math' from '/usr/lib/python2.7/lib-dynload/math.so'>
>>> math.pi
3.141592653589793
>>> math.sin(1)
0.8414709848078965
```

(The path after `from` might look different on your computer.)

So, `math` is a _module_, and this seems to behave a lot like other objects 
we’ve met: it’s a container with properties and methods attached that we can 
access with the dot operator `.`. Actually, that’s pretty much all there is to 
them!

The only piece of new syntax for us is `import`. Using `import` lets us use 
modules in our own code. As well as `import <module>`, we can also import only 
the specific pieces of the module we want to use. There are a couple of ways to 
express this; they are equivalent, only changing the name of the variable we 
have access to.

```python
>>> from random import uniform
>>> uniform(0, 1)
0.9016358095193693
>>> import random import gauss as normal
>>> normal(0, 1)
-0.615100936422843
```

Modules can contain other modules. Sometimes you can access these from the 
top-level module, other times you need to get them with `import`.

```python
>>> import os
>>> os.path
<module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>
>>> import os.path
>>> os.path
<module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>
>>> import os.path as amazing
>>> amazing
<module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>
>>> from os import path
>>> from os import path as amazing_again
>>> amazing_again
<module 'posixpath' from '/usr/lib/python2.7/posixpath.pyc'>
```

We can see that `path` is a _submodule_ of the `os` module. The various `... as 
<name>` constructs just mean we store the module with the name we want. This 
can be useful when two modules have the same name, but we want to use both of 
them, or when as module has a really long name that we don’t want to type all 
the time.

## Importing everything

You can choose to import _everything_ from a module, so that you can access its 
contents without prefixing the module name.

```python
>>> from math import *
>>> cos(pi)
-1.0
```

This is _not_ recommended, because it makes it harder to find out where a 
certain variable comes from. If you don’t want to reference the module name 
every time, doing something like the following is preferred:

```python
>>> from math import cos, pi
```

If you need to import a lot, you can split the import over multiple lines.

```python
>>> from math import (
...     exp,
...     log,
...     e,
...     floor
... )
>>> floor(exp(log(e)))
2.0
```

## The standard library

The set of things that Python comes with, from all of the types of objects to 
all of the different modules, is called the [standard library][stl]. It’s 
recommend to browse through the standard library documentation to see what’s 
available. There’s load of cool stuff, and knowing about it usually means 
having to do less work yourself.

[stl]: https://docs.python.org/2/library/index.html
