## Git-ing started
Before you can use Git, you need to configure it. This is necessary, as Git
will use your name and email address to reference the changes you made to a
project. Run the following commands in your terminal substituting your name and
email address accordingly:

```bash
git config --global user.name "Name Surname"
git config --global user.email "name.surname@cern.ch"
```

You can also set other options like for example coloured output with the same
command:

```bash
git config --global color.ui auto
```

You can view all your settings by running `cat ~/.gitconfig`. You can also edit
this file by hand if you know what you're doing. Extensive documentation can be
found on the `git-config` manpage (run `man git-config`) or in the [online
documentation](https://git-scm.com/docs/git-config).

---

### Excercises

 1. List the contents of your Git configuration. Make sure that your name and
    email address are set correctly.
 2. Git has a nice feature that can automatically correct commands if you made a
    typing error. Find out how to enable this option (and enable it if you want
    to).
