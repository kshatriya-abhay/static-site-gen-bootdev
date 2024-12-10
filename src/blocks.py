from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    assert isinstance(block, str)
    default_type = BlockType.PARAGRAPH
    if is_heading(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.ULIST
    if is_ordered_list(block):
        return BlockType.OLIST
    return default_type

def is_heading(block):
    assert isinstance(block, str)
    for line in block.split("\n"):
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### ") or line.startswith("#### ") or line.startswith("##### ") or line.startswith("###### "):
            continue
        else:
            return False
    return True

def is_code_block(block):
    assert isinstance(block, str)
    lines = block.split("\n")
    if len(lines) < 3:
        return False
    if lines[0] == "```" and lines[-1] == "```":
        return True
    else:
        return False

def is_quote(block):
    assert isinstance(block, str)
    lines = block.split("\n")
    for line in lines:
        if line.startswith(">"):
            continue
        else:
            return False
    return True

def is_unordered_list(block):
    assert isinstance(block, str)
    lines = block.split("\n")
    for line in lines:
        if line.startswith("* ") or line.startswith("- "):
            continue
        else:
            return False
    return True

def is_ordered_list(block):
    assert isinstance(block, str)
    lines = block.split("\n")
    for i in range(len(lines)):
        num = i+1
        if lines[i].startswith(str(num) + ". "):
            continue
        else:
            return False
    return True