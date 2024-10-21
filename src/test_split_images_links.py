import unittest

from split_images_links import *

class TestSplitImages(unittest.TestCase):
    def test_split_images(self):
        input_list = [TextNode("abc ![alt](http://example.com) xyz [url](http://www.google.com)", TextType.TEXT)]
        output_list = split_nodes_image(input_list)
        self.assertEqual(len(output_list), 3)
        self.assertEqual(output_list[0], TextNode("abc ", TextType.TEXT))
        self.assertEqual(output_list[1], TextNode("alt", TextType.IMAGE, "http://example.com"))
        self.assertEqual(output_list[2], TextNode(" xyz [url](http://www.google.com)", TextType.TEXT))
    
    def test_split_images_2(self):
        input_list = [TextNode("![alt](http://example.com)", TextType.TEXT)]
        output_list = split_nodes_image(input_list)
        self.assertEqual(len(output_list), 1)
        self.assertEqual(output_list[0], TextNode("alt", TextType.IMAGE, "http://example.com"))
    
    def test_split_images_3(self):
        input_list = ["abc ![alt](http://example.com) xyz [url](http://www.google.com)"]
        self.assertRaises(AssertionError, split_nodes_image, input_list)

class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        input_list = [TextNode("abc ![alt](http://example.com) xyz [url](http://www.google.com) 123", TextType.TEXT)]
        output_list = split_nodes_link(input_list)
        self.assertEqual(len(output_list), 3)
        self.assertEqual(output_list[0], TextNode("abc ![alt](http://example.com) xyz ", TextType.TEXT))
        self.assertEqual(output_list[1], TextNode("url", TextType.LINK, "http://www.google.com"))
        self.assertEqual(output_list[2], TextNode(" 123", TextType.TEXT))
    
    def test_split_links_2(self):
        input_list = [TextNode("[url](http://example.com)", TextType.TEXT)]
        output_list = split_nodes_link(input_list)
        self.assertEqual(len(output_list), 1)
        self.assertEqual(output_list[0], TextNode("url", TextType.LINK, "http://example.com"))
    
    def test_split_links_3(self):
        input_list = ["abc ![alt](http://example.com) xyz [url](http://www.google.com)"]
        self.assertRaises(AssertionError, split_nodes_link, input_list)