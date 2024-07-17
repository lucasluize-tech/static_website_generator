import unittest
from helper import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode


class TestHelperFunctions(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        code_node = TextNode("this is a text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([code_node], "`", "code")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "this is a text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, "code")
        self.assertAlmostEqual(new_nodes[2].text, " word")

        bold_node = TextNode("this is a text with a **bold delimiter** word", "text")
        new_nodes = split_nodes_delimiter([bold_node], "**", "bold")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "this is a text with a ")
        self.assertEqual(new_nodes[1].text, "bold delimiter")
        self.assertEqual(new_nodes[1].text_type, "bold")
        self.assertAlmostEqual(new_nodes[2].text, " word")

        italic_node = TextNode("this is a text with a *italic delimiter* word", "text")
        new_nodes = split_nodes_delimiter([italic_node], "*", "italic")
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "this is a text with a ")
        self.assertEqual(new_nodes[1].text, "italic delimiter")
        self.assertEqual(new_nodes[1].text_type, "italic")
        self.assertAlmostEqual(new_nodes[2].text, " word")

    def test_extract_markdown_images(self):
        test = extract_markdown_images(
            "this is a text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertEqual(len(test), 2)
        self.assertEqual(test[0][0], "rick roll")
        self.assertEqual(test[0][1], "https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(test[1][0], "obi wan")
        self.assertEqual(test[1][1], "https://i.imgur.com/fJRm4Vk.jpeg")

    def test_extract_markdown_links(self):
        test2 = extract_markdown_links(
            "this is a text with a [link](https://www.google.com) and [another link](https://www.example.com)"
        )
        self.assertEqual(len(test2), 2)
        self.assertEqual(test2[0][0], "link")
        self.assertEqual(test2[0][1], "https://www.google.com")
        self.assertEqual(test2[1][0], "another link")
        self.assertEqual(test2[1][1], "https://www.example.com")

    def test_split_nodes_image(self):
        text_node = TextNode(
            "this is a text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text",
        )
        new_nodes = split_nodes_image([text_node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "this is a text with a ")
        self.assertEqual(new_nodes[1].text, "rick roll")
        self.assertEqual(new_nodes[1].text_type, "image")
        self.assertEqual(new_nodes[1].url, "https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[3].text, "obi wan")
        self.assertEqual(new_nodes[3].text_type, "image")
        self.assertEqual(new_nodes[3].url, "https://i.imgur.com/fJRm4Vk.jpeg")

    def test_split_nodes_image(self):
        text_node = TextNode(
            "this is a text with a [link](https://www.google.com) and [another link](https://www.example.com)",
            "text",
        )
        new_nodes = split_nodes_link([text_node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "this is a text with a ")
        self.assertEqual(new_nodes[1].text, "link")
        self.assertEqual(new_nodes[1].text_type, "link")
        self.assertEqual(new_nodes[1].url, "https://www.google.com")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[2].text_type, "text")
        self.assertEqual(new_nodes[3].text, "another link")
        self.assertEqual(new_nodes[3].text_type, "link")
        self.assertEqual(new_nodes[3].url, "https://www.example.com")

    def test_text_to_textnodes(self):
        test_input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(test_input)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, "bold")
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, "italic")
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, "code")
        self.assertEqual(nodes[7].text, "obi wan image")
        self.assertEqual(nodes[7].text_type, "image")
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].text_type, "link")
