from textnode import TextNode
import re

img_regex = re.compile(r"!\[([^\]]+)\]\(([^)]+)\)")
link_regex = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    demiliters = {"`": "code", "**": "bold", "*": "italic"}
    if delimiter not in demiliters:
        raise Exception(f"Invalid delimiter: {delimiter}")
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text:
            split_text = node.text.split(delimiter)
            for i, text in enumerate(split_text):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, "text", node.url))
                else:
                    new_nodes.append(TextNode(text, text_type, node.url))
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    images = []
    for match in img_regex.finditer(text):
        images.append((match.group(1), match.group(2)))
    return images


def extract_markdown_links(text):
    links = []
    for match in link_regex.finditer(text):
        links.append((match.group(1), match.group(2)))
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images:
            for i, img in enumerate(images):
                sections = node.text.split(f"![{img[0]}]({img[1]})", 1)
                if i == 0:
                    new_nodes.append(TextNode(sections[0], "text"))
                    new_nodes.append(TextNode(img[0], "image", img[1]))
                    node.text = sections[i + 1]
                else:
                    new_nodes.append(TextNode(sections[0], "text"))
                    new_nodes.append(TextNode(img[0], "image", img[1]))
        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links:
            for i, link in enumerate(links):
                sections = node.text.split(f"[{link[0]}]({link[1]})", 1)
                if i == 0:
                    new_nodes.append(TextNode(sections[0], "text"))
                    new_nodes.append(TextNode(link[0], "link", link[1]))
                    node.text = sections[i + 1]
                else:
                    new_nodes.append(TextNode(sections[0], "text"))
                    new_nodes.append(TextNode(link[0], "link", link[1]))
        else:
            new_nodes.append(node)

    return new_nodes


def text_to_textnodes(text):
    nodes = []
    nodes_bold = split_nodes_delimiter([TextNode(text, "text")], "**", "bold")
    if nodes_bold:
        nodes.append(nodes_bold[0])
        nodes.append(nodes_bold[1])
        text = nodes_bold[2].text

    nodes_italic = split_nodes_delimiter([TextNode(text, "text")], "*", "italic")
    if nodes_italic:
        nodes.append(nodes_italic[0])
        nodes.append(nodes_italic[1])
        text = nodes_italic[2].text

    nodes_code = split_nodes_delimiter([TextNode(text, "text")], "`", "code")
    if nodes_code:
        nodes.append(nodes_code[0])
        nodes.append(nodes_code[1])
        text = nodes_code[2].text

    nodes_image = split_nodes_image([TextNode(text, "text")])
    if nodes_image:
        nodes.append(nodes_image[0])
        nodes.append(nodes_image[1])
        text = text.split(f"![{nodes_image[1].text}]({nodes_image[1].url})", 1)[1]

    nodes_link = split_nodes_link([TextNode(text, "text")])
    if nodes_link:
        nodes.append(nodes_link[0])
        nodes.append(nodes_link[1])

    return nodes
