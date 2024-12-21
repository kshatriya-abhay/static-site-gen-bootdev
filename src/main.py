from textnode import TextNode
import os
import shutil
from generate_page import generate_pages_recursive

def main():
    print("hello world")
    copy_static_to_public()

def copy_static_to_public():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    if os.path.exists("./static"):
        print("Copying static files to public dir...")
        shutil.copytree("./static", "./public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()