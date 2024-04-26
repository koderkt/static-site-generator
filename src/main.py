from htmlnode import HTMLNode
from textnode import TextNode 

def main():
  # text_node = TextNode("This is a text node", "bold", "http://localhost:8080")
  # print(text_node.__repr__)

  html_node = HTMLNode(
            tag="h",
            value="This is text",
            props={
                "class": "greeting",
                "href": "https://www.google.com"
                }
          )
  # print(html_node.__repr__)
  print(html_node.props_to_html())

main()
