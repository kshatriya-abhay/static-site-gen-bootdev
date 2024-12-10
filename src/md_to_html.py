from blocks import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from node_conversion import text_node_to_html_node
import re

def markdown_to_html(text):
    blocks_list = markdown_to_blocks(text)
    child_nodes = []
    for block in blocks_list:
        nodes = block_to_htmlnode(block)
        
        child_nodes.append(nodes)
    return ParentNode(tag="div", children=child_nodes)

def block_to_htmlnode(text_block):
    block_type = block_to_block_type(text_block)
    if block_type == BlockType.HEADING:
        return heading_block_to_htmlnode(text_block)
    elif block_type == BlockType.CODE:
        return code_block_to_htmlnode(text_block)
    elif block_type == BlockType.QUOTE:
        return quote_block_to_htmlnode(text_block)
    elif block_type == BlockType.ULIST:
        return ulist_to_htmlnode(text_block)
    elif block_type == BlockType.OLIST:
        return olist_to_htmlnode(text_block)
    elif block_type == BlockType.PARAGRAPH:
        return paragraph_to_htmlnode(text_block)
    else:
        raise Exception("invalid block type")

def heading_block_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    nodes = []
    for line in text_block.split("\n"):
        heading_tag = ""
        if line.startswith("# "):
            heading_tag = "h1"
        elif line.startswith("## "):
            heading_tag = "h2"
        elif line.startswith("### "):
            heading_tag = "h3"
        elif line.startswith("#### "):
            heading_tag = "h4"
        elif line.startswith("##### "):
            heading_tag = "h5"
        elif line.startswith("###### "):
            heading_tag = "h6"
        else:
            raise Exception("invalid heading block")
        line_text = line.lstrip("#").lstrip()
        node = text_to_htmlnode(line_text, heading_tag)
        nodes.append(node)
    return nodes

def code_block_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    code_block = text_block.strip("```")
    return text_to_htmlnode(code_block, "code")

def quote_block_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    # remove the quote prefix ('> ') from all the lines
    quote_block = "\n".join([line.lstrip("> ") for line in text_block.split("\n")])
    return text_to_htmlnode(quote_block, "blockquote")

def ulist_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    list_items = []
    for text in text_block.split("\n"):
        list_item_text = ""
        if text.startswith("* "):
            list_item_text = text.lstrip("* ")
        elif text.startswith("- "):
            list_item_text = text.lstrip("- ")
        else:
            raise Exception("invalid unordered list block")
        list_items.append(list_item_text)
    ul = HTMLNode("ul")
    ul.children = [text_to_htmlnode(text, "li") for text in list_items]
    return ul

def olist_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    list_items = []
    i = 1
    for text in text_block.split("\n"):
        words = text.split(" ")
        index_word = words[0]
        if len(re.findall(r"[0-9]+\.", index_word)) != 1:
            raise Exception("invalid ordered list block")
        list_item_words = words[1:]
        list_item_text = " ".join(list_item_words)
        list_items.append(list_item_text)
    ol = HTMLNode("ol")
    ol.children = [text_to_htmlnode(text, "li") for text in list_items]
    return ol

def paragraph_to_htmlnode(text_block):
    assert isinstance(text_block, str)
    return text_to_htmlnode(text_block, "p")

def text_to_htmlnode(text, tag):
    node = HTMLNode(tag)
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))
    node.children = leaf_nodes
    return node