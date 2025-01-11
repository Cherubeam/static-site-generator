from textnode import TextNode, TextType
from extract_links_images_markdown import extract_markdown_images, extract_markdown_links

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
    if images == []:
      return [node]

    sections = []
    
    for i, image in enumerate(images):
      (image_alt, image_link) = image
      if sections == []:
        sections = node.text.split(f"![{image_alt}]({image_link})", 1)
      else:
        sections = sections[1].split(f"![{image_alt}]({image_link})", 1)

      new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(image_alt, TextType.LINK, image_link))

  return new_nodes   

def split_nodes_links(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    links = extract_markdown_links(node.text)
    if links == []:
      return [node]

    sections = []
    
    for i, link in enumerate(links):
      (link_text, url) = link
      if sections == []:
        sections = node.text.split(f"[{link_text}]({url})", 1)
      else:
        sections = sections[1].split(f"[{link_text}]({url})", 1)

      new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(link_text, TextType.LINK, url))

  return new_nodes

