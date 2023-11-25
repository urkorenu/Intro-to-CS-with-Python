class Stack():
    def __init__(self) -> None:
        self.stack = []
        self.size = 0
        
# ////////// Set Methods //////////////

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        else:
            return self.stack[self.size - 1]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        poped = self.stack[self.size - 1]
        self.stack = self.stack[0:self.size - 1]
        self.size -= 1
        return poped
        

    def push(self, val):
        self.stack.append(val)
        self.size += 1

# ////////// Get Methods //////////////

    def __repr__(self) -> str:
        return f'stack = {self.stack}'
    
    def is_empty(self) -> bool:
        return self.size == 0

def validation(stack : Stack) -> bool:
    for val in range(1, stack.size):
        temp = stack.stack[val -1 ]
        if temp > stack.stack[val]:
            return False
    return True


s = Stack()
# s.push(5)
# s.push(5)
s.push(2)
s.push(3)
s.push(4)
s.push(78)
s.push(91)
print(s)
print(validation(s))