# Scripting

OK, so we’ve spent quite a long time in Python shells. But we can quit.
With IPython’s history we can only get back our work line-by-line. When we want to
persist what we’ve done, we write code to a file and then run the file.

Let’s create a file called `pizzaiolo.py`, and write a little python in it.

```python
import time

def make_pizza(*toppings):
    """Make a delicious pizza from the toppings."""
    print('Making pizza...')
    for topping in toppings:
        print('Adding {0}'.format(topping))
        time.sleep(1)
    print('Done!')
    return 'Pizza with toppings: {0}'.format(toppings)

pizza = make_pizza('cheese', 'olives')
```

To run it, we can run the `python` or `ipython` programs in our shell, passing
the filename as an argument.

```shell
$ python pizzaiolo.py
Making pizza...
Adding cheese
Done!
Adding olives
Done!
$ ipython pizzaiolo.py
Making pizza...
Adding cheese
Done!
Adding olives
Done!
```

We can enter an interactive shell after the script has run by including the
`-i` flag, in which we’ll have access to anything that was defined by the
script.

```shell
$ python -i pizzaiolo.py
Making pizza...
Adding cheese
Done!
Adding olives
Done!
>>> time
<module 'time' from '/usr/lib/python2.7/lib-dynload/time.so'>
>>> pizza
"Pizza with toppings: ('cheese', 'olives')"
>>> exit()

$ ipython -i pizzaiolo.py
Making pizza...
Adding cheese
Done!
Adding olives
Done!

In [1]: pizza
"Pizza with toppings: ('cheese', 'olives')"

In [2]: exit()

$
```

One of the most interesting things you can do in your own scripts is accept
arguments. Wouldn’t it be great if we could decide what toppings our pizza has
_from the command line_?

```shell
$ python pizzaiolo.py cheese broccoli
Making pizza...
Adding cheese
Done!
Adding olives
Done!
```

Of course, nothing’s changed because our script doesn’t know how to handle such
arguments. To add this, we use for example the `sys` module, which makes the command line
arguments available as the `argv` property. We can modify our script to print
this out, to get a feeling for what’s going on. We’ll comment out our method
call whilst we’re just playing around.

```python
import sys
import time

def make_pizza(*toppings):
    """Make a delicious pizza from the toppings."""
    print('Making pizza...')
    for topping in toppings:
        print('Adding {0}'.format(topping))
        time.sleep(1)
    print('Done!')
    return 'Pizza with toppings: {0}'.format(toppings)

print('sys.argv:', sys.argv)
# pizza = make_pizza('cheese', 'olives')
```

Then run it:

```shell
$ python pizzaiolo.py
sys.argv: ['pizzaiolo.py']
$ python pizzaiolo.py cheese broccoli
sys.argv: ['pizzaiolo.py', 'cheese', 'broccoli']
$ python pizzaiolo.py cheese broccoli --help --verbose
sys.argv: ['pizzaiolo.py', 'cheese', 'broccoli', '--help', '--verbose']
```

Awesome! `sys.argv` is just a list with one value per argument (arguments on
the command line are separate by spaces). The first value is always the name of
the script that we run.

So, let’s use the command line arguments in our script.

```python
# print('sys.argv:', sys.argv)
toppings = sys.argv[1:]
pizza = make_pizza(*toppings)
```

And then run it:

```shell
$ python pizzaiolo.py cheese broccoli
Making pizza...
Adding cheese
Done!
Adding broccoli
Done!
```

Super cool. Now we could decide to add some flags that modify the behaviour of
our program. We might like the `--help` flag to print a help message and exit,
without actually making pizza, and a `--verbose` flag to enable printing more
information.

```python
arguments = sys.argv[1:]

if '--help' in arguments:
    print('Make a pizza.')
    print('Usage: pizzaiolo.py topping1 topping2 ...')
    sys.exit()

if '--verbose' in arguments:
    verbose = True
    # We don't want the flag passed as a topping!
    arguments.remove('--verbose')
else:
    verbose = False

if verbose:
    print('About to call make_pizza')
pizza = make_pizza(*arguments)
if verbose:
    print('Finished')
```

Let’s try running it.

```shell
$ python pizzaiolo.py cheese broccoli
Making pizza...
Adding cheese
Done!
Adding broccoli
Done!
$ python pizzaiolo.py cheese broccoli --help
Make a pizza.
Usage: pizzaiolo.py topping1 topping2 ...
$ python pizzaiolo.py cheese broccoli --verbose
About to call make_pizza
Making pizza...
Adding cheese
Done!
Adding broccoli
Done!
Finished
```

Great, everything seems to work.

## argparse

The [`argparse` module][argparse] comes as part of the Python standard library,
and allows us to define what arguments our scripts accept much more easily
than what we’ve shown. Under the hood, it just inspects `sys.argv` in exactly
the same way as we’ve done, but it takes care of things like validation for us.

```
import argparse
import sys
import time


def make_pizza(*toppings):
    """Make a delicious pizza from the toppings."""
    print('Making pizza...')
    for topping in toppings:
        print('Adding {0}'.format(topping))
        time.sleep(1)
    print('Done!')
    return 'Pizza with toppings: {0}'.format(toppings)


parser = argparse.ArgumentParser(description='Make a pizza')
parser.add_argument('toppings', nargs='+',
                    help='Toppings to put on the pizza.')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Print more information whilst making.')
arguments = parser.parse_args()

if arguments.verbose:
    print('About to call make_pizza')
make_pizza(*arguments.toppings)
if arguments.verbose:
    print ('Finished')
```

We say that we want an argument, that we will refer to as `toppings` in the
code, that can be specified multiple times `nargs='+'`, and a flag called
`--verbose`. We ask that that flag can also be specified using the `-v`
shorthand.

Let’s start by asking for help again.

```shell
$ python pizzaiolo.py --help
usage: simple.py [-h] [--verbose] toppings [toppings ...]

Make a pizza

positional arguments:
  toppings       Toppings to put on the pizza.

optional arguments:
  -h, --help     show this help message and exit
  --verbose, -v  Print more information whilst making.
```

Woah, nice! We didn’t even tell `argparse` to have a `--help` flag, but we have
one automatically. (`argparse` will also add `-h` as an alias for `--help`.)

Let's now prepare the traditional Pizza Margherita.

```shell
$ python pizzaiolo.py 'tomato sauce' 'buffalo mozzarella' --verbose
About to call make_pizza
Making pizza...
Adding tomato sauce
Done!
Adding buffalo mozzarella
Done!
Finished
```

The same result is obtained, but more cleanly expressed and with fewer lines of code!

[argparse]: https://docs.python.org/2/library/argparse.html
