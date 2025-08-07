from enum import Enum

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if self.props != None:
            for key in self.props:
                output += f' {key}=\"{self.props[key]}"'
        return output
        

    def __repr__(self):
        print(f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props_to_html()}")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        
        if self.tag == None:
            return f"{self.value}"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag cannot be empty")
        elif self.children == None:
            raise ValueError("Chldren cannot be empty")
        
        childnodes = "" 
        for node in self.children:
            childnodes += node.to_html()

        print(f"<{self.tag}>{childnodes}</{self.tag}>")
        return f"<{self.tag}{self.props_to_html()}>{childnodes}</{self.tag}>"

    def __repr__(self):
        return f'ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props}, )'