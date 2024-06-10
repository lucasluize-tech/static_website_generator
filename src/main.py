from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("Hello World", "bold", "https://www.example.com")
    print(text_node)
    html_node = HTMLNode("button", "Click me", props={"href": "https://www.example.com", "target": "_blank", "class": "btn btn-primary"})
    print(html_node.props_to_html())
    print(html_node)
    
if __name__ == "__main__":
    main()