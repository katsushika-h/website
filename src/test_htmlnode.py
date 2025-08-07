
import unittest
from htmlnode import *
from textnode import *
from main import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    #def test_eq(self):
    #    node = HTMLNode("tag","value", "children", "props")
    #    node2 = HTMLNode("tag","value", "children", "props")
    #    self.assertEqual(node, node2)

    #def test_not_eq(self):
    #    node = HTMLNode("tag2","value2", "children2", "props2")
    #    node2 = HTMLNode("tag","value", "children", "props")
    #    self.assertNotEqual(node, node2)

    def test_props_to_html_blank(self):
        node = HTMLNode("p","value", None,)
        self.assertEqual(node.props_to_html(), "")

    def test_pth_one_eg(self):
        node = HTMLNode("p",None,None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_pth_two_eg(self):
        node = HTMLNode("p",None,None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"' )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

   # def test_tags(self):
    #    childnode = LeafNode("b", "child")
     #   pnode = ParentNode('a', childnode, 'google.com')
      #  self.assertEqual(pnode.to_html(), '<a href="google.com"><b>child<b></a>')

    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    if __name__ == "__main__":
        unittest.main()
         

