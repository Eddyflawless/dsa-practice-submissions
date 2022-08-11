from doctest import OutputChecker
from pprint import pprint
# O (V + E) time | O (V) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, node):
        self.children.append(node) 
        return self    
    
    
    def dfs(self, array):
        
        array.append(self.name) #calls on itself
        
        for child in self.children:
            child.dfs(array)
            
        return array       


def createTree():
    root = Node('A')
    
    b_node = Node('B')
    b_node.addChild(Node('E'))
    b_node.addChild(Node('F').addChild(Node('I').addChild(Node('J'))))
    root.addChild(b_node)
    
    root.addChild(Node('C'))
    root.addChild(Node('D').addChild(Node('G').addChild(Node('K'))).addChild(Node('H')))
    
    return root


if __name__ == '__main__':
    # tree = ['A','B','E','F','I','C','D','G','K' ,'H']
    basic_tree = createTree()
    output = []
    basic_tree.dfs(output)
    
    print(output)