from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {'href':text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img', '', {'src':text_node.url, 'alt':text_node.text})
    else:
        raise Exception("invalid type")
        


def main():
    testnode = TextNode("the quick brown fox", TextType.BOLD)
    print(testnode)
    print("hello world")

if __name__ == "__main__":
    main()