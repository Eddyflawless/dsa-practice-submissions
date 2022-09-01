## A node has data and next attributes

class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None


    def reverse(self):
        
        node =  self.getLastNode()
        
        if node is None:
            return 
        
        while node.prev:
            pass
            
            
    
    def getLastNode(self):
        node = self.head
    
        while node.next:            
            node = node.next
        
        return node
    
    def search(self, data):
        
        depth = 1
        node = self.head
        
        while node:
            
            if node.data == data:
                break
            depth += 1
            node = node.next
            
        return depth
            
    
            
    def removeAt(self, index):
        depth = 1
        node = self.head
        
        prevNode = None
        while node:
            if depth == index:
                prevNode.next = node.next
            else:
                prevNode = node
                
            depth += 1
            node = node.next
         
    
    def getAt(self, index):
        depth = 1
        node = self.head
        
        while node:
            if index == depth:
                return node
            depth += 1
            node = node.next
             
        return node
    
    def append(self, data):
        
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            node = self.head 
            
            while node.next: #check if next_node is not None
                
                # since its defined, it has a next propert as all nodes should have
                # property -> data, next 
                node = node.next; 

            node.next = newNode    
            
        return self
    
    def prepend(self, data):
        
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    
    def insertAt(self, data, index):
        
        depth = 1
        
        node = self.head
        prevNode = None
        
        while node:
            
            if depth == index:
                prevNode.next = Node(data)
                prevNode.next.next = node
                break
                
            prevNode = node
            node = node.next
            depth += 1
            
        
    
    def getLength(self):
        length = 0
        
        next = self.head
        
        while next:
            length += 1
            next = next.next
             
        return length 
    
    def printList(self):
        
        node = self.head
        
        outputStr = 'head-->'
        
        while node:
            outputStr += f"[ {node.data} ]-->"
            node = node.next
            
        outputStr += " None"
        print(outputStr)
            
        
def constructLinkedList(elements):
    l = LinkedList()
    
    for element in elements:
        l.append(element)
    
    return l
    
    

if __name__ == '__main__':
    
    elements = [16,7,0,21,13,5 ]
    
    linkedList = constructLinkedList(elements)
    
    linkedList.prepend(201)
    
    linkedList.printList()
    
    lenthOfLinkedList = linkedList.getLength()
    
    print("length of linked list: " ,lenthOfLinkedList)
    
    elementAtIndex = linkedList.getAt(3)
    
    print("elementAtIndex: " ,elementAtIndex.data)
    
    linkedList.removeAt(3)
    
    linkedList.printList()
    
    linkedList.insertAt(89,3)
    
    linkedList.printList()
    
    print("Element is found at index: ", linkedList.search(13))