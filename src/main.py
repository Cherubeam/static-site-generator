import shutil
import os

from textnode import TextNode

def main():
  node = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(node)
  copy_static_to_public()


def copy_static_to_public():
  static_dir = "./static"
  public_dir = "./public"

  # Create public directory if it does not exist
  if not os.path.exists(public_dir):
    os.mkdir(public_dir)

  # Delete public directory if it is not empty
  content_public_dir = os.listdir(public_dir)
  if len(content_public_dir) != 0:
    print(f"PUBLIC DIRECTORY CONTAINS FILES:\n{content_public_dir}")
    shutil.rmtree(public_dir)

  # try:
  #   shutil.copy(static_dir, public_dir)


main()