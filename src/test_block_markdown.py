import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

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
  def test_block_heading(self):
    markdown = "# This is a level 1 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H1:\n{block_type}")

    markdown = "## This is a level 2 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H2:\n{block_type}")

    markdown = "### This is a level 3 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H3:\n{block_type}")

    markdown = "#### This is a level 4 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H4:\n{block_type}")

    markdown = "##### This is a level 5 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H5:\n{block_type}")

    markdown = "###### This is a level 6 heading"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE H6:\n{block_type}")
  
  def test_block_code(self):
    markdown = "```let variable = code_block```"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE CODE:\n{block_type}")

  def test_block_quote(self):
    markdown = "> This is a quote."
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE QUOTE:\n{block_type}")

  def test_block_unordered_list(self):
    markdown = "- This is an unordered list item"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE UL V1:\n{block_type}")

    markdown = "* This is an unordered list item"
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE UL V2:\n{block_type}")

  def test_block_ordered_list(self):
    markdown = """
1. This is an ordered list item
2. This is an ordered list item
3. This is an ordered list item
"""
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE OL VALID:\n{block_type}")

    markdown = """
1. This is an ordered list item
1. This is an ordered list item
2. This is an ordered list item
"""
    block_type = block_to_block_type(markdown)
    print(f"BLOCK TYPE OL INVALID:\n{block_type}")