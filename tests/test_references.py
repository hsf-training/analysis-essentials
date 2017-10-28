import os
import re
import unittest


class TestRefsInMarkdownFiles(unittest.TestCase):
    def test_refs(self):
        pat = re.compile(r'\[[^\]]*\]\(([^\)]+)\)')
        checked = set()
        to_check = ['SUMMARY.md']
        while to_check:
            path = to_check.pop()
            root = os.path.dirname(path)
            self.assertTrue(os.path.exists(path),
                            'File `{}` does not exists.'.format(path))
            checked.add(path)
            if path.endswith('.md'):
                with open(path) as f:
                    refs = pat.findall(f.read())
                files = [os.path.normpath(os.path.join(root, ref))
                         for ref in refs if not ':' in ref and not ref.startswith('#')]
                to_check += [f for f in files if f not in checked]
