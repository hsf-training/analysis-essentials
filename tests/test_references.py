#!/usr/bin/env python

import unittest

class TestLinksInHtmlFiles(unittest.TestCase):
    def test_files(self):
        from .common import find_html_files
        cond = all(self.check_links_in_file(r, f)
                   for r, f in find_html_files('_book'))
        self.assertTrue(cond)

    @classmethod
    def check_links_in_file(cls, root, fname):
        from bs4 import BeautifulSoup
        from os import path

        soup = BeautifulSoup(open(path.join(root, fname)))
        links = [a.get('href') for a in soup.findAll('a')]
        links = [l for l in links if l.startswith('.')]  # Only local links

        return all(path.exists(path.join(root, lhref)) for lhref in links)
