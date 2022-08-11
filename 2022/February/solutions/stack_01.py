
"""
    stack operations
    1. peek
    2. push
    3. length
    4. pop
"""

class Stack():

    def __init__(self):
       self.stack = []

    def peek(self):

        if len(self.stack) > 0:
            return self.stack[-1]
        
        return None

    def pop(self):
        # returns last element inserted
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1    
       
    def push(self,item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


if __name__ == "__main__":

    s1 = Stack()
    for index,item in enumerate([32,11,90,100,-24,15,0]):
        s1.push(item)

    print(s1.pop())
    print("remaining", s1.__dict__)    

    print("peek",s1.peek())
