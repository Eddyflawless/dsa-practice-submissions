
from pprint import pprint

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    """
        adding a node is the same as adding 
        child
    """
    def addNode(self,node):
        node.parent = self
        # child/node need to know 
        # who its parent is
        self.children.append(node)
        return self

    def addNodes(self,nodes=[]):
        # children need to know 
        # who their parents are
        for node in nodes:
            node.parent = self
            self.children.append(node)

        return self    

    """

    """
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


    def printTree(self):
        spaces = " " * self.getLevel() * 3
        prefix = spaces + "|----" if self.parent else " "
        print(prefix + self.data)
        for node in self.children:
            node.printTree()

    

if __name__ == '__main__':

    # root node
    root = TreeNode("Televisions")
    root.addNodes([
        TreeNode("Samsung").addNodes([
            TreeNode("Samsung HD 48 inch"),
            TreeNode("Samsung UHD 32 inch"),
            TreeNode("Samsung UHD 42 inch"),
            TreeNode("Samsung UHD 61.2 inch"),
        ]),
        TreeNode("TLC").addNode(TreeNode("TLC HD 48 inch")),
        TreeNode("Sony"),
    ])

    root.printTree()