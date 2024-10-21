import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_1(self):
        n = TextNode(text="My name is _Abhay_", text_type=TextType.TEXT)
        nodes = split_nodes_delimiter([n], "_", text_type=TextType.ITALIC)
        self.assertEqual(len(nodes), 2)
        expected_nodes = [TextNode("My name is ", TextType.TEXT), TextNode("Abhay", TextType.ITALIC)]
        self.assertEqual(nodes, expected_nodes)
    
    def test_split_nodes_2(self):
        n = TextNode("_Italic text_*Bold text*`Code`", TextType.TEXT)
        nodes = split_nodes_delimiter([n], "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        expected_nodes = [TextNode("Italic text", TextType.ITALIC), TextNode("Bold text", TextType.BOLD), TextNode("Code", TextType.CODE)]
        self.assertEqual(nodes, expected_nodes)