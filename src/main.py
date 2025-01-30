import os

from textnode import TextNode

def main():
  node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(node)
  copy_static_to_public()

def copy_static_to_public():
  if os.path.exists("./static") and os.path.exists("./public"):
    print(f"PATH EXISTS")
    print(os.listdir("./static"))
  else:
    print(f"PATH DOES NOT EXISTS")

main()