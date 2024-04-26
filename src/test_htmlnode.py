import unittest

from htmlnode import HTMLNode, LeafNode, TagType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode(
            tag=TagType.bold,
            value="This is bold text",
            props={"href": "https://www.google.com"},
        )
        html_node2 = HTMLNode(
            tag=TagType.bold,
            value="This is bold text",
            props={"href": "https://www.google.com"},
        )
        self.assertEqual(html_node, html_node2)

    def test_repr(self):
        html_node = HTMLNode(
            tag="h", value="This is text", props={"href": "https://www.google.com"}
        )
        self.assertEqual(
            "HTMLNode(h, This is text, None, {'href': 'https://www.google.com'})",
            repr(html_node),
        )

    def test_pros_to_html(self):
        html_node = HTMLNode(
            tag="h",
            value="This is text",
            props={"class": "greeting", "href": "https://www.google.com"},
        )
        self.assertEqual(
            html_node.props_to_html(), ' class="greeting" href="https://www.google.com"'
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
