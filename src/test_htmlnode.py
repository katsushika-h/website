
import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()

