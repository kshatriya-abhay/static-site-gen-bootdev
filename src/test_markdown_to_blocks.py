import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_md_to_block(self):
        test_md = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        actual_output = markdown_to_blocks(test_md)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            '''* This is the first list item in a list block
* This is a list item
* This is another list item'''
        ]
        self.assertEqual(actual_output, expected)
        