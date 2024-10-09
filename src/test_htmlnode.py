import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        child = HTMLNode(None, "raw text")
        props = {}
        props["tag1"] = "value1"
        props["tag2"] = "value2"
        node = HTMLNode("<p>", "Lorem Ipsum", [child], props)
        attribute_str = node.props_to_html()
        self.assertEqual(" tag1=\"value1\" tag2=\"value2\"", attribute_str)
        
    def test_props_to_html_blank(self):
        props = {}
        node = HTMLNode("", "", [], props)
        attr = node.props_to_html()
        self.assertEqual("", attr)