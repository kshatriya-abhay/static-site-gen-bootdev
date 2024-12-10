from textnode import TextNode, TextType
from extract_links_images import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    return split_nodes(old_nodes, TextType.IMAGE, extract_markdown_images, make_image_markdown_from_tuple)

def split_nodes_link(old_nodes):
    return split_nodes(old_nodes, TextType.LINK, extract_markdown_links, make_url_markdown_from_tuple)

def split_nodes(old_nodes, extracted_text_type, extract_markdown_fn, markdown_text_from_tuple_fn):
    new_nodes = []
    for node in old_nodes:
        assert isinstance(node, TextNode)
        node_text = node.text
        if node_text == None:
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        assert isinstance(node_text, str)
        image_tuples = extract_markdown_fn(node_text)
        if len(image_tuples) == 0:
            new_nodes.append(node)
            continue
        last_end = 0
        for image_tuple in image_tuples:
            assert isinstance(image_tuple, tuple)
            assert len(image_tuple) == 2
            image_link = markdown_text_from_tuple_fn(image_tuple)
            start = node_text.find(image_link)
            end = start + len(image_link)
            if last_end < start:
                new_nodes.append(TextNode(node_text[last_end:start], TextType.TEXT))
            new_nodes.append(TextNode(image_tuple[0], extracted_text_type, image_tuple[1]))
            last_end = end
        
        if last_end < len(node_text):
            new_nodes.append(TextNode(node_text[last_end:], TextType.TEXT))
        
    return new_nodes

def make_image_markdown_from_tuple(t):
    assert isinstance(t, tuple)
    assert len(t) == 2
    return "![" + t[0] + "](" + t[1] + ")"

def make_url_markdown_from_tuple(t):
    assert isinstance(t, tuple)
    assert len(t) == 2
    return "[" + t[0] + "](" + t[1] + ")"