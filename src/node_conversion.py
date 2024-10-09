from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    assert isinstance(text_node, TextNode)
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        props = {}
        props["href"] = text_node.url
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == "image":
        props = {}
        props["src"] = text_node.url
        props["alt"] = text_node.text
        return LeafNode("img", "", props)
    else:
        raise Exception("invalid text type")
    
    