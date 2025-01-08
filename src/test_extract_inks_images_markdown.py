import unittest

from extract_links_images_markdown import extract_markdown_images, extract_markdown_links

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
