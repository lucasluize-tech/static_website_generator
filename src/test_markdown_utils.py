import unittest
from markdown_utils import markdown_to_blocks, block_to_block_type


class TestMarkdownUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        mk_input = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        blocks = markdown_to_blocks(mk_input)
        self.assertEqual(len(blocks), 3)

    def test_block_to_block_type(self):
        heading = "### This is a heading"
        self.assertEqual(block_to_block_type(heading), "heading")

        code_block = "```python\nprint('Hello World')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")

        unordered_list = "* This is the first list item in a list block"
        self.assertEqual(block_to_block_type(unordered_list), "unordered_list")

        ordered_list = "- This is the first list item in a list block"
        ordered_list_numbers = "1. This is the first list item in a list block"
        self.assertEqual(block_to_block_type(ordered_list), "ordered list")
        self.assertEqual(block_to_block_type(ordered_list_numbers), "ordered list")

        quote = "> This is a quote"
        self.assertEqual(block_to_block_type(quote), "quote")

        paragraph = "This is a paragraph of text."
        self.assertEqual(block_to_block_type(paragraph), "paragraph")
