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
        

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        
        if type(node) != TextNode:
            raise Exception("Not a TextNode!")
        if node.text_type != TextType.TEXT:
            new_nodes.extend(node)
        
        split_nodes_string = node.text.split(delimiter)
        split_node = []

        if len(split_nodes_string) % 2 == 0:
            raise ValueError("invalid markdown, did you forget to close a section?")

        for i in range(len(split_nodes_string)):
            if split_nodes_string[i] == '':
                continue
            if i % 2 == 0:
                split_node.append(TextNode(split_nodes_string[i], TextType.TEXT))
            else:
                split_node.append(TextNode(split_nodes_string[i], text_type))



        #split_node = [
        #    TextNode(split_nodes_string[0], TextType.TEXT),
        #    TextNode(split_nodes_string[1], text_type),
        #    TextNode(split_nodes_string[2], TextType.TEXT)
        #]
        new_nodes.extend(split_node)
    
        
        
    return new_nodes


def main():

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    

if __name__ == "__main__":
    main()