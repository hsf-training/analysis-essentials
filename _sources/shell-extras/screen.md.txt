## Using screen to keep things running
{% objectives "Learning Objectives" %}

* Create a new `screen` session
* Disconnect from a `screen` session
* Reconnect to an existing `screen` session
* End an existing `screen` session
* Handling of Kerberos tokens

{% endobjectives %}

Often we want to run a program for a long time on a computer we
connected to via `ssh`, like the `lxplus` machines. The `screen`
program allows you to keep programs running on the remote computer
even if you disconnect from it. For example when putting your laptop
to sleep or losing wifi.

Connect to `lxplus`:

```bash
$ ssh lxplus.cern.ch
```

You can start `screen` by simply typing its name:

```bash
$ screen
```

Once you do this it will look as if nothing has happened. However you
now have a fresh terminal inside what is refered to as a "screen
session". Let's type some commands that generate some output:

```bash
$ uptime
```
```
 11:48:02 up 15 days, 20:36, 105 users,  load average: 2.26, 2.10, 3.16
```
```bash
$ date
```
```
Thu Apr 16 11:48:32 CEST 2015
```

To disconnect from this session press `Ctrl-a d`. We are now back to
the terminal that we first started in. You can check that your
`screen` session is still running by typing `screen -list`, which will
list all active sessions:

```bash
$ screen -list
```
```
There is a screen on:
      25593.pts-44.lxplus0234   (Detached)
1 Socket in /var/run/screen/S-thead.
```

To reconnect to the session you use `screen -rD`. When there is just
one session running (like now) then it will reconnect you to that
session. Try it and you should see the date and time output by the
`date` command we ran earlier.

When you have more than one session you need to provide the name of
the session as an argument to `screen -rD`. The name of the above
session is: `25593.pts-44.lxplus0234`. You can reconnect to it with:

```bash
$ screen -rD 25593.pts-44.lxplus0234
```

To end a `screen` session you are currently connected to, simply press
`Ctrl-d`. Just like you would to disconnect from a `ssh` session.

A `screen` session is tied to a specific computer. This means you need
to remember which computer you connected to. Even if your `screen`
session keeps running, you can only resume it from the same machine as
you started it.

When connecting to `lxplus` you are assigned to a random computer, but you can find out its name with `hostname`:

```bash
$ hostname
```
```
lxplus0081.cern.ch
```

This tells you that the computer you are connected to is called
`lxplus0081.cern.ch`. Later on you can re-connect to exactly this
machine with:

```bash
$ ssh lxplus0081.cern.ch
```

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

{% callout "tmux" %}

`tmux` is another program you can use to keep things running remotely. 
In practice, it is very similar to screen, but it has some minor 
differences. You can find syntax guides easily online, including guides 
showing the equivalent commands in tmux and screen 
([this one](http://hyperpolyglot.org/multiplexers) is quite good), but 
here's a quick list of equivalent commands to those used in this lesson:
* `tmux ls` instead of `screen -list`
* `Ctrl-b d` to detach instead of `Ctrl-a d` (`tmux` in general uses 
  `Ctrl-b` instead of `Ctrl-a`)
* `tmux a` or `tmux attach` instead of `screen -rD`

{% endcallout %}
