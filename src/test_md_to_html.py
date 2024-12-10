import unittest
from md_to_html import markdown_to_html
from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestMarkdownToHTML(unittest.TestCase):
    pass

    def test_paras(self):
        test_markdown = '''ABC

DEF'''
        actual_html = markdown_to_html(test_markdown)
        exp_children = [
            HTMLNode("p", children=[HTMLNode(tag=None, value="ABC")]),
            HTMLNode("p", children=[HTMLNode(tag=None, value="DEF")])
        ]
        expected = ParentNode("div", children=exp_children)
        self.assertEqual(expected, actual_html)