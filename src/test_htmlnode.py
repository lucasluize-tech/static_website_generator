import unittest

from htmlnode import HTMLNode

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