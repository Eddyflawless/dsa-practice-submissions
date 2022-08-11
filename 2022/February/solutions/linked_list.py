# node points to another node [noode]->[node] and has data


class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):    
        if self.head is None:
            self.insertAtBeginning(data)
            return

        node = self.head    
        while node.next:
            node = node.next

        node.next = Node(data)    

    def insertAtBeginning(self, data):

        if self.head is None:
            self.head = Node(data,self.head)
        else:
            self.head = Node(data,None)    

    def printNodes(self):
        pass

    def getLength(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count    

    def reverse(self):
        pass    




if __name__ == '__main__':
    linked_list = LinkedList()
