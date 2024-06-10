class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children
    
    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self):
        return ' '.join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        attrs = ' '.join(f'{k}="{v}"' for k, v in self.props.items()) if self.props else ""
        if attrs:
            attrs = ' ' + attrs
        
        children = ''.join(str(c) for c in self.children ) if self.children else "" 
        return f'<{self.tag}{attrs}>{self.value}{children}</{self.tag}>'

    