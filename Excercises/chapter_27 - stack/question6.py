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

def rec_sum(stack : Stack) -> int:
    if not stack.is_empty():
        temp_stack.push(stack.pop())
        return temp_stack.top() + rec_sum(stack)
    else:
        while not temp_stack.is_empty():
            stack.push(temp_stack.pop())
        return 0

s = Stack()
temp_stack = Stack()
# s.push(5)
# s.push(5)
s.push(2)
s.push(3)
s.push(4)
s.push(78)
s.push(91)
print(s)
print(rec_sum(s))
print(s)