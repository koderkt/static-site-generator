import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(
            "This is a text node", TextType.text_type_bold, "http://localhost:8888"
        )
        node2 = TextNode(
            "This is a text node", TextType.text_type_bold, "http://localhost:8888"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextType.text_type_text, "https://www.boot.dev"
        )
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html(self):
        node = TextNode(
            "This is a text node", TextType.text_type_bold, "https://www.boot.dev"
        )

        self.assertEqual(
            text_node_to_html_node(node), LeafNode("b", "This is a text node")
        )


if __name__ == "__main__":
    unittest.main()
