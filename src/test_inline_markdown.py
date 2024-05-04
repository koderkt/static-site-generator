import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    TextType,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text_type_text),
                TextNode("bolded", TextType.text_type_bold),
                TextNode(" word", TextType.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text_type_text),
                TextNode("bolded", TextType.text_type_bold),
                TextNode(" word and ", TextType.text_type_text),
                TextNode("another", TextType.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text_type_text),
                TextNode("bolded word", TextType.text_type_bold),
                TextNode(" and ", TextType.text_type_text),
                TextNode("another", TextType.text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextType.text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text_type_text),
                TextNode("italic", TextType.text_type_italic),
                TextNode(" word", TextType.text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode(
            "This is text with a `code block` word", TextType.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text_type_text),
                TextNode("code block", TextType.text_type_code),
                TextNode(" word", TextType.text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://bit.ly/4dbFaaV)"
        )
        self.assertListEqual([("image", "https://bit.ly/4dbFaaV")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://google.com) and [another link](https://blog.google.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://google.com"),
                ("another link", "https://blog.google.com"),
            ],
            matches,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://bit.ly/4dbFaaV)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text_type_text),
                TextNode("image", TextType.text_type_image, "https://bit.ly/4dbFaaV"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.text_type_image,
                    "https://www.example.com/image.png",
                ),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://bit.ly/4dbFaaV) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text_type_text),
                TextNode("image", TextType.text_type_image, "https://bit.ly/4dbFaaV"),
                TextNode(" and another ", TextType.text_type_text),
                TextNode(
                    "second image",
                    TextType.text_type_image,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and [another link](https://blog.google.com) with text that follows",
            TextType.text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text_type_text),
                TextNode("link", TextType.text_type_link, "https://google.com"),
                TextNode(" and ", TextType.text_type_text),
                TextNode(
                    "another link", TextType.text_type_link, "https://blog.google.com"
                ),
                TextNode(" with text that follows", TextType.text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://bit.ly/4dbFaaV) and a [link](https://google.com)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.text_type_text),
                TextNode("text", TextType.text_type_bold),
                TextNode(" with an ", TextType.text_type_text),
                TextNode("italic", TextType.text_type_italic),
                TextNode(" word and a ", TextType.text_type_text),
                TextNode("code block", TextType.text_type_code),
                TextNode(" and an ", TextType.text_type_text),
                TextNode("image", TextType.text_type_image, "https://bit.ly/4dbFaaV"),
                TextNode(" and a ", TextType.text_type_text),
                TextNode("link", TextType.text_type_link, "https://google.com"),
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
