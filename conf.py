# You should normally never do wildcard imports
# Here it is useful to allow the configuration to be maintained elsewhere
from starterkit_ci.sphinx_config import *  # NOQA

project = 'Analysis essentials'
copyright = 'TODO1'
author = 'TODO2'
html_logo = 'hsf_logo_angled.png'

exclude_patterns = [
    r'shell/data-shell/writing/thesis/empty-draft.md',
    r'shell/data-shell/.*',
    'README.md',
]

html_context = {
    'display_github': True,
    'github_user': 'hsf-training',
    'github_repo': 'analysis-essentials',
    'github_version': 'master',
    'conf_py_path': '/',
}

linkcheck_ignore += [
    # FIXME: This no longer exists...
    r'http://lhcb-release-area\.web\.cern\.ch/LHCb-release-area/DOC/online/releases/v4r65/doxygen/df/dd9/src_2_lineshape_maker_8cpp__incl\.png',
]
