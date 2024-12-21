import unittest

from extract_links_images import *

class TestExtractLinks(unittest.TestCase):
    def test_extract_links(self):
        tuple_list = extract_markdown_links("This is a [url](http://www.example.com)")        
        self.assertEqual(len(tuple_list), 1)
        self.assertEqual(tuple_list[0], tuple(["url", "http://www.example.com"]))

        tuple_list = extract_markdown_links("This is an ![image](http://www.google.com/favicon.ico)")
        self.assertEqual(len(tuple_list), 0)

        tuple_list = extract_markdown_links("This is a local link [first post here](/majesty)")
        self.assertEqual(len(tuple_list), 1)
        self.assertEqual(tuple_list[0], tuple(["first post here", "/majesty"]))

class TestExtractImages(unittest.TestCase):
    def test_extract_images(self):
        tuple_list = extract_markdown_images("This is a [url](http://www.example.com)")        
        self.assertEqual(len(tuple_list), 0)

        tuple_list = extract_markdown_images("This is an ![image](http://www.google.com/favicon.ico)")
        self.assertEqual(len(tuple_list), 1)
        self.assertEqual(tuple_list[0], tuple(["image", "http://www.google.com/favicon.ico"]))