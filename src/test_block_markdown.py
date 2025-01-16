import unittest

from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_block_strings(self):
    markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    results = markdown_to_blocks(markdown)
    block_strings = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
    self.assertListEqual(results, block_strings)
