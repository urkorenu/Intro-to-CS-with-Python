class LNode():
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return repr(self.data)
    

class LinkedList():
    def __init__(self, items) -> None:
        self.head = LNode(items[0])
        temp = self.head
        for i in range(1,len(items)):
            temp.next = LNode(items[i])
            temp = temp.next

    def pre_append(self, data):
        node = LNode(data)
        node.next = l.head
        l.head = node
    
    def __repr__(self) -> str:
        if self.head == None:
            return '[]'
        temp = self.head
        s = '['
        while temp:
            s += repr(temp) + ','
            temp = temp.next
        return s[:-1] + ']'
    
    def __len__(self) -> int:
        if self.head == None:
            return 0
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length
    
    def sum(self) -> int:
        if self.head == None:
            return 0
        sum = 0
        temp = self.head
        while temp:
            sum += temp.data
            temp = temp.next
        return sum

    def find(self, target: int):
        temp = self.head
        while temp:
            if target == temp.data:
                return temp
            temp = temp.next
        return None
    
    def __getitem__(self, index : int):
        assert 0 <= index < len(self)
        temp = self.head
        for x in range(index):
            temp = temp.next
        return temp
    
    def __setitem__(self, index : int, new_data):
        # assert 0 <= index < len(self)
        self[index].data = new_data

    def insert(self, index : int, val):
        # assert 0 <= index < len(self)
        if index == 0:
            self.pre_append(val)
            return
        node = self.head
        for i in range(0, index - 1):
            node = node.next
        temp = node.next
        node.next = LNode(val)
        node.next.next = temp

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.head
        for i in range(index - 1):
            node = node.next
        node.next = node.next.next

 
# a = LNode(1)
# b = LNode(2)
# c = LNode(3)
l = LinkedList()
# l.head = a
# l.head.next = b
# l.head.next.next = c
l.pre_append(15)
print(l)
print(len(l))
print(l.sum()) 
print(l.find(2))
print(l[0])
l[1] = 14
l.insert(4, 4)
l.delete(0)
print(l)