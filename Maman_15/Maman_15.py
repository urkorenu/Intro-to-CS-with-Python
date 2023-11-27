class WordNode():
    def __init__(self, data, next = None, counter = 1) -> None:
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
            for val in items:
                node = self.find(val)
                if node:
                    node.counter += 1
                else:
                    self.addToData(val)

    def pre_append(self, data):
        node = WordNode(data)
        node.WordNode_next = l.head
        self.head = node
    
    def __repr__(self) -> str:
        if self.head == None:
            return '[]'
        temp = self.head
        s = '['
        while temp:
            s += repr(temp) + f':{temp.counter}' +'\n'
            temp = temp.WordNode_next
        return s[:-1] + ']'

    def find(self, target: int):
        temp = self.head
        while temp:
            if target == temp.String_word:
                return temp
            temp = temp.WordNode_next
        return None
    
#     def __getitem__(self, index : int):
#         assert 0 <= index < len(self)
#         temp = self.head
#         for x in range(index):
#             temp = temp.WordNode_next
#         return temp
    
#     def __setitem__(self, index : int, new_data):
#         # assert 0 <= index < len(self)
#         self[index].String_word = new_data

    def addToData(self, val = None):
        if val:
            node = self.head
            if node == None:
                self.head = WordNode(val)
                return
            elif node.String_word > val:
                    self.pre_append(val)
            while node.WordNode_next:
                if node.WordNode_next.String_word > val:
                    temp = node.WordNode_next
                    node.WordNode_next = WordNode(val)
                    node.WordNode_next.WordNode_next = temp
                    return
                else:
                    node = node.WordNode_next
            node.WordNode_next = WordNode(val)  

    def howManyWords(self):
        if self.head == None:
            return 0
        length = 0
        temp = self.head
        while temp:
            length += temp.counter
            temp = temp.WordNode_next
        return length

    def howManyDifferentWords(self):
        if self.head == None:
            return 0
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.WordNode_next
        return length
    
    def mostFrequentWord(self):
        len_frequent = 0
        temp = self.head
        most_frequent = None
        while temp:
            if temp.counter > len_frequent:
                len_frequent = temp.counter
                most_frequent = temp
            temp = temp.WordNode_next
        return most_frequent
    
    def howManyStarting(self,letter):
        counter = 0
        temp = self.head
        while temp:
            if temp.String_word[0] == letter:
                counter += temp.counter
            
                print(letter)
            temp = temp.WordNode_next
        return counter
    
    def mostFrequentStartingLetter(self):
        node = self.head
        letter = node.String_word[0] 
        return self.rec_freq_start_letter(node)
        

    # def rec_freq_start_letter(self,node,max):
    #     if node == None:
    #         return
    #     if self.howManyStarting(node.String_word[0]) > max

l = TextList('anything you can do i can do better')
l2 = TextList()
print(l2)
# print(f'len :{len(l)}')
l.addToData('zb')
print(l)
print(f'How many words: {l.howManyWords()}')
print(f'How many different words {l.howManyDifferentWords()}')
print(f'Most frequent word: {l.mostFrequentWord()}')
print(f'How many starting {l.howManyStarting("c")}')
 
