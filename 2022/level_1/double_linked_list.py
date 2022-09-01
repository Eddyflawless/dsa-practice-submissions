
class Node:
    
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
        
class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self, data):
       
        newNode = Node(data)
       
        if self.head is None:
           self.head = newNode
        else:
            
            node = self.head
            
            while node.next:
                
                node = node.next
            
            node.next = newNode 
            newNode.prev = node
            #newNode.next = None
              
        return self    
    
    def remove(self, node):
        
        if node is None: 
            return
            
        if node.prev is not None:
            node.prev.next = node.next
            
        if node.next is not None:
            node.next.prev = node.prev    
            
            
    def removeAt(self, index):
        
        if index < 0:
            raise ValueError("index must be positive")
        depth = 0
        node = self.head
        
        #best case scenario
        if index == 0:
            if node:
               self.head = node.next     
            return
        
        prevNode = node
        while node:
            if depth == index:
                prevNode.next = node.next 
                node.prev = prevNode.next
                break
                
            depth += 1
            prevNode = node
            node = node.next
    
    def getLastNode(self):
        node = self.head
        
        while node.next:            
            node = node.next
        
        return node
    
    def reversePrint(self):
        
        output = ["None-->"]
        #get last node
        node = self.getLastNode()
        
        if node:
            while node:
                output.append(f"[{node.data}]-->")
                node = node.prev
        
        output.append("Head")        
        print(''.join(output))    

    def printList(self):
        
        output = ["head-->"]
        node = self.head
        
        while node:
            
            output.append(f"[ {node.data} ]-->")
            node = node.next
            
        output.append("None")
                
        print(''.join(output))    


def constructLinkedList(elements):
    l = DoubleLinkedList()
    
    for element in elements:
        l.append(element)
    
    return l


if __name__ == "__main__":
    elements = [16,7,0,21,13,5 ]
    linkedList = constructLinkedList(elements)
    linkedList.printList()
    
    # print("in reversePrint")
    # linkedList.reversePrint()
    linkedList.removeAt(2)
    linkedList.printList()
    

    