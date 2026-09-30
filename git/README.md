# Git

Git is a *version control system*: a tool that records the history of the
files in a project. With Git you can go back to any earlier version of your
work, see exactly what changed, when and why, try out ideas without fear of
breaking what already works, and combine your work with that of your
collaborators. It is free and open source, and it is by far the most widely
used version control system, for everything from analysis code and papers to
large software projects like ROOT or the software of the LHC experiments.

This lesson will teach you to use Git on your own computer to keep track of
your work, and then to collaborate with others through a shared repository.

{% callout "Git, GitLab and GitHub" %}

**Git** is the program that runs on your computer and keeps the history of your
project. **GitLab**, **GitHub** and similar services are websites that host
copies of Git repositories online, so that you can share them, and they add
collaboration tools on top, such as merge requests, issues and continuous
integration. CERN runs its own GitLab instance at
[gitlab.cern.ch](https://gitlab.cern.ch).

You can use Git entirely without any of these websites, and the first part of
this lesson does exactly that.

{% endcallout %}

[![XKCD about Git](https://imgs.xkcd.com/comics/git.png)](https://xkcd.com/1597/)

If this comic feels familiar, don't worry: by the end of this lesson you will
know what those commands actually do.

{% prereq "Before you start" %}

- **Git** installed on your computer, version 2.28 or newer. You can check with
  `git --version`; if you need to install or update it, see
  [git-scm.com](https://git-scm.com/downloads/). Git is already available on
  lxplus.
- **Some familiarity with the shell**: moving between directories and running
  commands. The [shell lesson](../shell/README.md) covers everything you need.
- For the collaboration part of the lesson: an account on
  [CERN GitLab](https://gitlab.cern.ch) (you can log in with your CERN
  computing account) or on [GitHub](https://github.com), with an SSH key added
  to it, as explained
  in [Remotes in CERN GitLab](08-gitlab.md).

{% endprereq %}

The lesson is organised in four parts, followed by a reference page:

**Part 1: Using Git on your own**

- [Automated Version Control](01-basics.md): what version control is and why
  it is worth using.
- [Setting Up Git](02-setup.md): configuring Git the first time you use it.
- [Creating a Repository](03-create.md): starting to track a project with Git.
- [Tracking Changes](04-changes.md): the modify-add-commit cycle and writing
  good commit messages.
- [Exploring History](05-history.md): comparing versions, restoring old files
  and undoing commits.
- [Ignoring Things](06-ignore.md): telling Git which files not to track.
- [Branching and Merging](07-branches.md): working on several things in
  parallel and combining them.

**Part 2: Collaborating with others**

- [Remotes in CERN GitLab](08-gitlab.md): putting your repository online and
  keeping it in sync.
- [Sharing a Repository with Others](09-share.md): cloning and working on a
  shared repository.
- [Tracking Work with Issues](10-issues.md): reporting bugs, planning work and
  discussing it next to the code.
- [Collaborating with Pull Requests](11-pullrequests.md): proposing changes
  through forks, branches and merge requests.
- [Conflicts](12-conflict.md): what happens when changes overlap, and how to
  resolve them.

**Part 3: Automation**

- [Continuous Integration](13-ci.md): running tests and other tasks
  automatically every time you push, with GitLab CI.

**Part 4: Sharing your research**

- [Open Science](14-open.md): how version control supports open and
  reproducible research.
- [Licensing](15-licensing.md): choosing a licence so that others can reuse
  your work.
- [Citation](16-citation.md): making your work easy to cite.

**Reference**

- [Git Command Reference](17-reference.md): all the commands from this
  lesson on one page, for quick lookup.

```eval_rst
.. toctree::
    :hidden:
  :maxdepth: 3
  :includehidden:
  :caption: Contents:

    01-basics.md
  02-setup.md
  03-create.md
  04-changes.md
  05-history.md
  06-ignore.md
  07-branches.md
  08-gitlab.md
  09-share.md
  10-issues.md
  11-pullrequests.md
  12-conflict.md
  13-ci.md
  14-open.md
  15-licensing.md
  16-citation.md
  17-reference.md
```
