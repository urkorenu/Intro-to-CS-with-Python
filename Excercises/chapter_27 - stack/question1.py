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

def check_signs(data : str) -> bool:
    s = Stack()
    first_signs = ['(','[','{']
    second_signs = [')',']','}']
    for val in data:
        if val in first_signs:
            s.push(val)
        if val in second_signs:
            if s.is_empty():
                return False
            if val == ')' and s.top() == '(':
                s.pop()
            elif val == '}' and s.top() == '{':
                s.pop()
            elif val == ']' and s.top() == '[':
                s.pop()
    return s.is_empty()

print(check_signs('(4+4)'))