# Creating a Repository

{% objectives "Learning Objectives" %}

- Create a local Git repository.

{% endobjectives %}

Once Git is configured,
we can start using it.
Let's create a directory for our work and then move into that directory:

```bash
$ mkdir planets
$ cd planets
```

Then we tell Git to make `planets` a repository—a place where
Git can store versions of our files:

```bash
$ git init
```

If we use `ls` to show the directory's contents,
it appears that nothing has changed:

```bash
$ ls
```

But if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory within `planets` called `.git`:

```bash
$ ls -a
.	..	.git
```

Git stores information about the project in this special sub-directory.
If we ever delete it,
we will lose the project's history.

We can check that everything is set up correctly
by asking Git to tell us the status of our project:

```bash
$ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```

{% challenge "Places to Create Git Repositories" %}


Dracula starts a new project, `moons`, related to his `planets` project.
Despite Wolfman's concerns, he enters the following sequence of commands to
create one Git repository inside another:

```bash
$ cd             # return to home directory
$ mkdir planets  # make a new directory planets
$ cd planets     # go into planets
$ git init       # make the planets directory a Git repository
$ mkdir moons    # make a sub-directory planets/moons
$ cd moons       # go into planets/moons
$ git init       # make the moons sub-directory a Git repository
```

Why is it a bad idea to do this? (Notice here that the `planets` project is now also tracking the entire `moons` repository.)
How can Dracula undo his last `git init`?

{% solution "Solution" %}


Git repositories can interfere with each other if they are "nested" in the
directory of another: the outer repository will try to version-control
the inner repository. Therefore, it's best to create each new Git
repository in a separate directory. To be sure that there is no conflicting
repository in the directory, check the output of `git status`. If it looks
like the following, you are good to go to create a new repository as shown
above:

```bash
$ git status
```
```
fatal: Not a git repository (or any of the parent directories): .git
```

Note that we can track files in directories within a Git:

```bash
$ touch moon phobos deimos titan    # create moon files
$ cd ..                             # return to planets directory
$ ls moons                          # list contents of the moons directory
$ git add moons/*                   # add all contents of planets/moons
$ git status                        # show moons files in staging area
$ git commit -m "add moon files"    # commit planets/moons to planets Git repository
```

Similarly, we can ignore (as discussed later) entire directories, such as the `moons` directory:

```bash
$ nano .gitignore # open the .gitignore file in the texteditor to add the moons directory
$ cat .gitignore # if you run cat afterwards, it should look like this:
moons
```

To recover from this little mistake, Dracula can just remove the `.git`
folder in the moons subdirectory. To do so he can run the following command from inside the 'moons' directory:

```bash
$ rm -rf moons/.git
```

But be careful! Running this command in the wrong directory, will remove
the entire git-history of a project you might wanted to keep. Therefore, always check your current directory using the
command `pwd`.

{% endsolution %}

{% endchallenge %}


{% keypoints "Key Points" %}

- `git init` initializes a repository.

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation 
{% endright %}
