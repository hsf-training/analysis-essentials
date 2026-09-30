# Citation

{% objectives "Learning Objectives" %}

- Make your work easy to cite.
- Add a `CITATION.cff` file to a repository.

{% endobjectives %}

If other people use your code in their research, you will want them to cite
it, and they will want to know how. The simplest way to tell them is to add a
*citation file* to your repository, which describes how to reference your
project.

The most widely used format for this is the
[Citation File Format](https://citation-file-format.github.io/) (CFF): a small
text file called `CITATION.cff` in the base directory of your repository. For
Dracula's `planets` project, it could look like this:

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "planets: notes on possible bases in the Solar System"
authors:
  - family-names: "Dracula"
    given-names: "Vlad"
    orcid: "https://orcid.org/0000-0000-0000-0000"
  - family-names: "Stein"
    given-names: "Frank N."
version: 1.0.0
date-released: 2026-09-30
url: "https://gitlab.cern.ch/vlad/planets"
```

The file is written in YAML, like the CI configuration in the
[previous lessons](12-ci.md). Besides the required fields (`cff-version`,
`message`, `title` and `authors`), you can add many others, for example the
`doi` of a published version (see below) or the `license` of your code.
Including an [ORCID](https://orcid.org/) identifier for each author makes sure
the citation is linked to the right person.

Because the format is standard, tools can read it:

* On GitHub, a repository with a `CITATION.cff` file gets a **Cite this
  repository** link in the right-hand sidebar, which gives the citation
  ready to copy in APA or BibTeX format. See
  [GitHub's documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)
  for details.
* [Zenodo](https://zenodo.org) can use it to fill in the metadata of your
  software when it archives a release and gives it a DOI (see the
  [open science](13-open.md) lesson).
* Other tools can convert it into BibTeX and other formats, such as
  [cffconvert](https://github.com/citation-file-format/cffconvert), which can
  also check that your file is valid.

You don't need to write the file by hand: the
[cffinit](https://citation-file-format.github.io/cff-initializer-javascript/)
website creates one for you from a simple form.

{% callout "Getting a DOI for your software" %}

A citation is most useful when it points to a specific, permanent version of
your work. The common way to get one is to archive a release of your repository
on [Zenodo](https://zenodo.org), which gives it a
[DOI](https://en.wikipedia.org/wiki/Digital_object_identifier). For
repositories on GitHub this can happen automatically for every release; see
[GitHub's guide](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
Once you have a DOI, add it to your `CITATION.cff` with the `doi` field.

{% endcallout %}

{% discussion "Plain-text CITATION files" %}

Before the Citation File Format existed, projects often included a plain-text
file called `CITATION` or `CITATION.txt`, written in whatever form the authors
liked. You will still find many of these. For example, the
[one for Software Carpentry](https://github.com/swcarpentry/website-archive/blob/gh-pages/CITATION)
states:

```
To reference Software Carpentry in publications, please cite both of the following:

Greg Wilson: "Software Carpentry: Getting Scientists to Write Better
Code by Making Them More Productive".  Computing in Science &
Engineering, Nov-Dec 2006.

Greg Wilson: "Software Carpentry: Lessons Learned". arXiv:1307.5448,
July 2013.

@article{wilson-software-carpentry-2006,
    author =  {Greg Wilson},
    title =   {Software Carpentry: Getting Scientists to Write Better Code by Making Them More Productive},
    journal = {Computing in Science \& Engineering},
    month =   {November--December},
    year =    {2006},
}

@online{wilson-software-carpentry-2013,
  author      = {Greg Wilson},
  title       = {Software Carpentry: Lessons Learned},
  version     = {1},
  date        = {2013-07-20},
  eprinttype  = {arxiv},
  eprint      = {1307.5448}
}
```

This works for human readers, but because there is no fixed format, tools
cannot read it automatically. For new projects, prefer `CITATION.cff`.

{% enddiscussion %}

{% challenge "Make Your Project Citable" %}

Create a `CITATION.cff` file for one of your own projects (or for your
`planets` repository), either by hand or with
[cffinit](https://citation-file-format.github.io/cff-initializer-javascript/).
Commit it and push it. If your repository is on GitHub, check that the
**Cite this repository** link appears.

{% endchallenge %}

{% keypoints "Key Points" %}

- Add a `CITATION.cff` file to a repository to explain how you want your work cited.
- The Citation File Format is understood by GitHub, Zenodo and other tools.
- Archiving a release on Zenodo gives your software a DOI that others can cite.

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation
{% endright %}
