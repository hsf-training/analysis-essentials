# Setting Up Git

{% objectives "Learning Objectives" %}

- Configure `git` the first time it is used on a computer.
- Understand the meaning of the `--global` configuration flag.

{% endobjectives %}

When we use Git on a new computer for the first time,
we need to configure a few things. Below are a few examples
of configurations we will set as we get started with Git:

*   our name and email address,
*   the name of the first branch in new repositories,
*   what our preferred text editor is,
*   how Git should combine our work with other people's when we pull,
*   and that we want to use these settings globally (i.e. for every project)

On a command line, Git commands are written as `git verb`,
where `verb` is what we actually want to do. So here is how
Dracula sets up his new laptop:

```bash
$ git config --global user.name "Vlad Dracula"
$ git config --global user.email "vlad@tran.sylvan.ia"
```

Please use your own name and CERN/institutional email address instead of Dracula's. This user name and email will be associated with your subsequent Git activity,
which means that any changes pushed to
[GitHub](https://github.com/),
[BitBucket](https://bitbucket.org/),
[GitLab](https://gitlab.com/) or
another Git host server
in a later lesson will include this information.

{% discussion "Which email address should I use?" %}

`user.email` is not a login: it is just a label that Git writes into every
commit you make, and you can push your work whatever it says. Hosting
platforms use it to link each commit to an account, so that it shows your
name and profile picture. This only works if the email in the commit is one
of the addresses registered on your account there.

So use the email of the account where most of your work ends up, for example
your CERN email for CERN GitLab. If you also use a platform where your account
has a different address (say, a GitHub account with a personal email), you
can either:

* add your other email address to that account as well (GitHub and GitLab both
  allow several addresses per account), or
* use a different email for just one repository, by running the same command
  *without* `--global` inside it:

```bash
$ git config user.email "vlad@personal.example"
```

Also keep in mind that the email in a commit is visible to anyone who can see
the repository. If you would rather not publish your address in public
projects, GitHub gives you a private "noreply" address to use instead; see
[GitHub's documentation][git-privacy].

{% enddiscussion %}

{% discussion "What about color.ui?" %}

Older tutorials (including earlier versions of this one) also run
`git config --global color.ui "auto"` so that Git uses colours in its output.
Colours have been switched on by default since Git 1.8.4 (2013), so you no
longer need this setting.

{% enddiscussion %}

Dracula also tells Git to call the first *branch* of every new repository
`main` (we will learn what branches are in the lesson on
[branching and merging](07-branches.md)):

```bash
$ git config --global init.defaultBranch main
```

{% discussion "Why main and not master?" %}

For most of Git's history, the first branch of a new repository was always
called `master`. In 2020, many projects and companies decided to move away from
this name, mainly because of its association with "master/slave" terminology,
and because `main` simply describes the branch better: it is the main line of
work in the project. Git 2.28 (2020) added the `init.defaultBranch` setting so
that you can choose the name yourself, and GitHub (2020) and GitLab (2021) now
call the first branch of new repositories `main`.

You will still come across plenty of repositories, tutorials and Stack Overflow
answers that use `master`. Nothing else is different: wherever you see
`master`, the same commands work with that name instead of `main`. You can
check which branch you are on with `git status`, and rename a branch in your
own repository with `git branch -m master main`.

{% enddiscussion %}

{% discussion "Line endings (worth reading if you use Windows)" %}


As with other keys, when you hit the 'return' key on your keyboard,
your computer encodes this input.
For reasons that are long to explain, different operating systems
use different character(s) to represent the end of a line.
(You may also hear these referred to as newlines or line breaks.)
Because git uses these characters to compare files,
it may cause unexpected issues when editing a file on different machines.

You can change the way git recognizes and encodes line endings
using the 'core.autocrlf' command to 'git config'.
The following settings are recommended:

On macOS and Linux:

```bash
$ git config --global core.autocrlf input
```

And on Windows:

```bash
$ git config --global core.autocrlf true
```

You can read more about this issue
[on this GitHub page](https://docs.github.com/en/get-started/git-basics/configuring-git-to-handle-line-endings).

{% enddiscussion %}

Dracula also has to set his favourite text editor, which Git opens whenever it
needs him to write something longer, such as a commit message. Pick the line
for your editor:

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| nano               | `$ git config --global core.editor "nano -w"`    |
| Visual Studio Code | `$ git config --global core.editor "code --wait"` |
| vim                | `$ git config --global core.editor "vim"`   |
| emacs              | `$ git config --global core.editor "emacs"`   |

{% discussion "Other editors" %}

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| BBEdit (Mac, with command line tools) | `$ git config --global core.editor "edit -w"`    |
| Sublime Text (Mac) | `$ git config --global core.editor "subl -n -w"` |
| Sublime Text (Win) | `$ git config --global core.editor "'c:/program files/sublime text/sublime_text.exe' -w"` |
| Notepad++ (Win)    | `$ git config --global core.editor "'c:/program files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`|
| Kate (Linux)       | `$ git config --global core.editor "kate"`       |
| Gedit (Linux)      | `$ git config --global core.editor "gedit --wait --new-window"`   |

{% enddiscussion %}

It is possible to reconfigure the text editor for Git whenever you want to change it.

{% callout "Exiting Vim" %}


Note that `vim` is the default editor for many programs. If you haven't used `vim` before and wish to exit a session, type `Esc` then `:q!` and `Enter`.

{% endcallout %}

Finally, Dracula tells Git what to do when `git pull` finds that his copy and
the shared copy of a project have both changed. We will meet this situation in
the lesson on [conflicts](11-conflict.md); for now it is enough to know that
this setting makes Git combine the two histories with a *merge*, which is the
behaviour this lesson assumes:

```bash
$ git config --global pull.rebase false
```

Without this setting, recent versions of Git stop with the error
`fatal: Need to specify how to reconcile divergent branches.` instead.
(Git for Windows already sets this by default; running the command anyway does
no harm.)

The `git config` commands we just ran only need to be run once: the flag `--global` tells Git
to use the settings for every project, in your user account, on this computer.

You can check your settings at any time:

```bash
$ git config --list
```

You can change your configuration as many times as you want: just use the
same commands to choose another editor or update your email address.

{% callout "Git Help and Manual" %}


Always remember that if you forget a `git` command, you can access the list of commands by using `-h` and access the Git manual by using `--help` :

```bash
$ git config -h
$ git config --help
```

{% endcallout %}

[git-privacy]: https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address


{% keypoints "Key Points" %}

-   "Use `git config` to configure a user name, email address, editor, and other preferences once per machine."

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation 
{% endright %}
