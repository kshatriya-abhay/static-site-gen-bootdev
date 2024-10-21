from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        assert isinstance(node, TextNode)
        node_text = node.text
        if node_text == None:
            continue
        assert isinstance(node_text, str)
        split_text = node_text.split(delimiter)
        if len(split_text) == 1:
            new_nodes.append(node)
        elif len(split_text) % 2 == 1:
            split_nodes = get_split_nodes(split_text, text_type)
            new_nodes.extend(split_nodes)
        else:
            raise ValueError("Odd number of delimiters in the input")
    return new_nodes

def get_split_nodes(split_text, text_type):
    nodes = []
    for text in split_text:
        if text == '':
            continue
        new_node = TextNode(text=text, text_type=TextType.TEXT)
        index = split_text.index(text)
        # The text on odd numbered index needs the actual text type
        if index % 2 != 0:
            new_node.text_type = text_type
        nodes.append(new_node)
    return nodes