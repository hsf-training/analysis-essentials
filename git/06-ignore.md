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
On branch main
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
On branch main
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
On branch main
nothing to commit, working tree clean
```

As a bonus, using `.gitignore` helps us avoid accidentally adding to the
repository files that we don't want to track:

```bash
$ git add a.dat
```
```
The following paths are ignored by one of your .gitignore files:
a.dat
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
```

If we really want to override our ignore settings,
we can use `git add -f` to force Git to add something. For example,
`git add -f a.dat`.
We can also always see the status of ignored files if we want:

```bash
$ git status --ignored
```
```
On branch main
Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
	a.dat
	b.dat
	c.dat
	results/

nothing to commit, working tree clean
```

{% callout "What to ignore in a physics analysis" %}

A good rule of thumb is to track the files that *produce* your results (code,
configuration, small inputs, documentation), and to ignore the files that can
be *regenerated* from them. In a typical analysis, a `.gitignore` might look
like this:

```
# Data and large outputs: keep them on EOS, CERNBox, etc. instead
*.root
*.h5
*.parquet

# Plots and logs made by the analysis scripts
plots/
*.log

# Compiled code and build directories
build/
*.o
*.so

# Python caches and Jupyter checkpoints
__pycache__/
.ipynb_checkpoints/
```

You don't have to start from scratch: GitHub maintains a
[collection of `.gitignore` templates](https://github.com/github/gitignore)
for many languages and tools, and both GitHub and GitLab offer to add one when
you create a new project.

Remember that `.gitignore` only affects files that are not tracked yet. If you
have already committed a file that should be ignored, tell Git to stop tracking
it (the file itself stays on your disk), then commit that change:

```bash
$ git rm --cached hist.root
```
```
rm 'hist.root'
```

{% endcallout %}

{% callout "Never commit secrets" %}

Passwords, access tokens, private SSH keys and grid certificates (such as the
`usercert.pem` and `userkey.pem` files in `~/.globus/`) must never go into a
repository. Everything you commit stays in the history, and once it is pushed,
anyone who can see the repository, or who has already cloned it, can read it.

* Keep secrets outside your project, for example in your home directory or in
  environment variables, and have your code read them from there.
* If a tool expects a file with credentials inside the project (a common name
  is `.env`), add that file to `.gitignore` *before* creating it.
* Before committing, check what you are about to commit with `git status` and
  `git diff --staged`.

If a secret does get pushed, **revoke it immediately**: delete the access
token on GitLab or GitHub, remove the SSH key from your account, or contact the
issuer of your certificate. Deleting the file, or even rewriting the history to
remove the commit, is not enough, because the secret may already have been
copied.

{% endcallout %}

{% discussion "A global ignore file for your own clutter" %}

Some files have nothing to do with a particular project, but are created by
your own tools: backup files from your editor (such as `*~` or `*.swp`), the
`.DS_Store` files that macOS creates, or settings folders like `.vscode/`.
Rather than adding them to the `.gitignore` of every project (where they would
only matter to you), you can list them once in a *global* ignore file, which
Git applies to all your repositories. By default this is the file
`~/.config/git/ignore`:

```bash
$ mkdir -p ~/.config/git
$ nano ~/.config/git/ignore
$ cat ~/.config/git/ignore
```
```
*~
*.swp
.DS_Store
.vscode/
```

{% enddiscussion %}

{% discussion "Large files and Git LFS" %}

Git keeps every version of every file forever, and every clone contains the
whole history. That is perfect for code, but a bad fit for large data files:
committing a few gigabytes of ROOT files makes the repository slow to clone for
everyone, and removing them later requires rewriting history. Hosting platforms
also set limits: GitHub, for example, warns about files larger than 50 MiB and
refuses files larger than 100 MiB.

So keep large data outside Git, for example on EOS or CERNBox, or publish it on
a data repository such as [Zenodo](https://zenodo.org), and commit the scripts
(or the instructions) that fetch it instead.

For moderately large binary files that really belong with the code, such as a
few reference files for tests, there is [Git LFS](https://git-lfs.com/) (Large
File Storage). It stores the content of the files you choose on a separate
server, and keeps only small pointer files in the repository:

```bash
$ git lfs install
$ git lfs track "*.root"
$ git add .gitattributes
```

After this, `*.root` files are added and committed as usual. Most hosting
platforms, including GitLab and GitHub, support Git LFS, usually with a storage
quota. Everyone who clones the repository needs Git LFS installed to get the
actual files.

{% enddiscussion %}

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
any number of directory levels. For example, `**/results/plots/` would make Git ignore
a `results/plots` directory wherever it appears in the repository, at any depth.

{% endsolution %}

{% endchallenge %}

{% challenge "Including Specific Files" %}


How would you ignore all `.data` files in your root directory except for
`final.data`?
Hint: Find out what `!` (the exclamation point operator) does

{% solution "Solution" %}


You would add the following two lines to your .gitignore:

```
# ignore all data files...
*.data
# ...except final.data
!final.data
```

The exclamation point operator will include a previously excluded entry.
Note that comments in a `.gitignore` file must be on their own line, starting
with `#`: a `#` placed after a pattern is treated as part of the pattern.

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

4. Discuss with your neighbour what other types of files could reside in your directory that you do not want to track and thus would exclude via `.gitignore`.

{% solution "Solution" %}


1. append either `log_*`  or  `log*`  as a new entry in your .gitignore
3. track `log_01` using   `git add -f log_01`

{% endsolution %}

{% endchallenge %}


{% keypoints "Key Points" %}

- The `.gitignore` file tells Git what files to ignore.
- Track the files that produce your results, and ignore the ones that can be regenerated, such as data files, plots and build outputs.
- `git rm --cached <file>` stops tracking a file that was committed by mistake, without deleting it.
- Keep large data files out of Git; use Git LFS only for moderately large files that belong with the code.
- Never commit passwords, tokens or private keys; if one is pushed by mistake, revoke it immediately.

{% endkeypoints %}

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation
