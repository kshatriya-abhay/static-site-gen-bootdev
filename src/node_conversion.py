from textnode import TextNode
from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
    assert isinstance(text_node, TextNode)
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        props = {}
        props["href"] = text_node.url
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props = {}
        props["src"] = text_node.url
        props["alt"] = text_node.text
        return LeafNode("img", "", props)
    else:
        raise Exception("invalid text type")
    
    