# Git Command Reference

This page collects the Git commands used in this lesson, grouped by task, as a
quick reminder once you have worked through the lessons. Each group links to
the lesson where the commands are explained. For the full details of any
command, run `git <command> --help`, or `git <command> -h` for a short summary.
At the end, a [glossary](#glossary) explains the terms that are easy to mix up.

## Setting up

See [Setting Up Git](02-setup.md).

* `git config --global user.name "Your Name"`: set the name recorded in your
  commits.
* `git config --global user.email "you@example.org"`: set the email recorded in
  your commits.
* `git config --global init.defaultBranch main`: call the first branch of new
  repositories `main`.
* `git config --global core.editor "nano -w"`: choose the editor Git opens, for
  example for commit messages.
* `git config --global pull.rebase false`: make `git pull` combine histories
  with a merge.
* `git config --list`: show all your settings.

## Starting a repository

See [Creating a Repository](03-create.md) and
[Sharing a Repository with Others](09-share.md).

* `git init`: turn the current directory into a Git repository.
* `git clone <url>`: download a copy of a remote repository, including its
  whole history.

## Recording changes

See [Tracking Changes](04-changes.md) and [Ignoring Things](06-ignore.md).

* `git status`: show which files have changed, and which changes are staged.
* `git add <file>`: stage changes to a file for the next commit.
* `git add -p <file>`: choose which parts of a file's changes to stage.
* `git commit -m "Message"`: record the staged changes as a new commit.
* `git commit --amend`: fix the last commit (only if it has not been pushed).
* `git rm --cached <file>`: stop tracking a file, without deleting it.
* `.gitignore`: a file listing patterns of files that Git should ignore.

## Looking at history

See [Tracking Changes](04-changes.md) and [Exploring History](05-history.md).

* `git log`: list the commits, most recent first.
* `git log --oneline --graph --all`: a compact view of the history of all
  branches.
* `git log --patch <file>`: show the commits that changed a file, with their
  changes.
* `git diff`: show changes that have not been staged yet.
* `git diff --staged`: show changes that are staged for the next commit.
* `git diff <commit> <file>`: compare a file with its version in an earlier
  commit.
* `git show <commit>`: show the changes and message of one commit.
* `HEAD`, `HEAD~1`, `HEAD~2`, ...: the latest commit, the one before it, and so
  on; they can be used wherever a commit identifier is expected.

## Undoing things

See [Exploring History](05-history.md).

* `git restore <file>`: discard changes to a file that have not been staged.
* `git restore --staged <file>`: unstage a file, keeping the changes.
* `git restore --source=<commit> <file>`: get a file back as it was in an
  earlier commit.
* `git revert <commit>`: create a new commit that undoes an earlier one.
* `git reset --hard <commit>`: move the branch back to an earlier commit,
  discarding everything after it (only for commits that have not been pushed).
* `git reflog`: list where `HEAD` has recently been, to recover lost commits.

## Branches and tags

See [Branching and Merging](07-branches.md).

* `git branch`: list the branches; the current one is marked with `*`.
* `git switch -c <branch>`: create a new branch and switch to it.
* `git switch <branch>`: switch to another branch.
* `git switch --detach <commit>`: look at the whole project at an earlier
  commit.
* `git merge <branch>`: merge another branch into the current one.
* `git branch -d <branch>`: delete a branch that has been merged.
* `git stash` and `git stash pop`: put uncommitted changes aside, and bring
  them back.
* `git tag -a v1.0 -m "Message"`: mark the current commit with a tag.

## Working with remotes

See [Remotes in CERN GitLab](08-gitlab.md),
[Sharing a Repository with Others](09-share.md) and
[Collaborating with Pull Requests](11-pullrequests.md).

* `git remote add <name> <url>`: connect a remote repository under a short name,
  usually `origin`.
* `git remote -v`: list the remotes and their URLs.
* `git push -u origin <branch>`: push a branch for the first time, and remember
  where it goes.
* `git push`: send new commits to the remote.
* `git push origin <tag>`: send a tag to the remote.
* `git pull`: download new commits from the remote and merge them into the
  current branch.
* `git fetch`: download new commits from the remote without merging them.

## Resolving conflicts

See [Conflicts](12-conflict.md).

* Edit the file to remove the `<<<<<<<`, `=======` and `>>>>>>>` markers, then
  `git add <file>` and `git commit` to finish the merge.
* `git merge --abort`: give up on a merge and go back to how things were.
* `git restore --ours <file>` or `git restore --theirs <file>`: keep one side of
  a conflict, for example for a binary file.

## Glossary

* **Artefact**: a file produced by a CI job and kept after the job has
  finished, so that it can be downloaded or used by later jobs.
  ([Continuous Integration](13-ci.md))
* **Branch**: an independent line of development. Technically, a label that
  points at a commit and moves forward with every new commit made on it.
  ([Branching and Merging](07-branches.md))
* **CI (continuous integration)**: running tasks such as tests automatically
  every time commits are pushed. On GitLab, the tasks are *jobs*, grouped in a
  *pipeline* and run on machines called *runners*.
  ([Continuous Integration](13-ci.md))
* **Clone**: a complete copy of a repository, including its whole history,
  usually on your own computer; made with `git clone`.
  ([Sharing a Repository with Others](09-share.md))
* **Commit**: a snapshot of the project recorded in its history, together
  with a message, the author, the date and a unique identifier.
  ([Tracking Changes](04-changes.md))
* **Commit identifier** (or *hash*): the unique 40-character code of a
  commit, such as `f22b25e3233b4645dabd0d81e651fe074bd8e73b`. The first 7
  characters are usually enough to refer to it.
  ([Exploring History](05-history.md))
* **Conflict**: what happens when two changes to the same lines cannot be
  combined automatically, and Git asks you to decide what the result should be.
  ([Conflicts](12-conflict.md))
* **Detached HEAD**: the state in which `HEAD` points directly at a commit
  rather than at a branch, for example after `git switch --detach`.
  ([Exploring History](05-history.md))
* **Fast-forward**: a merge in which Git only needs to move the branch label
  forward, without creating a new commit. ([Branching and Merging](07-branches.md))
* **Fetch**: downloading new commits from a remote without merging them into
  your own work; done with `git fetch`.
  ([Sharing a Repository with Others](09-share.md))
* **Fork**: your own copy of someone else's project on the hosting platform,
  which you can push to. ([Collaborating with Pull Requests](11-pullrequests.md))
* **HEAD**: where you currently are, normally the latest commit of the current
  branch. `HEAD~1` is the commit before it, `HEAD~2` the one before that, and
  so on. ([Exploring History](05-history.md))
* **Hosting platform**: a website, such as GitLab or GitHub, that stores
  repositories online and adds collaboration tools such as merge requests and
  issues. ([Remotes in CERN GitLab](08-gitlab.md))
* **Issue**: a numbered page on a hosting platform where a bug, an idea, a
  question or a task is described and discussed.
  ([Tracking Work with Issues](10-issues.md))
* **main**: the usual name of the default branch of a repository. Older
  repositories often call it `master`. ([Setting Up Git](02-setup.md))
* **Merge**: bringing the changes of one branch into another, with
  `git merge`. ([Branching and Merging](07-branches.md))
* **Merge commit**: a commit with two parents, created when a merge joins two
  lines of work that have both moved on. ([Branching and Merging](07-branches.md))
* **Merge request / pull request**: a proposal, made on the hosting platform,
  to merge the changes of a branch into a project, where they can be reviewed
  and discussed first. GitLab calls it a merge request, GitHub a pull request.
  ([Collaborating with Pull Requests](11-pullrequests.md))
* **origin**: the usual short name of the remote that a repository was cloned
  from, or first pushed to. ([Remotes in CERN GitLab](08-gitlab.md))
* **Pull**: downloading new commits from a remote and merging them into the
  current branch, with `git pull`. ([Remotes in CERN GitLab](08-gitlab.md))
* **Push**: sending your new commits to a remote, with `git push`.
  ([Remotes in CERN GitLab](08-gitlab.md))
* **Remote**: another copy of the repository, usually on a hosting platform,
  that you can push to and pull from. Each remote has a short name, such as
  `origin`. ([Remotes in CERN GitLab](08-gitlab.md))
* **Repository**: a project tracked by Git: its files together with their
  complete history, which Git stores in the hidden `.git` directory.
  ([Creating a Repository](03-create.md))
* **Staging area** (also called the *index*): where you gather, with
  `git add`, the changes that will go into the next commit.
  ([Tracking Changes](04-changes.md))
* **Tag**: a label that permanently marks one commit, such as a released
  version. ([Branching and Merging](07-branches.md))
* **Upstream**: the original repository that a fork was made from. For a
  branch, also the remote branch it is linked to, as set up by `git push -u`.
  ([Collaborating with Pull Requests](11-pullrequests.md))
* **Working directory** (also called the *working tree*): the files of the
  project as you see and edit them. ([Tracking Changes](04-changes.md))

## Getting help

* `git <command> -h`: a short summary of a command's options.
* `git <command> --help`: the full manual page of a command.
* The [Pro Git book](https://git-scm.com/book/en/v2), free online, covers
  everything in this lesson and much more.

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Original content
