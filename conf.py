# You should normally never do wildcard imports
# Here it is useful to allow the configuration to be maintained elsewhere
from starterkit_ci.sphinx_config import *  # NOQA

project = 'Analysis essentials'
copyright = 'HSF [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode) - Originally based on [swcarpentry](https://github.com/swcarpentry/) © 2016–2017 Software Carpentry Foundation'
author = 'HSF'
html_logo = 'hsf_logo_angled.png'

exclude_patterns += [
    'miniconda/**',
    'shell/data-shell/**',
    'README.md',
]

html_context = {
    'display_github': True,
    'github_user': 'hsf-training',
    'github_repo': 'analysis-essentials',
    'github_version': 'master',
    'conf_py_path': '/',
}


html_static_path += [
    f'_static',
]

linkcheck_ignore += [
    # FIXME: This no longer exists...
    r'http://lhcb-release-area\.web\.cern\.ch/LHCb-release-area/DOC/online/releases/v4r65/doxygen/df/dd9/src_2_lineshape_maker_8cpp__incl\.png',
]

for folder in ['advanced-python', 'git', 'python', 'shell-extras', 'shell']:
    starterkit_ci_redirects[f'{folder}/index.html'] = f'https://hsf-training.github.io/analysis-essentials/{folder}/README.html'


def hsf_ci_setup(app):
    app.add_css_file('hsf.css')


setup.extra_setup_funcs += [hsf_ci_setup]

nbsphinx_execute = 'always'
nbsphinx_timeout = 60*20
# FIXME: This should be removed
# nbsphinx_execute = 'never'


def setup(app):
    app.add_js_file(
        "https://views.scientific-python.org/js/script.js",
        **{"defer": "defer", "data-domain": "hepsoftwarefoundation.org"}
    )
