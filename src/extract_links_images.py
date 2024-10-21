import re

def extract_markdown_links(text):
    assert isinstance(text, str)
    url_list = re.findall(r"(?<!\!)\[.*?\]\(\w+\:\/\/[a-zA-Z0-9_\/\.]+\)", text)
    return get_tuples(url_list)

def extract_markdown_images(text): 
    image_patterns = re.findall(r"\!\[.*?\]\(\w+\:\/\/[a-zA-Z0-9_\/\.]+\)", text)
    return get_tuples(image_patterns)

def get_tuples(pattern_list):
    list = []
    for pattern in pattern_list:
        assert isinstance(pattern, str)
        text_start = pattern.find("[")
        text_end = pattern.find("]")
        text = pattern[text_start+1:text_end]
        url_start = pattern.find("(")
        url_end = pattern.find(")")
        url = pattern[url_start+1:url_end]
        list.append(tuple([text, url]))
    return list 