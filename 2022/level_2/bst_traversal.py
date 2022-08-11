from typing import List

class BST:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def preOrder(self, root):
        
        if root is None:
            return
        
        print(root.value)
        self.preOrder(root.left)
        self.preOrder(root.right)
        
        
    # O(n) time | O(depth) space    
    def inOrder(self, root):
        
        if root is None:
            return
        
        self.inOrder(root.left)
        print(root.value)
        self.inOrder(root.right)
        
            
        
    def postOrder(self, root):
        
        if root is None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.value)
        
    # O(log n) time | O(n) space |    
    def add(self, value):
        
        root = self
        node = BST(value)

        while root:
                
            if value < root.value:
                if root.left is not None:
                    root = root.left
                else:
                    root.left = node
                    break
            elif value > root.value:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = node
                    break    
            else:
                #check if node exist in tree
                if value == root.value:
                    continue
        
        return root                    
    
def constructTree(rtValue: int, nodes: List[int]) -> BST:
    
    root = BST(rtValue)
    
    for node in nodes:
        if node > 0:
            root.add(node)
            
        
    return root

      
if __name__ == '__main__':
    els = [5,15,22,2,1] 
    
    rootNode = constructTree(10, els)  
    
    #inorder traversal of tree
    print("---inoder--------------------------------")
    rootNode.inOrder(rootNode) # expect 1,2,5,10,15,22
    print("---inoder--------------------------------")
         
    #preorder traversal of tree
    print("---preoder--------------------------------")
    rootNode.preOrder(rootNode) # expect 10,5,2,1,5,15,22
    print("---preorder--------------------------------")
    
     
    #postorder traversal of tree
    print("---postorder--------------------------------")
    rootNode.postOrder(rootNode) # expect 1,2,5,5,22,15,10
    print("---postorder--------------------------------")