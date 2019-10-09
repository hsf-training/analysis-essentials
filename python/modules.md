# Modules

Python comes with lots of useful stuff, which is provided with modules
(and submodules, see later).
We have already met the maths module, but did not talk about how we started using it.

```python
>>> import math
>>> math
<module 'math' from '/usr/lib/python2.7/lib-dynload/math.so'>
>>> math.pi
3.141592653589793
>>> math.sin(1)
0.8414709848078965
```

The path after `from` might look different on your computer.

So, `math` is a _module_, and this seems to behave a lot like other objects we
have met: it is a container with properties and methods attached that we can
access with the dot operator `.`. Actually, that is pretty much all there is to
them.


## Using modules into your code: import

The keyword `import`, usually specified at the beginning of your source code, is
used to tell Python what modules you want to make available to your current
code.

There are different ways of specifying an import. The one we have seen already
simply makes the module available to you:

```python
>>> import random
>>> random.uniform(0, 1)
0.5877109428927353
```

The module `random` contains functions useful for random number generation: with
the `import` above, we have made the `random` module accessible, and everything
within that module is accessible via the syntax `random.<name>`. For the record,
the `uniform(x,y)` method returns a pseudo-random number within the range
`$ [x,y] $`.

Sometimes you want to make only one or more things from a given module
accessible: Python gives you the ability to import just those:

```python
>>> from random import uniform, choice
>>> uniform(0, 1)
0.4059007502204043
>>> choice([ 33, 56, 42, -1 ])
42
```

In this case the `uniform` and `choice` names are available _directly_, _i.e._
without using the `random` prefix. All other functions in the `random` module
are not available in this case. For the record, the `choice` function returns a
random element from a given collection.

Another option is to import _all_ functions of a certain module and make them
available without a prefix:

```python
>>> from random import *
>>> gauss(0, 1)
-1.639334770284028
```

This is not that recommended as you generally do not know what is the extent
of what you are importing and you might end up with name clashes between your
current code and the imported module, as it will all be in the same namespace,
meaning directly available with no need for a `.<name>` syntax. 

Lastly, it is possible to import modules, or specific names from a module,
under an alias.

```python
>>> from random import uniform as uni
>>> uni(0, 1)
0.7288973406605329
>>> import numpy as np
np.arccos(1)
0.0
```

This option is useful when you need to assign shorter aliases to names you will
use frequently. In particular, the alias `np` for the `numpy` module will be
encountered a lot.

Note that modules can have submodules, specified with extra dots `.`:

```python
>>> from os.path import abspath
>>> abspath('..')
'/afs/cern.ch/user/d'
```

When importing a module, its **submodules are not available by default and you
must import them explicitly**:

```python
>>> import os
>>> os.getcwd()
'/afs/cern.ch/user/d/dberzano'
>>> import os.path
>>> os.path.basename(os.getcwd())
'dberzano'
```

Note that due to the current Python implementation of the `os` module, `os.path`
functions are _actually_ available _even without importing `os.path`. But just
`os`_. You cannot and should not rely on this implementation, which represents an exception
and might change in the future. Always import submodules explicitly!

It is also possible to import several modules with a single import command:

```python
>>> import os, sys, math
```

but this is [not recommended by the Python style guide][pep8-import], which
suggests to use several import statements, one per module, as it improves
readability:

```python
>>> import os
>>> import sys
>>> import math
```

If you need to import several names from a single module, you can split an import
function over multiple lines:

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
all of the different modules, is called the [standard library][stl]. It is
recommended to browse through the standard library documentation to see what is
available: Python is rich of standard modules, and you should reuse them as much
as possible instead of rewriting code on your own.

Some of the categories for which standard modules are available are:

* processing paths
* date and time manipulation
* mathematical functions
* parsing of certain file formats
* support for multiple processes and threads
* ...

Use standard Python library modules with confidence: being part of any standard
Python distribution, your code will be easily portable.


## Modules from PyPi

Many external modules can be found on [PyPi][pypi], the Python Package Index repository.
Some of those modules are
already part of some Python distributions (such as [Anaconda][anaconda], which
comes with more than a thousand science-oriented modules preinstalled).

If a certain module you need is not available on your distribution you can
easily install it with the `pip` shell command. Since you typically do not have write
access to the standard Python installation's directories, `pip` allows you to
install modules only for yourself, under your current user's home directory.
It is recommended to set up in your shell startup script (such as `~/.bashrc`)
the following two lines telling once and for all where to install and search for
Python user modules:

```bash
export PYTHONUSERBASE=$HOME/.local
export PATH=$PYTHONUSERBASE/bin:$PATH
```

Once you have done that, close your current terminal window and open a new one,
and you will be ready to use `pip`. We will see in a later lesson how to install
the `root_pandas` module with:

```bash
pip install --user root_pandas
```

## Modules inside a virtual environment

It is however usually preferable and safer to do everything inside a virtual environement.
The latter is like a copy of your current environement. Thus you can modify your virtual 
environement (including installing/deleting/updating modules) without affecting your default
environement. If at some point you realize you have broken everything, you can always exit
the virtual environement and go back to the default lxplus one.

To build a virtual environement based on LCG views, you can use [LCG_virtualenv][lcg_virtualenv]:

```bash
git clone https://gitlab.cern.ch/cburr/lcg_virtualenv.git
./lcg_virtualenv/create_lcg_virtualenv myVenv
```
To activate the virtual environement do:

```bash
source myVenv/bin/activate
```

You can then install stuff with `pip`, like for instance `root_pandas`:

