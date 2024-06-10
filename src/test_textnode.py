import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()