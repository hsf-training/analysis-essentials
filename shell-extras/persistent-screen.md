## Persistent screen or tmux session on lxplus

### Setting up password-less kerberos token

In order for the kerberos token to be refreshed automatically, it must be possible to do so without a password.
Therefore, we create a keytab (similar to a private ssh key) on lxplus using the keytab utility. After starting it by typing `ktutil`, type the following three lines into the prompt and confirm the first two steps with your password.
```bash
add_entry -password -p USERNAME@CERN.CH -k 1 -e arcfour-hmac-md5
add_entry -password -p USERNAME@CERN.CH -k 1 -e aes256-cts
wkt USERNAME.keytab
```
and close the `ktutil` prompt with `Ctrl+D`.
This will create a file called USERNAME.keytab in the current directory. It is strongly recommended to store this file in a directory to which only you have access as anyone who obtains a copy of this file can use it to obtain tokens in your name.
### Making use of the keytab
This keytab file can now be used to obtain kerberos tokens without having to type a password:
```bash
kinit -k -t USERNAME.keytab USERNAME@CERN.CH
```
where `-k` tells `kinit` to use a keytab file and `-t USERNAME.keytab` where this keytab actually is.
### Using k5reauth to automatically refresh your kerberos token
To create a permanent session of `tmux` or `screen`, the `k5reauth` command is used, which by default creates a new shell and attaches it as a child to itself and keeps renewing the kerberos token for its children. `k5reauth` can start processes other than a new shell by specifying the program you want to start as an argument
```bash
k5reauth -f -i 3600 -p .... -- <command>
```
To start `screen` or `tmux` run:
```bash
k5reauth -f -i 3600 -p USERNAME -k /path/to/USERNAME.keytab -- tmux new-session -s NAME
```
which will create a `tmux` session whose kerberos token is refreshed automatically every 3600 seconds. When attaching back to the process, a simple
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
        k5reauth -f -i 3600 -p USERNAME -k /path/to/USERNAME.keytab -- tmux new-session
    else #pass the argument as the tmux session name
        k5reauth -f -i 3600 -p USERNAME -k /path/to/USERNAME.keytab -- tmux new-session -s $1
    fi
}
```
You could then start a tmux session named “Test” using
```bash
ktmux Test
```
