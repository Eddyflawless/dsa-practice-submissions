"""
    queue operations
    1. size
    2. enqueue
    3. dequeue
    4. isEmpty
    5. IsFull
    6. Peek
"""

class Queue():

    def __init__(self,limit=float("inf")):
       self.queue = []
       self.limit = limit

    def peek(self):

        if len(self.queue) > 0:
            return self.queue[-1]
        
        return None

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return None
        # self.queue.insert(0,item)
        self.queue.append(item)
          
    def dequeue(self):
        if self.isEmpty() == True:
            return None
        self.queue.pop(0)

    def isEmpty(self):
        if self.size() > 0:
            return False
        return True  

    def isFull(self):
        if self.size() < self.limit:
            return False
        return True  

    def size(self):
        return len(self.queue)

    def printQueue(self):    
        for item in self.queue:
            print(item,end=" ")
        print() #empty line    


if __name__ == "__main__":

    q1 = Queue()
    for index,item in enumerate([32,11,90,100,-24,15,0]):
        q1.enqueue(item)

    q1.printQueue() 
    q1.dequeue() # remove first element    
    q1.printQueue() 
    q1.enqueue(67)
    q1.printQueue() 
    q1.dequeue() # remove first element    
    q1.dequeue() # remove first element    
    q1.printQueue() 
