# Licensing

{% objectives "Learning Objectives" %}

- Explain why adding licensing information to a repository is important.
- Choose a proper licence.
- Explain differences in licensing and social expectations.

{% endobjectives %}

When a repository with source code, a manuscript or other creative
works becomes public, it should include a file `LICENSE` or
`LICENSE.txt` in the base directory of the repository that clearly
states under which licence the content is being made available. This
is because creative works are automatically eligible for intellectual
property (and thus copyright) protection. Reusing creative works
without a licence is dangerous, because the copyright holders could
sue you for copyright infringement.

A licence solves this problem by granting rights to others (the
licensees) that they would otherwise not have. What rights are being
granted under which conditions differs, often only slightly, from one
licence to another. In practice, a few licences are by far the most
popular, and [choosealicense.com](https://choosealicense.com/) will
help you find a common licence that suits your needs. Important
considerations include:

* Whether you want to address patent rights.
* Whether you require people distributing derivative works to also
  distribute their source code.
* Whether the content you are licensing is source code.
* Whether you want to license the code at all.

Most open licences fall into a few families:

* **Permissive licences**, such as [MIT](https://choosealicense.com/licenses/mit/),
  [BSD](https://choosealicense.com/licenses/bsd-3-clause/) and
  [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/), let anyone
  reuse the code for any purpose, including in closed-source software, as long
  as they keep the copyright notice. Apache 2.0 also explicitly deals with
  patent rights.
* **Copyleft licences**, such as the
  [GPL](https://choosealicense.com/licenses/gpl-3.0/), require that anyone who
  distributes software built on your code makes their own source code available
  under the same licence. The [LGPL](https://choosealicense.com/licenses/lgpl-2.1/)
  is a weaker variant, often used for libraries: other software may *use* the
  library without itself becoming LGPL.
* **[Creative Commons](https://creativecommons.org/cc-licenses/)
  licences** are designed for documents, figures, data and other content rather
  than code. They let you mix and match conditions such as attribution (BY),
  sharing under the same terms (SA), no commercial use (NC) or no derivative
  works (ND). This lesson itself, for example, is available under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Choosing a licence that is in common use makes life easier for
contributors and users, because they are more likely to already be
familiar with the licence and don't have to wade through a bunch of
jargon to decide if they're ok with it. The [Open Source
Initiative](https://opensource.org/licenses) and [Free Software
Foundation](https://www.gnu.org/licenses/license-list.html) both
maintain lists of licences which are good choices.

[This article][software-licensing] provides an excellent overview of
licensing and licensing options from the perspective of scientists who
also write code.

{% callout "Licensing at CERN" %}

When developing software at CERN you should keep in mind the open grounds on
which this international organisation was constituted. CERN's
[Open Source Program Office](https://ospo.web.cern.ch/) (CERN login required)
and its [Legal Service](https://legal-service.web.cern.ch/) offer guidance on
licensing software and other kinds of materials: when in doubt do not hesitate
to contact them for trustworthy advice.

{% endcallout %}

At the end of the day what matters is that there is a clear statement
as to what the licence is. Also, the licence is best chosen from the
get-go, even if for a repository that is not public. Pushing off the
decision only makes it more complicated later, because each time a new
collaborator starts contributing, they, too, hold copyright and will
thus need to be asked for approval once a licence is chosen.

{% callout "Adding a licence file" %}

When you create a new project, GitHub and GitLab both offer to add a `LICENSE`
file from a list of common licences, and GitHub can also add one to an existing
repository (**Add file > Create new file**, then name it `LICENSE` and pick a
template). Either way, it is just a normal file in your repository, committed
like any other.

{% endcallout %}

{% challenge "Can I Use an Open Licence?" %}


Find out whether you are allowed to apply an open licence to your software.
Can you do this unilaterally,
or do you need permission from someone in your institution?
If so, who?

{% endchallenge %}

{% challenge "What Licences Have I Already Accepted?" %}


Many of the software tools we use on a daily basis (including in this lesson) are
released as open-source software. Pick a project from the list below, or
one of your own choosing. Find its licence (usually in a file called `LICENSE` or
`COPYING`) and talk about how it restricts your use of the software. Is it one of
the licences discussed in this session? How is it different?

- [Git](https://github.com/git/git), the source-code management tool
- [CPython](https://github.com/python/cpython), the standard implementation of the Python language
- [ROOT](https://github.com/root-project/root), the data analysis framework used across HEP
- [uproot](https://github.com/scikit-hep/uproot5), which reads ROOT files in Python without ROOT
- [Geant4](https://github.com/Geant4/geant4), the toolkit for simulating particles passing through matter

{% solution "Solution" %}

* **Git** uses the GPL, version 2: if you distribute a modified version of Git,
  you must also share its source code under the same licence.
* **CPython** uses the Python Software Foundation License, a permissive licence.
* **ROOT** uses the LGPL (version 2.1 or later): you can use ROOT in your own
  software under any licence, but changes to ROOT itself must stay under the
  LGPL.
* **uproot** uses the permissive BSD 3-clause licence.
* **Geant4** has its own licence, the Geant4 Software License, which is
  permissive but not one of the common licences discussed above: another reason
  why choosing a common licence makes life easier for your users.

{% endsolution %}

{% endchallenge %}

[software-licensing]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002598


{% keypoints "Key Points" %}

- Add a `LICENSE` file to your repository, ideally from the start, so that others know how they may reuse your work.
- Permissive licences (such as MIT, BSD and Apache) allow almost any reuse; copyleft licences (such as the GPL) require derived software to be shared under the same licence.
- The Creative Commons family of licences allow people to mix and match requirements and restrictions on attribution, creation of derivative works, further sharing, and commercialisation, and are meant for content rather than code.
- People who are not lawyers should not try to write licences from scratch.

{% endkeypoints %}

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation
