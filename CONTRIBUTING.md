analysis-essentials is an open source project,
and we welcome contributions of all kinds:
new lessons,
fixes to existing material,
bug reports,
and reviews of proposed changes are all equally welcome.

By contributing,
you are agreeing that we may redistribute your work under
[these licenses][license].
You also agree to abide by our
[contributor code of conduct][conduct].

## Getting Started

1.  We use the [fork and pull][gh-fork-pull] model to manage changes. More information
    about [forking a repository][gh-fork] and [making a Pull Request][gh-pull].

2.  To build the lessons please install the [dependencies](#DEPENDENCIES).

2.  For our lessons,
    you should branch from and submit pull requests against the `master` branch.

3.  When editing lesson pages, you need only commit changes to the Markdown source files.

4.  If you're looking for things to work on,
    please see [the list of issues for this repository][issues].
    Comments on issues and reviews of pull requests are equally welcome.

## Dependencies

To build the lessons locally install the following:

1. [Install node.js and npm](https://docs.npmjs.com/)

2. [Install gitbook](https://github.com/GitbookIO/gitbook) with `npm install gitbook-cli -g`

3. To convert Markdown files into HTML pages in the `_book` directory, go
   into the root directory of your lesson and run:

   ~~~
   $ make
   ~~~

   Now open `_book/index.html` in a browser to see your changes.

[conduct]: CONDUCT.md
[issues]: https://github.com/lhcb/analysis-essentials/issues
[license]: LICENSE.md
[pro-git-chapter]: http://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project
[gh-fork]: https://help.github.com/articles/fork-a-repo/
[gh-pull]: https://help.github.com/articles/using-pull-requests/
[gh-fork-pull]: https://help.github.com/articles/using-pull-requests/#fork--pull
[swc-lessons]: http://software-carpentry.org/lessons.html
