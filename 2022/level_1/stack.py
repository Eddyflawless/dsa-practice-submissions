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
       
    def push (self,el):
        self.stack.append(el)

    def length (self):
        return len(self.stack)
    
    def peek(self):
        if self.length() == 0:
            return None
        return self.stack[self.length() - 1]    
        
    def pop(self):
        
        if self.peek() is None:
            raise ValueError("stack is empty")
        
        self.stack.pop()  
          


def constructStack(els):
    stack = Stack()
    for item in els:
        stack.push(item)
        
    return stack    

if __name__ == '__main__':
    els = [32,11,90,100,-24,15,0]
    stack = constructStack(els)
    
    print(stack.stack)
    #operations