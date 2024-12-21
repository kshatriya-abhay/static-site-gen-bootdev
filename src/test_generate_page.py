import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        md = '''This is not the heading
#  this is the heading  '''
        title = extract_title(md)
        expected = "this is the heading"
        self.assertEqual(expected, title)

        md2 = "markdown without heading\n\nline 2"
        with self.assertRaises(Exception):
            t = extract_title(md2)