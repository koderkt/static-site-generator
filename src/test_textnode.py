import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.text_type_bold, "http://localhost:8888")
        node2 = TextNode("This is a text node", TextType.text_type_bold, "http://localhost:8888")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node",TextType.text_type_text , "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
   
if __name__ == "__main__":
    unittest.main()
