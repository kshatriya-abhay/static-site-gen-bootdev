class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other) -> bool:
        assert isinstance(other, HTMLNode)
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attributes = ""
        if self.props is not None:
            for key in self.props:
                attributes += f" {key}=\"{self.props[key]}\""
        return attributes
    
