# Running Python

To start using Python, we need access to the `python` program in a terminal.
The version installed on lxplus is 2.6.6, which is very old. However, we can get
a newer version along with various useful packages
(see details on the [LCG stacks][lcg_stack]) by setting up an LCG environment:

```bash
$ source /cvmfs/sft.cern.ch/lcg/views/setupViews.sh LCG_93 x86_64-slc6-gcc62-opt
```

If you have a computer running MacOS or some Linux distribution, it will have
come will Python pre-installed. Either way, a simple way to get Python on your 
computer is to install [Anaconda][anaconda].

{% callout "Python 3?" %}
You might see material that talks about Python 3. Like a lot of other software, 
Python is regularly updated and groups batches of updates, including bug fixes 
and new features, into versions. The interesting thing about Python 3 is that 
it isn’t _backwards compatible_ with Python 2. This means that code that works 
when run with version 2 of Python may not necessarily work when run with 
version 3. Python 2 was around for a long time, and so the process of migrating to Python 3 has been slow, which is why so many people talk about it.

Indeed, LHCb software is not compatible with Python 3, and so we use Python 2 
in these lessons. In general, and out in the real world, Python 3 is preferred 
as it receives the most focus from the people who make Python. If you’re 
starting a new project, and don’t have to use LHCb software, consider trying to 
use Python 3. You can install both Python 2 and Python 3 using 
[Anaconda](https://www.anaconda.com/download/).
{% endcallout %}

Python is a very user-friendly language. If you’re used to having to compile 
your code, this might seem refreshing:

```bash
$ python
Python 2.7.13 (default, Dec  5 2017, 19:29:24)
[GCC 6.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 3.14
>>> print a + 1
4.14
>>> a
3.14
```

Woah! What just happened?

1. We started an _interactive Python session_, also known as a Python _shell_, 
   by executing the `python` command;
2. We typed a line of code, `a = 3.14`, and hit enter;
3. We typed another line of code, `print a`, and hit enter;
4. The value `3.14` was printed to the terminal.

This interactive session is sometimes called a REPL: a **R**ead **E**valuate 
**P**rint **L**oop. This is just like `bash`, where you type your command, run 
it, see the results, and can then type the next line. Sometimes there are no 
results, so you don’t see anything being printed (just like running the `true` 
command in `bash`).

You can leave the session by running `exit()`, or by using the `Ctrl-d` key 
combination.

Everything that can be done in Python can be done in an interactive session; 
it’s a great way to experiment. An enhanced version of this session is called 
[IPython][ipython].

```bash
$ ipython

Python 2.7.13 (default, Dec  5 2017, 19:29:24)
Type "copyright", "credits" or "license" for more information.

IPython 5.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print 1 + 3
4
```

There are a few advantages to using `ipython` over `python`:

* Command **history persists** across sessions. This also works just like 
  `bash`: hit the up arrow to go through lines you typed in the past. If you 
  already have part of a command typed out, and _then_ hit the up arrow, 
  IPython will only show you lines that started with the same characters.
* **Autocompletion**. If you hit the `tab` key whilst typing something, IPython 
  will present you with a list of things that match the word you’re in the 
  middle of typing.

```python
In [2]: abc_my_var = 3.14

In [3]: abc_<tab>

In [4]: import math

In [5]: math.s<tab>
              math.sin
              math.sinh
              math.sqrt
```

* Easily **run shell commands** by starting your line with an exclamation mark.

```python
In [6]: !cal
    October 2017
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

* Access the **value of the last line** with the special `_` variable

```python
In [7]: 3.14 + 4.13
7.27

In [8]: _
7.27
```

Your best friend in a (I)Python shell is the `help` method. If you want more 
information on something, just ask for `help`!

```python
In [7]: help()

In [8]: help(math)
```

You can see what names are available to you by using the `dir` method.

```python
In [9]: dir()

In [10]: __doc__
'Automatically created module for IPython interactive environment'

In [11]: dir(math)
['__doc__',
 ...
 'sin',
 ...
 'trunc']
```

[anaconda]: https://www.anaconda.com/download/
[ipython]: https://ipython.org/
[lcg_stack]: http://lcginfo.cern.ch/