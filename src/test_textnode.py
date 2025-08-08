import unittest

from textnode import TextNode, TextType
from main import split_nodes_delimiter



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_URL_equal(self):
        node = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev/")
        self.assertEqual(node, node2)
    
    def test_URL_not_equal(self):
        node = TextNode("This is a URL node", TextType.LINK, "https://www.google.com/")
        node2 = TextNode("This is a URL node", TextType.LINK, "https://www.boot.dev/")
        self.assertNotEqual(node, node2)


    #============ DELIMITER TESTS ============

    def test_bold_delimiter(self):
        node = TextNode("This is a text with a **bold block** word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], '**' , TextType.BOLD)
        print(new_node)
        self.assertEqual(new_node, [TextNode("This is a text with a ", TextType.TEXT, None), 
                                TextNode("bold block", TextType.BOLD, None), 
                                TextNode(" word", TextType.TEXT, None)])
        
    def test_italic_delimiter(self):
        node = TextNode("This is a text with a *italic block* word", TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*' , TextType.ITALIC)
        print(new_node)
        self.assertEqual(new_node, [TextNode("This is a text with a ", TextType.TEXT, None), 
                                TextNode("italic block", TextType.ITALIC, None), 
                                TextNode(" word", TextType.TEXT, None)])
        
    #def test_exception_delimiter(self):
     #   node = 'This is an **invalid** node'
      #  self.assertRaises(Exception, split_nodes_delimiter(), [node], '**', TextType.BOLD)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        print('\n')
        print("test_delim_bold_double: \n")
        print(*new_nodes, sep='\n')
        print('\n')
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()