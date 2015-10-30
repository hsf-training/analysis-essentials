def find_files(base, pattern):
    """
    """
    from re import compile
    from os import walk
    pat = compile(pattern)
    return [(root, fname) for root, _, files in walk(base)
                          for fname in files if pat.match(fname)]


def find_html_files(base):
    """
    """
    return find_files(base, r'.*\.html')


def find_md_files(base):
    """ Limiting to `.md` instead of also allowing `.mdown` or `.markdown` is
    deliberate.
    """
    return find_files(base, r'.*\.md')
