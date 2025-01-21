import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_links, extract_markdown_images, extract_markdown_links, text_to_textnodes

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

class TestSplitImageDelimiter(unittest.TestCase):
  def test_split_image(self):
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
      ],
      new_nodes,
    )

  def test_split_image_single(self):
    node = TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
      ],
      new_nodes
    )

  def test_split_images(self):
    node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        TextNode(" and ", TextType.TEXT),
        TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
      ], 
      new_nodes
    )

class TestSplitLinkDelimiter(unittest.TestCase):
  def test_split_link(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
    new_nodes = split_nodes_links([node])
    self.assertListEqual(
      [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
      ],
      new_nodes,
    )

  def test_split_links(self):
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT)
    new_nodes = split_nodes_links([node])
    self.assertListEqual(
      [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")     
      ],
      new_nodes
    )

class TestExtractLinksImagesMarkdown(unittest.TestCase):
  def test_images(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    matches = extract_markdown_images(text)
    self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

  def test_images_without_alt(self):
    text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![](https://i.imgur.com/fJRm4Vk.jpeg)"
    matches = extract_markdown_images(text)
    self.assertEqual([("", "https://i.imgur.com/aKaOqIh.gif"), ("", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

  def test_links(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    matches = extract_markdown_links(text)
    self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

  def test_links_without_anchor(self):
    text = "This is text with a link [](https://www.boot.dev) and [](https://www.youtube.com/@bootdotdev)"
    matches = extract_markdown_links(text)
    self.assertEqual([("", "https://www.boot.dev"), ("", "https://www.youtube.com/@bootdotdev")], matches)

class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_text_nodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)
    self.assertListEqual(
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev")
      ],
      new_nodes
    )


if __name__ == "__main__":
    unittest.main()