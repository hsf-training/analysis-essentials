## Advanced screen topics

### Finding lost screens

Once you start a `screen` session you need to remember which
`lxplus` node it is running on. If you forget to note that down
you can use the following little snippet to find any `screen`
sessions running on `lxplus` nodes:

```bash
for i in $(seq -f "%04g" 1 500); do
 ssh -o ConnectTimeout=10 -o PreferredAuthentications=gssapi-with-mic,gssapi -o GSSAPIAuthentication=yes -o StrictHostKeyChecking=no -o LogLevel=quiet lxplus$i.cern.ch "(screen -list | head -1 | grep -q 'There is a screen on') && hostname && screen -list"
done
```
This will connect to the first 500 lxplus nodes in
turn, checking if a `screen` session is running and if
yes prints the hostname and output of `screen -list`.


### Using tabs in screen

Screen supports some features beyond detaching a session. A very useful feature is different sessions in tab pages, all within a single instance of `screen`.
In order to maximise the usefulness of this feature, you need to set the screen status bar. The simplest way to do this is by appending the following line to the file `~/.screenrc` (create it if it doesn't already exist):
```
# Status lines
hardstatus off
hardstatus alwayslastline
hardstatus string '%{= BG}%{.g}[ %{.G}%H %{.g}][ %{= Bw}%?%-Lw%?%{Yr}%{.k}%n*%f%? %t%?%?(%u)%?%{.r}%{Bw}%?%+Lw%? %{.g}%=][%{.W} %Y-%m-%d %c %{.g}]'
```
Note that this has predefined colours and layout that you can easily change yourself, see eg. this [detailed discussion](https://web.archive.org/web/20141011004648/http://sourceopen.com/2014/06/09/gnu-screen-status-bar-tips-tricks-basics/).

The following commands should help you get started using multiple tabs in a screen window. Note that `^a` stands for `Ctrl-a` in this list.
* Create a new tab: `^a c`
* Switch to tab number #: `^a #` (where # is a digit)
* Switch to the last visited tab: `^a ^a`
* Close a tab: log out of the shell with `^d`
* Kill a tab: `^a k` (only use if normal logout through `^d` doesn't work because a process has crashed)
* Change a tab's name: `^a A`

As one last note, you may find it easier if the tab numbers start with 1, rather than 0. To accomplish this, append the following lines to the aforementioned file `~/.screenrc`:
```
# Start with window 1 (instead of 0)
bind c screen 1
bind ^c screen 1
bind 0 select 10
screen 1
```
