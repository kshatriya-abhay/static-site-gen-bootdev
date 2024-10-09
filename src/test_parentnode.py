import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        lprops = {}
        lprops["t1"] = "v1"
        lnode = LeafNode("p","Test", lprops)
        parentprops = {}
        parentprops["t2"] = "v2"
        pnode = ParentNode("div", [lnode], parentprops)
        phtml = pnode.to_html()
        expected_html = "<div t2=\"v2\"><p t1=\"v1\">Test</p></div>"
        self.assertEqual(expected_html, phtml)
    
    def test_to_html_multilevel(self):
        l1node = LeafNode("p", "Test1")
        l2node = LeafNode("b", "Bold3")
        p1node = ParentNode("body", [l1node, l2node])
        l4node = LeafNode("title", "Test Title")
        p2node = ParentNode("head", [l4node])
        p3node = ParentNode("html", [p2node, p1node])
        expected_html = "<html><head><title>Test Title</title></head><body><p>Test1</p><b>Bold3</b></body></html>"
        self.assertEqual(expected_html, p3node.to_html())
    
    def test_to_html_emptynode(self):
        p1node = ParentNode("div", [])
        self.assertRaises(ValueError, p1node.to_html)
    
    def test_to_html_nonetag(self):
        p1node = ParentNode(None, [LeafNode("a","Test")])
        self.assertRaises(ValueError, p1node.to_html)