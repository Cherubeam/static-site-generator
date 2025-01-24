block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
  block_strings = []
  split_blocks = markdown.split("\n\n")

  for block in split_blocks:
    if block != "":
      block_strings.append(block.strip())
  
  return block_strings


def block_to_block_type(block):
  lines = block.split("\n")

  if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
    return block_type_heading
  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
    return block_type_code
  if block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return block_type_paragraph
    return block_type_quote
  if block.startswith("* "):
    for line in lines:
      if not line.startswith("* "):
        return block_type_paragraph
      return block_type_ulist
  if block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return block_type_paragraph
      return block_type_ulist
  if block.startswith("1. "):
    i = 1
    for line in lines:
      if not line.startswith(f"{i}. "):
        return block_type_paragraph
      i += 1
      return block_type_olist
  return block_type_paragraph


def markdown_to_html_node(markdown):
  split_blocks = markdown_to_blocks(markdown)

  collected_block_types = []

  for block in split_blocks:
    block_type = block_to_block_type(block)
    collected_block_types.append(block_type)
    
  return collected_block_types