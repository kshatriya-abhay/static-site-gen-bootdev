import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        props = {}
        props["tag1"] = "value1"
        l1 = LeafNode("p", "Lorem Ipsum", props)
        self.assertEqual("<p tag1=\"value1\">Lorem Ipsum</p>", l1.to_html())