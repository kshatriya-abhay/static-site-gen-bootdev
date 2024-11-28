def markdown_to_blocks(markdown):
    assert isinstance(markdown, str)
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
    while "" in blocks:
        blocks.remove("")
    return blocks
        