```bash
pip install --upgrade root_pandas matplotlib
python -c 'import pandas; print(f"Got pandas from {pandas.__file__}")'
python -c 'import root_pandas; print(f"Got root_pandas from {root_pandas.__file__}")'
python -c 'import matplotlib; print(f"Got matplotlib from {matplotlib.__file__}")'
```

You can go back to the default environement using the `deactivate` command.


## Write your first Python module

The simplest Python module you can write is just a `.py` file with some
functions inside:

```python
# myfirstmodule.py

def one():
    print('this is my first function')

def two():
    print('this is my second function')
```

You can now fire an `ipython` shell and use those functions right away:

```python
>>> import myfirstmodule
>>> myfirstmodule.one()
this is my first function
>>> myfirstmodule.two()
this is my second function
```

By simply calling the file `myfirstmodule.py` we have made it available as a
module named `myfirstmodule` - given that the file is in the same directory
where we have launched the Python interpreter.

{% callout "Module name restrictions" %}

Note that you cannot pick any name you want for a module! From the
[Python style guide][pep8-modulenames], we gather that we should use "short,
all-lowercase names". As a matter of fact, if we used dashes in the file name,
we would have ended up with a syntax error while trying to load it:

```python
>>> import my-first-module
  File "<ipython-input-1-ef292d9e19fe>", line 1
    import my-first-module
             ^
SyntaxError: invalid syntax
```

Python treats `-` as a minus and does not understand your intentions.

{% endcallout %}


## Write a structured module

Let's now create a more structured module, with submodules and different files.
We can start from the `myfirstmodule.py` file and create a directory structure:

```bash
$ mkdir yabba
$ cp myfirstmodule.py yabba/__init__.py
```

We have reused the same file created before, copied it into a directory called
`yabba` and renamed it to `__init__.py`. The double underscore should ring a
bell: this is a Python special name, and it represents the "main file" within
a module, whereas the directory name now represents the module name.

This means that our module is called `yabba`, and if we import it, functions
from `__init__.py` will be available:

```python
>>> import yabba
>>> yabba.one()
this is my first function
>>> yabba.two()
this is my second function
```

We can create an additional file inside the `yabba` directory, say
`yabba/extra.py` and have more functions there:

```python
# yabba/extra.py

def three():
  print 'this function will return the number three'
  return 3
```

We have effectively made `extra` a submodule of `yabba`. Let's try:

```python
>>> import yabba
>>> filter(lambda x: not x.startswith('__'), dir(yabba))
['one', 'two']
>>> import yabba.extra
>>> yabba.extra.three()
yabba.extra.three()
this function will return the number three
3
```

{% challenge "What have I done with the filter function?" %}

We have used the filter function above to list the functions we have defined
in our module. Can you describe in detail what the commands above do?
{% solution "Solution" %}

The `dir(module)` command lists all _names_ (not necessarily functions, not
necessarily defined by us) contained in a given imported module. We have used the
`filter()` command to filter out all names starting with two underscores. Every
item returned by `dir()` is passed as `x` to the lambda function which returns
`True` or `False`, determining whether the `filter()` function should keep or
discard the current element.

{% endsolution %}

{% endchallenge %}


## Run a module

We can make a Python module that can be easily imported by other Python
programs, but we can also make it in a way that it can be run directly as a
Python script.

Let's write this special module and call it `runnable.py`:

```python
#!/usr/bin/env python

long_format = False

def print_label(label, msg):
    if long_format:
        out = '{0}: {1}'.format(label.upper(), str(msg))
    else:
        out = '{0}-{1}'.format(label[0].upper(), str(msg))
    print out

def debug(msg):
    print_label('debug', msg)

def warning(msg):
    print_label('warning', msg)

if __name__ == '__main__':
    print '*** Testing print functions ***'
    debug('This is a debug message')
    long_format = True
    warning('This is a warning message with a long label')
else:
    print 'Module {0} is being imported'.format(__name__)
```

Now let's make it executable:

```bash
$ chmod +x runnable.py
```

It can be now run as a normal executable from your shell:

```
$ ./runnable.py
*** Testing print functions ***
D-This is a debug message
WARNING: This is a warning message with a long label
```

There are two outstanding notions here. First off, the first line is a
"shebang": it really has to be the _first_ line in a file (it cannot be the
second, or "one of the first", or the first non-empty) and it basically tells
your shell that your executable text file has to be interpreted by the current
Python interpreter. Just use this line as it is.

Secondly, we notice we have a peculiar `if` condition with a block that gets
executed when we run the file. `__name__` is a special internal Python variable
which is set to the module name in case the module is imported. When the module
is ran, it is set to the special value `"__main__"`.

The `else:` condition we have added is just to show what happens when you import
the module instead:

```python
>>> import runnable
Module runnable is being imported
>>> runnable.warning('hey I can use it from here too')
W-hey I can use it from here too
```

Now, the `if` condition is not necessary when you want to run the module - those
lines in the `if` block will be executed anyway. It is however used to _prevent_
some lines from being executed when you import the file as a module.

Please also note that module imports are typically _silent_, so the `else:`
condition with a printout would not exist in real life.


[stl]: https://docs.python.org/2/library/index.html
[pep8-import]: https://www.python.org/dev/peps/pep-0008/#imports
[pep8-modulenames]: https://www.python.org/dev/peps/pep-0008/#package-and-module-names
[pypi]: https://pypi.org/
[anaconda]: https://www.anaconda.com/distribution/
[lcg_virtualenv]: https://gitlab.cern.ch/cburr/lcg_virtualenv/
