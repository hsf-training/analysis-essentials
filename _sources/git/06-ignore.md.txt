# Ignoring Things

{% objectives "Learning Objectives" %}

- Configure Git to ignore specific files.
- Explain why ignoring files can be useful.

{% endobjectives %}

What if we have files that we do not want Git to track for us,
like backup files created by our editor
or intermediate files created during data analysis.
Let's create a few dummy files:

```bash
$ mkdir results
$ touch a.dat b.dat c.dat results/a.out results/b.out
```

and see what Git says:

```bash
$ git status
```
```
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.dat
	b.dat
	c.dat
	results/
nothing added to commit but untracked files present (use "git add" to track)
```

Putting these files under version control would be a waste of disk space.
What's worse,
having them all listed could distract us from changes that actually matter,
so let's tell Git to ignore them.

We do this by creating a file in the root directory of our project called `.gitignore`:

```bash
$ nano .gitignore
$ cat .gitignore
```
```
*.dat
results/
```

These patterns tell Git to ignore any file whose name ends in `.dat`
and everything in the `results` directory.
(If any of these files were already being tracked,
Git would continue to track them.)

Once we have created this file,
the output of `git status` is much cleaner:

```bash
$ git status
```
```
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
nothing added to commit but untracked files present (use "git add" to track)
```

The only thing Git notices now is the newly-created `.gitignore` file.
You might think we wouldn't want to track it,
but everyone we're sharing our repository with will probably want to ignore
the same things that we're ignoring.
Let's add and commit `.gitignore`:

```bash
$ git add .gitignore
$ git commit -m "Add the ignore file"
$ git status
```
```
# On branch master
nothing to commit, working directory clean
```

As a bonus, using `.gitignore` helps us avoid accidentally adding to the
repository files that we don't want to track:

```bash
$ git add a.dat
```
```
The following paths are ignored by one of your .gitignore files:
a.dat
Use -f if you really want to add them.
```

If we really want to override our ignore settings,
we can use `git add -f` to force Git to add something. For example,
`git add -f a.dat`.
We can also always see the status of ignored files if we want:

```bash
$ git status --ignored
```
```
On branch master
Ignored files:
 (use "git add -f <file>..." to include in what will be committed)

        a.dat
        b.dat
        c.dat
        results/

nothing to commit, working directory clean
```

{% challenge "Ignoring Nested Files" %}


Given a directory structure that looks like:

```
results/data
results/plots
```

How would you ignore only `results/plots` and not `results/data`?

{% solution "Solution" %}


As with most programming issues, there are a few ways that you
could solve this. If you only want to ignore the contents of
`results/plots`, you can change your `.gitignore` to ignore
only the `/plots/` subfolder by adding the following line to
your .gitignore:

`results/plots/`

If, instead, you want to ignore everything in `/results/`, but wanted to track
`results/data`, then you can add `results/` to your .gitignore
and create an exception for the `results/data/` folder.
The next challenge will cover this type of solution.

Sometimes the `**` pattern comes in handy, too, which matches
multiple directory levels. E.g. `**/results/plots/*` would make git ignore
the `results/plots` directory in any root directory.

{% endsolution %}

{% endchallenge %}

{% challenge "Including Specific Files" %}


How would you ignore all `.data` files in your root directory except for
`final.data`?
Hint: Find out what `!` (the exclamation point operator) does

{% solution "Solution" %}


You would add the following two lines to your .gitignore:

```
*.data           # ignore all data files
!final.data      # except final.data
```

The exclamation point operator will include a previously excluded entry.

{% endsolution %}

{% endchallenge %}

{% challenge "Ignoring all data Files in a Directory" %}


Given a directory structure that looks like:

```
results/data/position/gps/a.data
results/data/position/gps/b.data
results/data/position/gps/c.data
results/data/position/gps/info.txt
results/plots
```

What's the shortest `.gitignore` rule you could write to ignore all `.data`
files in `result/data/position/gps`? Do not ignore the `info.txt`.

{% solution "Solution" %}


Appending `results/data/position/gps/*.data` will match every file in
`results/data/position/gps` that ends with `.data`.  The file
`results/data/position/gps/info.txt` will not be ignored.

{% endsolution %}

{% endchallenge %}

{% challenge "The Order of Rules" %}


Given a `.gitignore` file with the following contents:

```
*.data
!*.data
```

What will be the result?

{% solution "Solution" %}

The `!` modifier will negate an entry from a previously defined ignore pattern.
Because the `!*.data` entry negates all of the previous `.data` files in the
`.gitignore`, none of them will be ignored, and all `.data` files will be
tracked.

{% endsolution %}

{% endchallenge %}

{% challenge "Log Files" %}


You wrote a script that creates many intermediate log-files of the form `log_01`, `log_02`, `log_03`, etc.
You want to keep them but you do not want to track them through `git`.

1. Write **one** `.gitignore` entry that excludes files of the form `log_01`, `log_02`, etc.

2. Test your "ignore pattern" by creating some dummy files of the form `log_01`, etc.

3. You find that the file `log_01` is very important after all, add it to the tracked files without changing the `.gitignore` again.

4. Discuss with your neighbor what other types of files could reside in your directory that you do not want to track and thus would exclude via `.gitignore`.

{% solution "Solution" %}


1. append either `log_*`  or  `log*`  as a new entry in your .gitignore
3. track `log_01` using   `git add -f log_01`

{% endsolution %}

{% endchallenge %}


{% keypoints "Key Points" %}

- The `.gitignore` file tells Git what files to ignore.

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation 
{% endright %}
