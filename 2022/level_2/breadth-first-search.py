class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        child = Node(name)
        self.children.append(child)
        return child    

    # O(V+E) time | O(V) space
    def breadthFirstSearch(self, visited: list):
        
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0) # remove first node
            visited.append(current.name)
            
            for child in current.children:
                queue.append(child)
            
                
                

"""
Tree structure
          A
        / |  \ 
      B   C    D
     / \       / \
    E     F    G  H
         / \    \
        I   J    K
               
"""

def constructTree():
    # Root-node
    root = Node('A')
    # B-node 
    b_node = root.addChild('B')
    b_node.addChild('E')
    # F-node
    f_node = b_node.addChild('F')
    f_node.addChild('I')
    f_node.addChild('J')
    # C-node
    root.addChild('C')
    # D-node
    d_node = root.addChild('D')
    d_node.addChild('G').addChild('K')
    d_node.addChild('H')
    
    return root

if __name__ == '__main__':
    
    tree_root = constructTree()
    visited = []
    tree_root.breadthFirstSearch(visited)
    print(visited)