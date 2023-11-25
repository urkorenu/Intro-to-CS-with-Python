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

def count(stack : Stack, x) -> int:
    count = 0
    for val in range(0, stack.size):
        if stack.stack[val] == x:
            count += 1
    return count


s = Stack()
s.push(5)
s.push(5)
s.push(2)
s.push(3)
s.push(4)
s.push(78)
s.push(91)
print(s)
print(count(s, 5))