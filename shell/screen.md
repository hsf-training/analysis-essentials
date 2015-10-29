---
layout: page
title: First Steps in LHCb
subtitle: Using screen to keep things running
minutes: 10
---
> ## Learning Objectives {.objectives}
>
> * Create a new `screen` session
> * Disconnect from a `screen` session
> * Reconnect to an existing `screen` session
> * End an existing `screen` session
> * Handling of Kerberos tokens

Often we want to run a program for a long time on a computer we
connected to via `ssh`, like the `lxplus` machines. The `screen`
program allows you to keep programs running on the remote computer
even if you disconnect from it. For example when putting your laptop
to sleep or losing wifi.

Connect to `lxplus`:

~~~ {.bash}
$ ssh lxplus.cern.ch
~~~

You can start `screen` by simply typing its name:

~~~ {.bash}
$ screen
~~~

Once you do this it will look as if nothing has happened. However you
now have a fresh terminal inside what is refered to as a "screen
session". Let's type some commands that generate some output:

~~~ {.bash}
$ uptime
~~~
~~~ {.output}
 11:48:02 up 15 days, 20:36, 105 users,  load average: 2.26, 2.10, 3.16
~~~
~~~ {.bash}
$ date
~~~
~~~ {.output}
Thu Apr 16 11:48:32 CEST 2015
~~~

To disconnect from this session press `Ctrl-a d`. We are now back to
the terminal that we first started in. You can check that your
`screen` session is still running by typing `screen -list`, which will
list all active sessions:

~~~ {.bash}
$ screen -list
~~~
~~~ {.output}
There is a screen on:
      25593.pts-44.lxplus0234   (Detached)
1 Socket in /var/run/screen/S-thead.
~~~

To reconnect to the session you use `screen -rD`. When there is just
one session running (like now) then it will reconnect you to that
session. Try it and you should see the date and time output by the
`date` command we ran earlier.

When you have more than one session you need to provide the name of
the session as an argument to `screen -rD`. The name of the above
session is: `25593.pts-44.lxplus0234`. You can reconnect to it with:

~~~ {.bash}
$ screen -rD 25593.pts-44.lxplus0234
~~~

To end a `screen` session you are currently connected to, simply press
`Ctrl-d`. Just like you would to disconnect from a `ssh` session.

A `screen` session is tied to a specific computer. This means you need
to remember which computer you connected to. Even if your `screen`
session keeps running, you can only resume it from the same machine as
you started it.

When connecting to `lxplus` you are assigned to a random computer, but you can find out its name with `hostname`:

~~~ {.bash}
$ hostname
~~~
~~~ {.output}
lxplus0081.cern.ch
~~~

This tells you that the computer you are connected to is called
`lxplus0081.cern.ch`. Later on you can re-connect to exactly this
machine with:

~~~ {.bash}
$ ssh lxplus0081.cern.ch
~~~

Another complication are your kerberos tokens. These typically
expire as soon as you disconnect from a `lxplus` machine. This means
the program you left running inside the `screen` session will
suddenly not be able to write to any files in your home directory
anymore. This is particularly annoying if you are running `ganga`
in your screen session.

One way to stop your tokens from expiring is to type `kinit`
when you first start a new `screen` session. The tokens you get
this way will survive you disconnecting. However they will
expire after 24 hours, so you will have to type `kinit` again
to renew them if you leave `screen` running for longer than
24 hours.

```bash
$ screen
# now inside the screen session
$ kinit
```

> ## Finding lost screens {.callout}
>
> Once you start a `screen` session you need to remember which
> `lxplus` node it is running on. If you forget to note that down
> you can use the following little snippet to find any `screen`
> sessions running on `lxplus` nodes:
>
> ```bash
> for i in $(seq -f "%04g" 1 500); do
>  ssh -o ConnectTimeout=10 -o PreferredAuthentications=gssapi-with-mic,gssapi -o GSSAPIAuthentication=yes -o StrictHostKeyChecking=no -o LogLevel=quiet lxplus$i.cern.ch "(screen -list | head -1 | grep -q 'There is a screen on') && hostname && screen -list"
> done
> ```
> This will connect to the first 500 lxplus nodes in
> turn, checking if a `screen` session is running and if
> yes prints the hostname and output of `screen -list`.
 
> ## Using tabs in screen {.callout}
>
> Screen supports some features beyond detaching a session. A very useful feature is different sessions in tab pages, all within a single instance of `screen`. 
> In order to maximise the usefulness of this feature, you need to set the screen status bar. The simplest way to do this is by appending the following line to the file `~/.screenrc` (create it if it doesn't already exist):
> ```
> # Status lines
> hardstatus off
> hardstatus alwayslastline
> hardstatus string '%{= BG}%{.g}[ %{.G}%H %{.g}][ %{= Bw}%?%-Lw%?%{Yr}%{.k}%n*%f%? %t%?%?(%u)%?%{.r}%{Bw}%?%+Lw%? %{.g}%=][%{.W} %Y-%m-%d %c %{.g}]'
> ```
> Note that this has predefined colours and layout that you can easily change yourself, see eg. this [detailed discussion](http://sourceopen.com/2014/06/09/gnu-screen-status-bar-tips-tricks-basics/).
>
> The following commands should help you get started using multiple tabs in a screen window. Note that `^a` stands for `Ctrl-a` in this list.
> * Create a new tab: `^a c`
> * Switch to tab number #: `^a #` (where # is a digit)
> * Switch to the last visited tab: `^a ^a`
> * Close a tab: log out of the shell with `^d`
> * Kill a tab: `^a k` (only use if normal logout through `^d` doesn't work because a process has crashed)
> * Change a tab's name: `^a A`
>
> As one last note, you may find it easier if the tab numbers start with 1, rather than 0. To accomplish this, append the following lines to the aforementioned file `~/.screenrc`:
> ```
> # Start with window 1 (instead of 0)
> bind c screen 1
> bind ^c screen 1
> bind 0 select 10
> screen 1
> ```
