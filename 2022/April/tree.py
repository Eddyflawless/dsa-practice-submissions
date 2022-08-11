class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:  

    def preOrder(self, node):  

        print(node.data) 
        self.preOrder(node.left)
        self.preOrder(node.right)
 

    def inOrder(self, node):
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)
    

    def postOrder(self, node):
        pass




if __name__ == '__main__':
    """
    
    1. inorder traversal
        left-node
        root
        right-node

    2.  Preorder  traversal
        root
        left
        right

    3.  Post traversal2
        Left
        right
        root    

    """
    
    