## Motivation

[![Final.doc](http://www.phdcomics.com/comics/archive/phd101212s.gif)](http://www.phdcomics.com/comics/archive.php?comicid=1531)

Does the situation depicted in this PhD comic look anything familiar to you?
What the student in this comic clearly needs (apart from some LaTeX lessons) is
a version control system! Such a system keeps a history of a project in a very
non-intrusive way. The user only sees the current state of the project in their
filesystem but all changes are versioned such that previous version are easily
accessible. This reduces the need for ridiculous `_version5.23_final` filename
appendices.

Another common challenge that every physics student has to face in their time
at university is collaborative work with fellow students. Let's take a lab
course for example: You gather data, analyse it, and write a report about your
findings. There's a lot to be versioned: your data (although it will not change
after it's been recorded), your analysis programs, and the LaTeX source of your
report. How do you collaborate? Do you exchange files by email?

![Exchanging files via mail](/img/mail.png)

As you can probably imagine, this is a very inconvenient solution. Changes have
to be merged by hand which takes up time and puts you at the risk of forgetting
something or overriding it by accident. If you want to go back in time, you have
to dig through your email archives. In some cases, if you overwrote local
changes, you might not even be able to get them back.

So how about Dropbox (or any other file synchronisation service)? At least they
offer a very convenient way to share files while integrating nicely into your
file system.

![Exchanging files via Dropbox](/img/dropbox.png)

While the integration with your file system is very convenient, the automatic
synchronisation is a problem: While you are working on a file, it might change
in the background leaving you with conflicting versions that again you will have
to merge manually.

Enter: Git. It is a (source code) version control system that was originally
developed by Linus Torvalds to keep track of the development on the Linux
kernel. It has some dramatic advantages over the previously described methods:

 * A (commented) record of your work is kept
 * It allows you to jump back to a previous state
 * _Most_ changes can be merged automatically
 * It can also function as a backup system

All this comes with a command line interface that unfortunately takes some
getting used to. But this is what we are here for. :)

_Note_: The two schematics on this page come from a course held at TU Dortmund
University. You can find the material (in German) online at
[toolbox.pep-dortmund.org](http://toolbox.pep-dortmund.org).

--- 

### Exercises

 1. Make sure Git is installed on your system by running `git --version`. The
    output should look somewhat like the following: `git version 2.6.2`. If it
    is not installed, follow the instructions on the prerequisites pages.
 2. Think about situations in your (academic) life where Git would have been
    useful.
