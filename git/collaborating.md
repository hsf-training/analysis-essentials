## Collaborating
One important feature is the `.gitignore` file. It defines a list of files
(wildcards are possible) that should always be ignored by Git for the current
repository. For example, if you are collaborating on a paper in LaTeX, you will
want to put your `.tex` files under version control but not any of the
intermediate files produced by your LaTeX compilation. In your repository's root
folder, create a file called `.gitinore` and fill it with the following lines:

```
*.acn
*.acr
*.alg
*.aux
*.bbl
*.blg
*.dvi
*.glg
*.glo
*.gls
*.idx
*.ilg
*.ind
*.ist
*.lof
*.log
*.lot
*.maf
*.mtc
*.mtc1
*.out
*.synctex.gz
*.toc
```

Please not that this list does not include `.pdf` files as you will probably add
figures as PDF files. You will want to add your resulting `.pdf` file to that
list above to keep the (dynamic) binary file from being put under version
control.

For files that are specific to your system (like `.DS_Store` files on OS X or
`.swp` files if you are using Vim) you can globally define a list of file types
that should be ignored by Git. Those files have nothing to do with your project
and are specific to _your_ system. Your collaborator might be using Emacs on
Linux and therefore not care about those files. Create a new file in your home
directory called `.gitignore` and add the following lines:

```
.DS_Store
*.swp
```

Then run the following command

```bash
git config --global core.excludesfile $HOME/.gitignore
```

This will tell Git to ignore all files named `.DS_Store` or those files ending
in `.swp`.
