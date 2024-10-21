import unittest

import node_conversion
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestNodeConversion(unittest.TestCase):
    def test_text(self):
        text = TextNode("Raw text", TextType.TEXT)
        actual = node_conversion.text_node_to_html_node(text)
        self.assertEqual(LeafNode(None, "Raw text"), actual)
    
    def test_bold(self):
        text = TextNode("Bold text", TextType.BOLD)
        actual = node_conversion.text_node_to_html_node(text)
        self.assertEqual(LeafNode("b", "Bold text"), actual)
    
    def test_italic(self):
        text = TextNode("Italic text", TextType.ITALIC)
        actual = node_conversion.text_node_to_html_node(text)
        self.assertEqual(LeafNode("i", "Italic text"), actual)
    
    def test_code(self):
        text = TextNode("print(\"Hello world\")", TextType.CODE)
        actual = node_conversion.text_node_to_html_node(text)
        self.assertEqual(LeafNode("code", "print(\"Hello world\")"), actual)
    
    def test_link(self):
        text = TextNode("Hyperlink text", TextType.LINK, "https://www.boot.dev")
        actual = node_conversion.text_node_to_html_node(text)
        expected_props = {}
        expected_props["href"] = "https://www.boot.dev"
        self.assertEqual(LeafNode("a", "Hyperlink text", expected_props), actual)
    
    def test_image(self):
        text = TextNode("Alt text", TextType.IMAGE, "https://www.boot.dev/favicon.ico")
        actual = node_conversion.text_node_to_html_node(text)
        exp_props = {}
        exp_props["src"] = "https://www.boot.dev/favicon.ico"
        exp_props["alt"] = "Alt text"
        self.assertEqual(LeafNode("img", "", exp_props), actual)