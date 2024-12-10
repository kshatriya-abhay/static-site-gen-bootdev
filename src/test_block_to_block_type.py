from blocks import block_to_block_type, BlockType
import unittest

class BlockToBlockType(unittest.TestCase):
    
    def test_heading_block(self):
        str1 = '''# ABC
## DEF
### GHI
#### JKLM
##### NOPQRSTUVWX
###### YZ'''
        actual = block_to_block_type(str1)
        expected = BlockType.HEADING
        self.assertEqual(expected, actual)

        str2 = 'Test non heading string'
        actual = block_to_block_type(str2)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)
    
    def test_code_block(self):
        str1 = '''```
fmt.Println("Hello world")
```'''
        actual = block_to_block_type(str1)
        expected = BlockType.CODE
        self.assertEqual(expected, actual)

        str2 = '''```
test
'''
        actual = block_to_block_type(str2)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)

        str3 = '''test123
```'''
        actual = block_to_block_type(str3)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)
    
    def test_quote_block(self):
        str1 = '''> Kaunse color ki chaddi pehle ho?
> hmm?
> bata do na'''
        actual = block_to_block_type(str1)
        expected = BlockType.QUOTE
        self.assertEqual(expected, actual)

        str2 = '''> Kaunse color ki chaddi pehle ho?
hmm? // no quote block bruh
> bata do na'''
        actual = block_to_block_type(str2)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)

    def test_unordered_list_block(self):
        str1 = '''* Test 1
* Test 2
* Test 3'''
        actual = block_to_block_type(str1)
        expected = BlockType.ULIST
        self.assertEqual(expected, actual)

        str2 = '''- Point 1
- Point 2
- Point 3'''
        actual = block_to_block_type(str2)
        expected = BlockType.ULIST
        self.assertEqual(expected, actual)

        str3 = '''Not List
Not List
* Huh
'''
        actual = block_to_block_type(str3)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)

    def test_ordered_list_block(self):
        str1 = '''1. Test 1
2. Test 2
3. Test 3'''
        actual = block_to_block_type(str1)
        expected = BlockType.OLIST
        self.assertEqual(expected, actual)

        str2 = '''1 Improper List
2) Uff'''
        actual = block_to_block_type(str2)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)

        str3 = '''Not List
Not List
* Huh
'''
        actual = block_to_block_type(str3)
        expected = BlockType.PARAGRAPH
        self.assertEqual(expected, actual)