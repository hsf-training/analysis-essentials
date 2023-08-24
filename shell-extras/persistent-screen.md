## Persistent screen or tmux session on lxplus

### Setting up password-less kerberos token

In order for the kerberos token to be refreshed automatically, it must be possible to do so without a password.
Therefore, we create a keytab (similar to a private ssh key) on lxplus using the keytab utility.

{% callout "The old way" %}

The former recipe was to start `ktutil`, then type the following three lines into the prompt and confirm the first two steps with your password.
```bash
add_entry -password -p USERNAME@CERN.CH -k 1 -e arcfour-hmac-md5
add_entry -password -p USERNAME@CERN.CH -k 1 -e aes256-cts
wkt USERNAME.keytab
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

### Making use of the keytab
This keytab file can now be used to obtain kerberos tokens without having to type a password:
```bash
kinit -k -t ~/private/$USER.keytab $USER@CERN.CH
```
where `-k` tells `kinit` to use a keytab file and `-t ~/private/$USER.keytab` where this keytab actually is.
### Using k5reauth to automatically refresh your kerberos token
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
