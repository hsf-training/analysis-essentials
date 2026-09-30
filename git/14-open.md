# Open Science

{% objectives "Learning Objectives" %}

- Explain how a version control system can be leveraged as an electronic lab notebook for computational work.

{% endobjectives %}

> The opposite of "open" isn't "closed".
> The opposite of "open" is "broken".

{% right %} John Wilbanks 
{% endright %}

Free sharing of information might be the ideal in science,
but the reality is often more complicated.
Normal practice today looks something like this:

*   A scientist collects some data and stores it on a machine
    that is occasionally backed up by her department.
*   She then writes or modifies a few small programs
    (which also reside on her machine)
    to analyse that data.
*   Once she has some results,
    she writes them up and submits her paper.
    She might include her data—a growing number of journals require this—but
    she probably doesn't include her code.
*   Time passes.
*   The journal sends her reviews written anonymously by a handful of other people in her field.
    She revises her paper to satisfy them,
    during which time she might also modify the scripts she wrote earlier,
    and resubmits.
*   More time passes.
*   The paper is eventually published.
    It might include a link to an online copy of her data,
    but the paper itself will be behind a paywall:
    only people who have personal or institutional access
    will be able to read it.

For a growing number of scientists,
though,
the process looks like this:

*   The data that the scientist collects is stored in an open access repository
    like [figshare](https://figshare.com/) or
    [Zenodo](https://zenodo.org), possibly as soon as it's collected,
    and given its own
    [Digital Object Identifier](https://en.wikipedia.org/wiki/Digital_object_identifier) (DOI).
    Or the data was already published and is stored in
    [Dryad](https://datadryad.org/).
*   The scientist creates a new repository on GitHub or GitLab to hold her work.
*   As she does her analysis,
    she pushes changes to her scripts
    (and possibly some output files)
    to that repository.
    She also uses the repository for her paper;
    that repository is then the hub for collaboration with her colleagues.
*   When she's happy with the state of her paper,
    she posts a version to [arXiv](https://arxiv.org/)
    or some other preprint server
    to invite feedback from peers.
*   Based on that feedback,
    she may post several revisions
    before finally submitting her paper to a journal.
*   The published paper includes links to her preprint
    and to her code and data repositories,
    which  makes it much easier for other scientists
    to use her work as starting point for their own research.

This open model accelerates discovery:
the more open work is,
[the more widely it is cited and re-used](https://doi.org/10.1371/journal.pone.0000308).
However,
people who want to work this way need to make some decisions
about what exactly "open" means and how to do it. You can find more on the different aspects of Open Science in [this book](https://link.springer.com/book/10.1007/978-3-319-00026-8).

This is one of the (many) reasons we teach version control.
When used diligently,
it answers the "how" question
by acting as a shareable electronic lab notebook for computational work:

*   The conceptual stages of your work are documented, including who did
    what and when. Every step is stamped with an identifier (the commit ID)
    that is for most intents and purposes unique.
*   You can tie documentation of rationale, ideas, and other
    intellectual work directly to the changes that spring from them.
*   You can refer to what you used in your research to obtain your
    computational results in a way that is unique and recoverable.
*   With a distributed version control system such as Git, the version
    control repository is easy to archive for perpetuity, and contains
    the entire history.

{% callout "Open science in high-energy physics" %}

Particle physics has a strong open science culture, and much of the
infrastructure mentioned above was built or is run by the HEP community:

*   [arXiv](https://arxiv.org/) started as a preprint server for physics, and
    almost every HEP paper appears there before publication. Thanks to
    [SCOAP3](https://scoap3.org/), most HEP journal articles are also open
    access.
*   [Zenodo](https://zenodo.org) is run by CERN, and is a common place to
    publish software, data and posters with a DOI.
*   [INSPIRE](https://inspirehep.net/) indexes HEP literature, and
    [HEPData](https://www.hepdata.net/) hosts the numerical data behind
    published plots and tables.
*   The [CERN Open Data portal](https://opendata.cern.ch/) makes data from the
    LHC experiments available to everyone, together with the software needed
    to analyse it.

To make your own code citable, see the lesson on [citation](16-citation.md).

{% endcallout %}

{% challenge "How Reproducible Is My Work?" %}


Ask one of your labmates to reproduce a result you recently obtained
using only what they can find in your papers or on the web.
Try to do the same for one of their results,
then try to do it for a result from a lab you work with.

{% endchallenge %}

{% challenge "How to Find an Appropriate Data Repository?" %}


Surf the internet for a couple of minutes and check out the data repositories
mentioned above: [Figshare](https://figshare.com/), [Zenodo](https://zenodo.org),
[Dryad](https://datadryad.org/). Depending on your field of research, you might
find community-recognised repositories that are well-known in your field.
You might also find useful [these data repositories recommended by Nature](
https://www.nature.com/sdata/policies/repositories).
Discuss with your neighbour which data repository you might want to
approach for your current project and explain why.

{% endchallenge %}

{% challenge "Can I Also Publish Code?" %}


There are many new ways to publish code and to make it citable. One
way is described [on the homepage of GitHub itself](
https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
Basically it's a combination of GitHub (where the code is) and Zenodo (the
repository creating the DOI). Read through this page while being aware
that this is only one of many ways to make your code citable; the lesson on
[citation](16-citation.md) describes how to tell people how to cite it.

{% endchallenge %}


{% keypoints "Key Points" %}

- Open scientific work is more useful and more highly cited than closed.

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation 
{% endright %}
