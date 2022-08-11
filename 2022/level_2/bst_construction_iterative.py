class BST:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # Average: O(log(n)) time | O(1) time 
    # Worst: O(n) time | O(1) time
    
    def insert(self, value: int):
        node = BST(value)
        currentNode = self 
        
        while True:
            
            if value < currentNode.value:
                
                #check if we are the end of a branch
                if currentNode.left is None:
                    currentNode.left = node
                    break
                else:
                    currentNode = currentNode.left
            else:
                
                if currentNode.right is None:
                    currentNode.right = node
                    break       
                else:
                    currentNode = currentNode.right        
                    
        return self     
            
    # Average: O(log(n)) time | O(1) time 
    # Worst: O(n) time | O(1) time
    def search(self, value: int):
        currentNode = self
        
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

        return False
    
    def delete(self, value: int, parentNode: None):
        currentNode = self
        
        while currentNode:
            if value < currentNode.value:
                
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                
                if currentNode.left and currentNode.right:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.delete(currentNode.value, parentNode)
                else: 
                    #check if the matching node has children
                    pass
                            
    def getMinValue(self):
        pass
    
    

def constructTree() -> BST: 
    ...


if __name__ == '__main__':
    binaryTree: BST = constructTree()