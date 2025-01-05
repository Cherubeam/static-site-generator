import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
  def test_repr(self):
    node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
    self.assertEqual(node.__repr__(), "HTMLNode(Tag: p, Value: What a strange world, Children: [], Props: {'class': 'primary'})")

  def test_values(self):
    node = HTMLNode("div", "I wish I could read")
    self.assertEqual(node.tag, "div")
    self.assertEqual(node.value, "I wish I could read")
    self.assertEqual(node.children, [])
    self.assertEqual(node.props, {})

  def test_a(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }

    a = HTMLNode("a", "This is a test link", "p", props)
    self.assertIsNotNone(a.children)
    self.assertIsNotNone(a.props)

  def test_props_to_html(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }

    node = HTMLNode("a", "This is a test link", None, props)
    properties_string = node.props_to_html()
    valid_string = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(properties_string, valid_string)


class TestLeafNode(unittest.TestCase):
  def test_repr(self):
    node = LeafNode("p", "What a strange world", {"class": "primary"})
    self.assertEqual(node.__repr__(), "LeafNode(Tag: p, Value: What a strange world, Props: {'class': 'primary'})")

  def test_values(self):
    node = LeafNode("p", "This is a paragraph of text")
    self.assertEqual(node.tag, "p")
    self.assertEqual(node.value, "This is a paragraph of text")
    self.assertEqual(node.props, {})

  def test_a(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }

    a = LeafNode("a", "Click me!", props)
    self.assertIsNotNone(a.props)

  def test_props_to_html(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }

    node = LeafNode("a", "This is a test link", props)
    properties_string = node.props_to_html()
    valid_string = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(properties_string, valid_string)

  def test_to_html(self):
    props = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }

    node = LeafNode("a", "Click me!", props)
    html_string = node.to_html()
    valid_string = '<a href="https://www.google.com" target="_blank">Click me!</a>'
    self.assertEqual(html_string, valid_string)


class TestParentNode(unittest.TestCase):
  def test_repr(self):
    node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),], {"class": "primary"})

    self.assertEqual(node.__repr__(), "ParentNode(Tag: p, Children: [LeafNode(Tag: b, Value: Bold text, Props: {}), LeafNode(Tag: None, Value: Normal text, Props: {})], Props: {'class': 'primary'})")
 
  def test_to_html_without_tag(self):
    node = ParentNode(None, [LeafNode("b", "Bold text")])
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_without_children(self):
    node = ParentNode("p", None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_with_children(self):
    node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
    child_nodes = node.to_html()
    html_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    self.assertEqual(child_nodes, html_output)

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )

  def test_headings(self):
      node = ParentNode("h2", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
      self.assertEqual(
          node.to_html(),
          "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
      )


if __name__ == "__main__":
    unittest.main()