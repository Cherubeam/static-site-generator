import unittest

from block_markdown import (
  markdown_to_blocks,
  block_to_block_type,
  markdown_to_html_node,
  block_type_paragraph,
  block_type_heading,
  block_type_code,
  block_type_olist,
  block_type_ulist,
  block_type_quote,
)

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

    markdown = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

    results = markdown_to_blocks(markdown)
    block_strings = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
    self.assertListEqual(results, block_strings)

class TestBlockToBlockType(unittest.TestCase):
  def test_block_to_block_types(self):
    block = "# heading"
    self.assertEqual(block_to_block_type(block), block_type_heading)
    block = "```\ncode\n```"
    self.assertEqual(block_to_block_type(block), block_type_code)
    block = "> quote\n> more quote"
    self.assertEqual(block_to_block_type(block), block_type_quote)
    block = "* list\n* items"
    self.assertEqual(block_to_block_type(block), block_type_ulist)
    block = "1. list\n2. items"
    self.assertEqual(block_to_block_type(block), block_type_olist)
    block = "paragraph"
    self.assertEqual(block_to_block_type(block), block_type_paragraph)

# class TestMarkdownToHTMLNode(unittest.TestCase):
#   def test_markdown_to_html_node(self):
#     markdown = """
# # This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item"""

#   results = markdown_to_html_node(markdown)
#   print(f"RESULLLLLTS\n{results}")

class TestMarkdownToHTMLNode(unittest.TestCase):
  def test_markdown_to_html_node(self):
    pass
    # results = markdown_to_html_node("This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
    # print(f"RESULTS\n{results}")


if __name__ == "__main__":
    unittest.main()