import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_uneq_one_url_nil(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node)
    
    def test_uneq(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        urlnode = TextNode("This is a text node", "bold", "https://www.google.com")
        typenode = TextNode("This is a text node", "italic", "https://www.example.com")
        textnode = TextNode("This is a different text node", "bold", "https://www.example.com")
        self.assertNotEqual(node, urlnode)
        self.assertNotEqual(node, typenode)
        self.assertNotEqual(node, textnode)


if __name__ == "__main__":
    unittest.main()