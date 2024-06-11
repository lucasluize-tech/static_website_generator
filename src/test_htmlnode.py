import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode('div')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_props_to_html(self):
        node = HTMLNode('div', props={"class": "foo", "id": "bar"})
        self.assertEqual(node.props_to_html(), 'class="foo" id="bar"')
        
        
    def test_repr_with_children(self):
        node = HTMLNode('div')
        node.children = [HTMLNode('p', children=[HTMLNode('span')])]
        self.assertEqual(str(node), '<div>None<p>None<span>None</span></p></div>')

    def test_repr_no_children(self):
        node = HTMLNode('div')
        self.assertEqual(str(node), '<div>None</div>')

    def test_repr_no_props(self):
        node = HTMLNode('div')
        self.assertEqual(str(node), '<div>None</div>')
        
    def test_repr_with_props(self):
        node = HTMLNode('div', props={"class": "foo"})
        self.assertEqual(str(node), '<div class="foo">None</div>')
        
    def test_leaf_node_without_tag(self):
        node = LeafNode(None, 'text')
        self.assertEqual(node.to_html(), 'text')

    def test_leaf_node_with_tag(self):
        node = LeafNode('p', 'text')
        self.assertEqual(node.to_html(), '<p>text</p>')

    def test_leaf_node_with_props(self):
        node = LeafNode('p', 'text', {'class': 'test'})
        self.assertEqual(node.to_html(), '<p class="test">text</p>')
    
    def test_leaf_node_no_children(self):
        node = LeafNode('div', None)
        self.assertEqual(node.children, None)

    def test_parent_node_without_props(self):
        children = [LeafNode('p', 'text')]
        node = ParentNode('div', children)
        self.assertEqual(node.to_html(), '<div><p>text</p></div>')

    def test_parent_node_with_props(self):
        children = [LeafNode('p', 'text')]
        node = ParentNode('div', children, {'class': 'test'})
        self.assertEqual(node.to_html(), '<div class="test"><p>text</p></div>')

    def test_leaf_node_without_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode('p', None)
            node.to_html()

    def test_parent_node_without_tag(self):
        with self.assertRaises(ValueError):
            children = [LeafNode('p', 'text')]
            node = ParentNode(None, children)
            node.to_html()