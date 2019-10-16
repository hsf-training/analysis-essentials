# Licensing

{% objectives "Learning Objectives" %}

- Explain why adding licensing information to a repository is important.
- Choose a proper license.
- Explain differences in licensing and social expectations.

{% endobjectives %}

When a repository with source code, a manuscript or other creative
works becomes public, it should include a file `LICENSE` or
`LICENSE.txt` in the base directory of the repository that clearly
states under which license the content is being made available. This
is because creative works are automatically eligible for intellectual
property (and thus copyright) protection. Reusing creative works
without a license is dangerous, because the copyright holders could
sue you for copyright infringement.

A license solves this problem by granting rights to others (the
licensees) that they would otherwise not have. What rights are being
granted under which conditions differs, often only slightly, from one
license to another. In practice, a few licenses are by far the most
popular, and [choosealicense.com](https://choosealicense.com/) will
help you find a common license that suits your needs.  Important
considerations include:

* Whether you want to address patent rights.
* Whether you require people distributing derivative works to also
  distribute their source code.
* Whether the content you are licensing is source code.
* Whether you want to license the code at all.

Choosing a licence that is in common use makes life easier for
contributors and users, because they are more likely to already be
familiar with the license and don't have to wade through a bunch of
jargon to decide if they're ok with it.  The [Open Source
Inititative](https://opensource.org/licenses) and [Free Software
Foundation](https://www.gnu.org/licenses/license-list.html) both
maintain lists of licenses which are good choices.

[This article][software-licensing] provides an excellent overview of
licensing and licensing options from the perspective of scientists who
also write code.

{% callout "Licensing at CERN" %}

When developing software at CERN you should keep in mind the open grounds on
which this international organization was constituted. CERN has a legal office
offering [counseling and guidelines](https://legal.web.cern.ch/licenses) for
licensing software and other kinds of materials: when in doubt do not hesitate
to contact them for trustworthy advice.

{% endcallout %}

At the end of the day what matters is that there is a clear statement
as to what the license is. Also, the license is best chosen from the
get-go, even if for a repository that is not public. Pushing off the
decision only makes it more complicated later, because each time a new
collaborator starts contributing, they, too, hold copyright and will
thus need to be asked for approval once a license is chosen.

{% challenge "Can I Use Open License?" %}


Find out whether you are allowed to apply an open license to your software.
Can you do this unilaterally,
or do you need permission from someone in your institution?
If so, who?

{% endchallenge %}

{% challenge "What licenses have I already accepted?" %}


Many of the software tools we use on a daily basis (including in this workshop) are
released as open-source software. Pick a project on GitHub from the list below, or
one of your own choosing. Find its license (usually in a file called `LICENSE` or
`COPYING`) and talk about how it restricts your use of the software. Is it one of
the licenses discussed in this session? How is it different?
- [Git](https://github.com/git/git), the source-code management tool
- [CPython](https://github.com/python/cpython), the standard implementation of the Python language
- [Jupyter](https://github.com/jupyter), the project behind the web-based Python notebooks we'll be using
- [EtherPad](https://github.com/ether/etherpad-lite), a real-time collaborative editor

{% endchallenge %}

[software-licensing]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002598


{% keypoints "Key Points" %}

- People who incorporate GPL'd software into their own software must make their software also open under the GPL license; most other open licenses do not require this.
- The Creative Commons family of licenses allow people to mix and match requirements and restrictions on attribution, creation of derivative works, further sharing, and commercialization.
- People who are not lawyers should not try to write licenses from scratch.

{% endkeypoints %}

{% right %} [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Based on [git-novice](https://github.com/swcarpentry/git-novice) © 2016–2017 Software Carpentry Foundation 
{% endright %}
