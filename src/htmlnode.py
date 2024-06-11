class HTMLNode:
    def __init__(self, tag='div', value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children
    
    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self):
        return ' '.join(f'{k}="{v}"' for k, v in self.props.items()) if self.props else ""

    def __repr__(self):
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.props.items()) if self.props else ""
        if attrs:
            attrs = ' ' + attrs
        
        children = ''.join(str(c) for c in self.children ) if self.children else "" 
        return f'<{self.tag}{attrs}>{self.value}{children}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return f'{self.value}'
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children ,props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        children = ''.join(c.to_html() for c in self.children )
        if self.props is None:
            return f'<{self.tag}>{children}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{children}</{self.tag}>'