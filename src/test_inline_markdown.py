import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image
from extract_links_images_markdown import extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_invalid_markdown_exception(self):
    node = TextNode("This is text with a `code block word", TextType.TEXT)
    with self.assertRaises(ValueError):
      new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

  def test_delim_bold(self):
    node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_double(self):
    node = TextNode(
      "This is text with a **bolded** word and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_bold_multiword(self):
    node = TextNode(
      "This is text with a **bolded word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded word", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_italic(self):
    node = TextNode("This is text with an *italic* word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_and_italic(self):
    node = TextNode("**bold** and *italic*", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    self.assertListEqual(
      [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
      ],
      new_nodes,
    )

  def test_delim_code(self):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

class TestSplitImagesDelimiter(unittest.TestCase):
  def test_images(self):
    node_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    node_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    node_text = "This is just text."

    new_nodes = split_nodes_image([node_images])
    print(f"TEST RESULTS:\n{new_nodes}")
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("rick roll", TextType.LINK, "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", TextType.TEXT),
        TextNode("obi wan", TextType.LINK, "https://i.imgur.com/fJRm4Vk.jpeg")
      ], 
      new_nodes
    )

# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

