from textnode import TextNode
import os
import shutil
import sys
from generate_page import generate_pages_recursive

def main():
    copy_static_to_public()

def copy_static_to_public():
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    if os.path.exists("./static"):
        print("Copying static files to docs dir...")
        shutil.copytree("./static", "./docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()