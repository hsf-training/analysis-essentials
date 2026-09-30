# Git Command Reference

This page collects the Git commands used in this lesson, grouped by task, as a
quick reminder once you have worked through the lessons. Each group links to
the lesson where the commands are explained. For the full details of any
command, run `git <command> --help`, or `git <command> -h` for a short summary.

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

## Getting help

* `git <command> -h`: a short summary of a command's options.
* `git <command> --help`: the full manual page of a command.
* The [Pro Git book](https://git-scm.com/book/en/v2), free online, covers
  everything in this lesson and much more.

{% right %}
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Original
content
{% endright %}
