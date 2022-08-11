class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.prev = prev
        self.next = next
        self.data = data


class DoubleLinkedList:
    
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):

        if self.head is None:
            self.head = Node(data,None,None)
        else:
            self.head = Node(data,self.head,None)    

    def insertAtEnd(self,data,prev=None):

            if self.head is None:
                self.insertAtBeginning(data)
                return

            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data,prev,None)  

            return node.next
    

    def printNodesForward(self):

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

    def printNodesBackward(self):

        last_node = None

        output = ""
        if self.head is None:
            output += "none"
            print("Linked list empty")
            print(output)
            return

        current_node = self.head
        while current_node:

            if current_node.next is None:
                break
            current_node = current_node.next

        last_node = current_node

        print("done", last_node.data)
        # return
        while last_node:
            print("hshs")
            output += str(last_node.data) + "-->"
            last_node  = last_node.prev

        output += "-->head"
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
                    node.next.prev = node
                    break

                index += 1 
                node = node.next   



if __name__ == '__main__':
    linked_list = DoubleLinkedList()

    n1 = linked_list.insertAtEnd(104)
    n2 = linked_list.insertAtEnd(25,n1)
    n3 = linked_list.insertAtEnd(7,n2)
    n4 = linked_list.insertAtEnd(3,n3)
    n5 = linked_list.insertAtEnd(14,n4)


    linked_list.printNodesForward()

    print("delete node")
    linked_list.removeNodeAt(2)

    linked_list.searchNode(3)

    linked_list.printNodesForward()
    linked_list.printNodesBackward()


    