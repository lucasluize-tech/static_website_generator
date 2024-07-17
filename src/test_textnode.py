import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
        
    def test_node_with_url(self):
        node = TextNode("This is a text node", "bold", "https://www.example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.example.com)")
        
    def test_node_type_string(self):
        node = TextNode("This is a text node","", "https://www.example.com")
        self.assertEqual(type(node.text_type), type("string"))
        self.assertEqual(type(node.text), type("string"))
        self.assertEqual(type(node.url), type("string"))
        
    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node image", "image", "https://www.example.com")
        self.assertEqual(node.text, "This is a text node image")
        self.assertEqual(node.text_type, "image")
        self.assertEqual(node.url, "https://www.example.com")
        test_img_node = text_node_to_html_node(node)
        self.assertEqual(test_img_node.to_html(), f'<img src="{node.url}" alt="{node.text}">None</img>')
        
        node = TextNode("This is a text node", "bold")
        test_text_node = text_node_to_html_node(node)
        self.assertEqual(test_text_node.to_html(), f'<b>{node.text}</b>')
        
        node = TextNode("This is a text node", "italic")
        test_italic_node = text_node_to_html_node(node)
        self.assertEqual(test_italic_node.to_html(), f'<i>{node.text}</i>')
        
        node = TextNode("This is a text node", "link", "https://www.example.com")
        test_link_node = text_node_to_html_node(node)
        self.assertEqual(test_link_node.to_html(), f'<a href="{node.url}">{node.text}</a>')


if __name__ == "__main__":
    unittest.main()