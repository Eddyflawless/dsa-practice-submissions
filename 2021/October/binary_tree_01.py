
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def createNode(self, data):
        return Node(data)

    def insert(self,data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = self.createNode(data)
                else:
                    self.left.insert(data)    
            else:
                if self.right is None:
                    self.right = self.createNode(data)    
                else:
                    self.right.insert(data)   
        else:
            print("else block runned")
            self.data = data  

        return self  

    def findValue(self, lkpvalue):
        if self.data:
            
            if lkpvalue < self.data :
                if self.left is None:
                    return str(lkpvalue) + " not found"
                return self.left.findValue(lkpvalue)    
            elif  lkpvalue > self.data :
                if self.right is None:
                    return str(lkpvalue) + " not found"
                return self.right.findValue(lkpvalue)
            else:
                return str(lkpvalue) + " found"       
                          

    # uses inorder traversal
    # In an inorder traversal, the left child is visited first, 
    # followed by the parent node, then followed by the right child.
    def printTreeInOrder(self):
        # runs till it has exhausted left nodes
        if self.left:
            self.left.printTreeInOrder()

        # only then it prints itself or data 
        print(self.data)

        # Now, since the left subtree and the root has been printed, call inorder on right subtree recursively until we reach a leaf node.
        if self.right:
            self.right.printTreeInOrder()

    # In a preorder traversal, the root node is visited first,
    #  followed by the left child, then the right child.
    def printTreeInOrderPostOrder(self):

        if self.data:
            print(self.data)
           
        if self.left:
            print(self.left.printTreeInOrderPostOrder())
        
        if self.right:
            print(self.right.printTreeInOrderPostOrder())


    

if __name__ == '__main__':

    """ 
        creation of a binary 
        tree starts from the top
    """
    root = Node(27)
    root.insert(14).insert(35).insert(31).insert(10).insert(19).insert(5)

    print("---------print nodes--------")

    #root.printTreeInOrder()
    root.printTreeInOrderPostOrder()

    print("---------find by value--------")
    print(root.findValue(15))