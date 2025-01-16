def markdown_to_blocks(markdown):
  block_strings = []
  split_blocks = markdown.split("\n\n")

  for block in split_blocks:
    if block != "":
      block_strings.append(block.strip())
  
  return block_strings