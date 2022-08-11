class Node:
    def __init__(self,data=None,next=None):
        self.next = next
        self.data = data

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):

        if self.head is None:
            self.head = Node(data,None)
        else:
            self.head = Node(data,self.head)    

    def insertAtEnd(self, data):

            if self.head is None:
                self.insertAtBeginning(data)
                return

            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data,None)  
    

    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)


    def printNodes(self):

        output = "head--->"
        if self.head is None:
            output += "none"
            print("Linked list empty")
            print(output)
            return
        
        node  = self.head
      
        while node:
            output += str(node.data) + "--->"
            node = node.next

        output += "none"
        print(output)

    def getLength(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count

    def insertNodeAt(self,data,pos=0):

        if pos < 0 or pos > self.get_length() :
            raise Exception("Invalid index") 

        if pos ==  0:
            self.insertAtBeginning(data)
            return

        if pos == self.getLength():
            self.insertAtEnd(data)  
            return  

        index = 0

        if self.head:
            node = self.head
            while node:
                if index == pos:
                    node.next = Node(data,node.next)
                    break
                index += 1
                node = node.next


    def searchNode(self, data):

        node = self.head
        index = 0
        while node:
            if node.data == data:
                print("Found")
                break
            node = node.next
            index += 1 

        print("Not found")       


    def reverseList(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next # store next node temporaily
            current.next = prev # point current node to previus node
            prev = current # current becomes previous node
            current = next

        self.head = prev



    def removeNodeAt(self,pos):
        if pos < 0 or pos > self.getLength() :
            raise Exception("Invalid index") 

        if pos == 0:
            self.head = self.head.next
            return

        index = 0
        if self.head:
            node = self.head
            while node:

                if index == pos - 1:
                    node.next = node.next.next
                    break

                index += 1 
                node = node.next   



if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insertAtEnd(34)
    linked_list.insertAtEnd(104)
    linked_list.insertAtEnd(25)
    linked_list.insertAtEnd(7)

    linked_list.insertAtBeginning(14)
    linked_list.insertAtBeginning(3)
    linked_list.printNodes()
    print(linked_list.getLength())

    linked_list.removeNodeAt(2)

    linked_list.printNodes()

    linked_list.searchNode(333)

    linked_list.reverseList()
    print("reversed list")
    linked_list.printNodes()

    