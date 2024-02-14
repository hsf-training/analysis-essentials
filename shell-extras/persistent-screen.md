## Persistent screen or tmux session on lxplus

The behavior of screen and tmux on lxplus depends on which version of lxplus you are using.

### lxplus7

If you are using lxplus7, you must manually initialize a kerberos token to give the screen or tmux session permission to continue to write even after you log out.
This requires jumping through a few hoops, described below.

{% callout "Alternative for lxplus7" %}

If you prefer, you can follow the instructions in [KB0002408](https://cern.service-now.com/service-portal?id=kb_article&n=KB0002408), instead of those below.

{% endcallout %}

#### Setting up password-less kerberos token on lxplus7

In order for the kerberos token to be refreshed automatically, it must be possible to do so without a password.
Therefore, we create a keytab (similar to a private ssh key) on lxplus using the provided `cern-get-keytab` utility. Note it will prompt for your password, in order to generate the keytab.

{% callout "The old way" %}

The former recipe was to start `ktutil`, then type the following three lines into the prompt and confirm the first two steps with your password.
```bash
cern-get-keytab --user USERNAME --keytab USERNAME.keytab
```
and close the `ktutil` prompt with `Ctrl+D`.
This would create a file called USERNAME.keytab in the current directory.
Since [OTG0077802](https://cern.service-now.com/service-portal?id=outage&n=OTG0077802), this recipe no longer works, and you will have to create a new keytab using these updated instructions.

{% endcallout %}

CERN [provides](https://cern.service-now.com/service-portal?id=kb_article&n=KB0003405) a shortcut command on lxplus9 (it will not work properly on lxplus7, though you can still use the created keytab from lxplus7 or lxplus8), which will prompt you for your password:
```bash
cern-get-keytab --keytab ~/private/$USER.keytab --user --login $USER
```
This will create a file called `$USER.keytab` (where `$USER` is your username) in the directory `~/private/`. By default, on lxplus, only `$USER` has access to this directory; anyone who can access this file can use it to obtain tokens in your name, so be careful if you decide to move it to a different directory.

To test if the keytab works:
```bash
kdestroy; kinit -kt ~/private/$USER.keytab $USER; klist
```
This should display information about a ticket cache.

#### Making use of the keytab on lxplus7
This keytab file can now be used to obtain kerberos tokens without having to type a password:
```bash
kinit -k -t ~/private/$USER.keytab $USER@CERN.CH
```
where `-k` tells `kinit` to use a keytab file and `-t ~/private/$USER.keytab` where this keytab actually is.

#### Using k5reauth to automatically refresh your kerberos token on lxplus7
To create a permanent session of `tmux` or `screen`, the `k5reauth` command is used, which by default creates a new shell and attaches it as a child to itself and keeps renewing the kerberos token for its children. `k5reauth` can start processes other than a new shell by specifying the program you want to start as an argument
```bash
k5reauth -f -i 3600 -p .... -- <command>
```
To start `screen` or `tmux` run:
```bash
k5reauth -f -i 3600 -p $USER -k ~/private/$USER.keytab -- tmux new-session -s NAME
```
which will create a `tmux` session whose kerberos token is refreshed automatically every 3600 seconds.

This is not enough to actually get a persistent session. From inside the `tmux` session, run:
```bash
kinit $USER@CERN.CH
```
Make a note of which lxplus machine you are on. Then, detach the session (<kbd>^B D</kbd> by default) and log out. Finally, log back into the same machine, attach the session using `tmux a`, and run `kinit $USER@CERN.CH` again.
Now, you should have a persistent tmux session on the machine you logged in to.

When attaching back to the process in the future, a simple
```bash
tmux attach-session -t NAME
```
or
```bash
tmux a
```
(if you want to attach the most recently used session) is sufficient.

You will almost certainly want to use an alias or function to access this command. One way to do that would be to copy and paste the following into your `~/.bashrc` (if you use bash):
```bash
ktmux(){
    if [[ -z "$1" ]]; then #if no argument passed
        k5reauth -f -i 3600 -p $USER -k ~/private/$USER.keytab -- tmux new-session
    else #pass the argument as the tmux session name
        k5reauth -f -i 3600 -p $USER -k ~/private/$USER.keytab -- tmux new-session -s $1
    fi
}
```
You could then start a tmux session named “Test” using
```bash
ktmux Test
```
Note that you will still have to follow the rest of the recipe (`kinit`, detach, log out, log in, attach, `kinit`) manually to get a persistent session.

### lxplus8

If you are on lxplus8, many of the above issues do not apply. You can simply create a screen or tmux session as normal; then, when you log back in to that node, it will still be there. You don't even have to initialize a kerberos token.

> This advice has not been tested for sessions lasting more than 24 hours.
> If you're worried, you can follow the recipe for lxplus7 or lxplus9.

### lxplus9

If you are on lxplus9, your screen or tmux session will be killed when you log out.
To avoid this, you must follow the recipe in [KB0008111](https://cern.service-now.com/service-portal?id=kb_article&n=KB0008111) to initialize the session:
```bash
systemctl --user start tmux.service
tmux a
```
This will auto-renew your kerberos ticket as well, obviating the need to call `kinit` or use keytabs.
The recipe for lxplus7 *will not work*.
