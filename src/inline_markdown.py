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
      images = extract_markdown_images(node)
      if images == []:
        return [node]
      
    pass
      



