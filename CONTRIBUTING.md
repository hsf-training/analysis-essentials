# Contributing

[starterkit-lessons][repo] is an open source project, and we welcome contributions of all kinds:

* New lessons;
* Fixes to existing material;
* Bug reports; and
* Reviews of proposed changes.

By contributing, you are agreeing that we may redistribute your work under [these licenses][license].
You also agree to abide by our [contributor code of conduct][conduct].

## Getting Started

1.  We use the [fork and pull][gh-fork-pull] model to manage changes.
    More information about [forking a repository][gh-fork] and [making a Pull Request][gh-pull].

2.  To build the lessons please install the [dependencies](#DEPENDENCIES).

2.  For our lessons, you should branch from and submit pull requests against the `master` branch.

3.  When editing lesson pages, you need only commit changes to the Markdown source files.

4.  If you're looking for things to work on, please see [the list of issues for this repository][issues].
    Comments on issues and reviews of pull requests are equally welcome.

## Dependencies

To build the lessons locally, install the following:

1. [sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
2. [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
2. [recommonmark](https://recommonmark.readthedocs.io/en/latest/)

Then build the pages:

```shell
$ starterkit_ci build --allow-warnings
$ starterkit_ci check --allow-warnings
```

and start a web server to host them:

```shell
$ cd build
$ python -m http.server 8000
```
You can see your local version by using a web-browser to navigate to `http://localhost:8000` or wherever it says it's serving the book.

[conduct]: CONDUCT.md
[repo]: https://github.com/lhcb/starterkit-lessons
[issues]: https://github.com/lhcb/starterkit-lessons/issues
[license]: LICENSE.md
[pro-git-chapter]: https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project
[gh-fork]: https://help.github.com/en/articles/fork-a-repo
[gh-pull]: https://help.github.com/en/articles/about-pull-requests
[gh-fork-pull]: https://reflectoring.io/github-fork-and-pull/


```eval_rst
.. toctree::
    :hidden:

    CONDUCT.md
    LICENSE.md
```
