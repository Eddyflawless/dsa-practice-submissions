class Queue:
    
    def __init__(self):
        self.queue = []

    """ 
        for queues first element 
        appears at the end of the list/array
    """
    def add(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)    

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        return "No elements in queue"    

    def size(self):
        return len(self.queue)


if __name__ == '__main__':

    
    q = Queue()
    q.add(12)
    q.add(202)
    q.add(13)
    q.add(0)
    q.add(12)

    print(q.queue)
    print(q.remove())
    print(q.queue)

    