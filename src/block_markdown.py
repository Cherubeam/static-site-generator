def markdown_to_blocks(markdown):
  block_strings = []
  split_blocks = markdown.split("\n\n")

  for block in split_blocks:
    if block != "":
      block_strings.append(block.strip())
  
  return block_strings

def block_to_block_type(markdown):    
  if markdown.startswith("#"):
    for i in range(1, 6):
      mdheading = f"{i * '#'} "
      print(f"MDHEADING:\n{mdheading}")
      if markdown.startswith(mdheading):
        return "heading"
 
    raise Exception("Invalid markdown heading")
  elif markdown.startswith("```") and markdown.endswith("```"):
    return "code"
  elif markdown.startswith(">"):
    return "quote"
  elif markdown.startswith("* ") or markdown.startswith("- "):
    return "unordered_list"
  elif markdown[0].isdigit() and markdown[1:3] == ". ":
    return "ordered_list"
  else:
    return "paragraph"