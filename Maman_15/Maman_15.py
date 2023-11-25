class WordNode():
    def __init__(self, data, next = None, counter = 0) -> None:
        self.String_word = data
        self.WordNode_next = next
        self.counter = counter

    def __repr__(self) -> str:
        return repr(self.String_word)
    

class TextList():
    def __init__(self, string=None) -> None:
        self.head = None
        if string:
            items = string.split(' ')
            items.sort()
            self.head = WordNode(items[0])
            temp = self.head
            for i in range(1,len(items)):
                temp.WordNode_next = WordNode(items[i])
                temp = temp.WordNode_next


# # Pre Fucntions-
#     def pre_append(self, data):
#         node = WordNode(data)
#         node.WordNode_next = l.head
#         l.head = node
    
#     def __repr__(self) -> str:
#         if self.head == None:
#             return '[]'
#         temp = self.head
#         s = '['
#         while temp:
#             s += repr(temp) + ','
#             temp = temp.WordNode_next
#         return s[:-1] + ']'
    
#     def __len__(self) -> int:
#         if self.head == None:
#             return 0
#         length = 0
#         temp = self.head
#         while temp:
#             length += 1
#             temp = temp.WordNode_next
#         return length
    
#     def sum(self) -> int:
#         if self.head == None:
#             return 0
#         sum = 0
#         temp = self.head
#         while temp:
#             sum += temp.String_word
#             temp = temp.WordNode_next
#         return sum

#     def find(self, target: int):
#         temp = self.head
#         while temp:
#             if target == temp.String_word:
#                 return temp
#             temp = temp.WordNode_next
#         return None
    
#     def __getitem__(self, index : int):
#         assert 0 <= index < len(self)
#         temp = self.head
#         for x in range(index):
#             temp = temp.WordNode_next
#         return temp
    
#     def __setitem__(self, index : int, new_data):
#         # assert 0 <= index < len(self)
#         self[index].String_word = new_data

#     def addToData(self, index : int, val):
#         # assert 0 <= index < len(self)
#         if index == 0:
#             self.pre_append(val)
#             return
#         node = self.head
#         for i in range(0, index - 1):
#             node = node.WordNode_next
#         temp = node.WordNode_next
#         node.WordNode_next = WordNode(val)
#         node.WordNode_next.WordNode_next = temp

#     def delete(self, index):
#         if index == 0:
#             self.head = self.head.WordNode_next
#             return
#         node = self.head
#         for i in range(index - 1):
#             node = node.WordNode_next
#         node.WordNode_next = node.WordNode_next.next

 

l = TextList('anything you can do i can do better')
l2 = TextList()
# l.head = a
# l.head.next = b
# l.head.next.next = c
# l.pre_append(15)
print(l)
print(l2)
print(len(l))
print(l.head)
# print(l.sum()) 
# print(l.find(2))
# print(l[0])
# l[1] = 14
# l.insert(4, 4)
# l.delete(0)
# print(l)