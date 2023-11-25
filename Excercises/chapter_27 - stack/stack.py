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

s = Stack()
s.push('a')
s.push(2)
s.pop()
print(s.top())
s.pop()
print(s.is_empty())
print(s)