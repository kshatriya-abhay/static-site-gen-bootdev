import os
from pathlib import Path
from md_to_html import markdown_to_html

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for listitem in os.listdir(dir_path_content):
        itempath = os.path.join(dir_path_content, listitem)
        if os.path.isfile(itempath):
            dest_filename = os.path.join(dest_dir_path, md_to_html_filename(listitem))
            generate_page(itempath, template_path, dest_filename)
        else:
            generate_pages_recursive(itempath, template_path, os.path.join(dest_dir_path, listitem))

def generate_page(from_path, template_path, dest_path):
    assert isinstance(dest_path, str)
    print("Generating page from %s to %s using %s", from_path, dest_path, template_path)
    from_txt = Path(from_path).read_text()
    template_txt = Path(template_path).read_text()
    html_txt = markdown_to_html(from_txt).to_html()
    title = extract_title(from_txt)
    generated_html = template_txt.replace("{{ Title }}", title).replace("{{ Content }}", html_txt)
    dir = dest_path.split("/")[:-1]
    dir = "/".join(dir)
    if dir != "" and not os.path.exists(dir):
        os.mkdir(dir)
    dest_file = open(dest_path, "w")
    dest_file.write(generated_html)
    dest_file.close()

def extract_title(markdown):
    assert isinstance(markdown, str)
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("No heading found in markdown")

def md_to_html_filename(filename):
    assert isinstance(filename, str)
    split_str = filename.split('.')
    if len(split_str) == 1:
        return filename + ".html"
    split_str[-1] = "html"
    return ".".join(split_str)