from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    text_node = TextNode("Hello World", "bold", "https://www.example.com")
    print(text_node)
    html_node = HTMLNode("button", "Click me", props={"href": "https://www.example.com", "target": "_blank", "class": "btn btn-primary"})
    print(html_node.props_to_html())
    print(html_node)
    
    leaf1 = LeafNode("p", "This is a paragraph of text.")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf1.to_html())
    print(leaf2.to_html())
    
    parent_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    print(parent_node.to_html())


    
if __name__ == "__main__":
    main()