class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True

        return False    

    def pop(self):
        return self.stack.pop()
         

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return "Stack is empty"    


if __name__ == '__main__':

    stack = Stack()
    stack.push(12)
    stack.push(10)
    stack.push(5)
    stack.push(12)
    stack.pop()

    print(stack.stack)
    print(stack.peek())
    