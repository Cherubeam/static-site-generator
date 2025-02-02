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
    #print(f"PUBLIC DIRECTORY DELETED AND RE-CREATED")

  # Copy files from static directory to public directory
  content_static_dir = os.listdir(static_dir)
  if len(content_static_dir) != 0:
    print(f"STATIC DIRECTORY CONTAINS FILES:\n{content_static_dir}") 
  
    #path = os.path.join(public_dir, content_static_dir[0])
    #print(f"PATH:\n{path}")
    path = os.path.join(static_dir, content_static_dir[0])
    shutil.copy(path, public_dir)

  # For each listed item in content_static_dir check if it is a file or a directory
  ## If it is a file copy it in the current directory level
  ## Else, enter directory


  # try:
  #   shutil.copy(static_dir, public_dir)


main()