# An introduction to Python

[Python][python] is a programming language. It’s widely used in the
scientific community due to the broad selection of feature-rich, actively 
maintained libraries. This means that a lot of software has already been 
written to solve problems common to our field, so you can concentrate on the 
interesting stuff!

In LHCb, Python is used for lots of things, particularly for writing files that 
make ntuples for you, but also for many analyses.
Unless you are absolutely _forced_ to use another language by external 
constraints, such as your fit program already being written in C++, we 
recommend using Python, even if you’re not comfortable with it right now. This 
is because there’s a large support group of other people who can help you with 
problems you might have down the line, and because we believe it’s the best 
tool, all in all, for data analysis.

## Aim of these lessons

There are already plenty of [superb guides][learn] on the Internet for learning 
Python, all of which will be more comprehensive than this one. This particular 
guide exists because it closely follows what we teach at the 
[Starterkit][starterkit], where we teach Python over the course of one day, and 
so only teaches you what you need to follow along in the lessons that are 
specific to high-energy physics.

We expect you to be familiar with at least one other programming language, so 
that you understand sentences like "we assign value 123 to variable `abc`" and 
"this is a function which accepts two arguments". You should also understand 
the basics of using a text editor, which you use to write code to a file 
somewhere, and then you can somehow run the contents using commands in your 
terminal to make stuff happen.

Sounds good? Then let’s get going!

[python]: https://www.python.org/
[starterkit]: https://lhcb.github.io/starterkit/
[learn]: https://www.google.com/search?q=learn+python

```eval_rst
.. toctree::
    :maxdepth: 3
    :includehidden:
    :caption: Contents:

    running.md
    operators.md
    numbers.md
    strings.md
    lists.md
    dictionaries.md
    conditions.md
    methods.md
    scripting.md
    modules.md
    learning.md
    first_histogram.md
    further_reading.md
```
