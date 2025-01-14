import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue

    sections = node.text.split(delimiter)

    if len(sections) % 2 == 0:
        raise ValueError(f"Invalid markdown, missing closing '{delimiter}'")

    split_nodes = []
    for i, section in enumerate(sections):
      if section == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(section, TextType.TEXT))
      else:
        split_nodes.append(TextNode(section, text_type))

    new_nodes.extend(split_nodes)

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue

    images = extract_markdown_images(node.text)

    if not images:
      new_nodes.append(node)
      continue

    remaining_text = node.text
    for (image_alt, image_link) in images:
      parts = remaining_text.split(f"![{image_alt}]({image_link})", 1)
      text_before = parts[0]
      remaining_text = parts[1] if len(parts) > 1 else ""

      if text_before.strip():
        new_nodes.append(TextNode(text_before, TextType.TEXT))

      new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

    if remaining_text.strip():
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))

  return new_nodes

def split_nodes_links(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue

    links = extract_markdown_links(node.text)

    if not links:
      new_nodes.append(node)
      continue

    remaining_text = node.text
    for (link_text, link_url) in links:
      parts = remaining_text.split(f"[{link_text}]({link_url})", 1)
      text_before = parts[0]
      remaining_text = parts[1] if len(parts) > 1 else ""

      if text_before.strip():
        new_nodes.append(TextNode(text_before, TextType.TEXT))

      new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

    if remaining_text.strip():
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))

  return new_nodes

def extract_markdown_images(text):
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches

def extract_markdown_links(text):
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  return matches

def text_to_textnodes(text):
  new_nodes = []
  node = TextNode(text, TextType.TEXT)
  new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD) 
  new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
  new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
  new_nodes = split_nodes_image(new_nodes)
  new_nodes = split_nodes_links(new_nodes)
  return new_nodes