import re
from textnode import TextNode, TextType


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.text_type_text)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text_type_text:
            new_nodes.append(node)
            continue
        # Split node text based on delimeter
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], TextType.text_type_text))
            else:
                new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text_type_text:
            new_nodes.append(node)
            continue
        original_text = node.text
        extracted_images = extract_markdown_images(original_text)
        if len(extracted_images) == 0:
            new_nodes.append(node)
            continue
        for extracted_image in extracted_images:
            sections = original_text.split(
                f"![{extracted_image[0]}]({extracted_image[1]})", 1
            )
            if len(sections) != +2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text_type_text))

            new_nodes.append(
                TextNode(
                    extracted_image[0],
                    TextType.text_type_image,
                    extracted_image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.text_type_text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text_type_text))
            new_nodes.append(TextNode(link[0], TextType.text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.text_type_text))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches



    
