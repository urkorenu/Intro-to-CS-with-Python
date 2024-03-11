# //////////////////////////////////////////////////////
# ///////////////////// Maman 15 ///////////////////////
# //////////////////////////////////////////////////////

# Code - 
class WordNode():
    def __init__(self, data, next_node = None, counter = 1):
        """
        Represents a node containing word data in a linked list.

        Args:
        - data (str): The word.
        - next_node (WordNode): Reference to the next WordNode.
        - counter (int): Frequency counter for the word.
        """
        self.String_word    = data
        self.WordNode_next  = next_node
        self.counter        = counter

    def __repr__(self):
        return repr(self.String_word)
    

class TextList():
    def __init__(self, string=None):
        """
        Represents a linked list of words with various word analysis methods.

        Args:
        - string (str): Optional initial string to populate the list.
        """
        self.head = None
        if string:
            self.populate_from_string(string)

# //////////////////////////////////////////////////////
# ///////////////////// Set Methods ////////////////////
# //////////////////////////////////////////////////////

    def populate_from_string(self, string):
        """Function that sort given string and mark the count of appeared strings"""
        items = string.split(' ')
        for val in items:
            node = self.find(val)
            if node:
                node.counter += 1
            else:
                self.addToData(val)

    def pre_append(self, data):
        """Add WordNode object to the start of the linked list"""
        node = WordNode(data)
        node.WordNode_next = l.head
        self.head = node

    def addToData(self, val = None):
        """Append WordNode object to the linked list (TextList)"""
        if val:
            if not self.head:
                self.head = WordNode(val)
                return
            
            node = self.head
            if node.String_word > val:
                    self.pre_append(val)
                    return
            
            new_node = WordNode(val)
            while node.WordNode_next:
                if node.WordNode_next.String_word > val:
                    temp = node.WordNode_next
                    node.WordNode_next = new_node
                    node.WordNode_next.WordNode_next = temp
                    return
                else:
                    node = node.WordNode_next

            node.WordNode_next = new_node

# //////////////////////////////////////////////////////
# ///////////////////// Get Methods ////////////////////
# //////////////////////////////////////////////////////
    
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
        """Find and object from the linked list and return the first object that matches the target"""
        temp = self.head
        while temp:
            if target == temp.String_word:
                return temp
            
            temp = temp.WordNode_next
        return None

    def howManyWords(self):
        """Returns the total count of words in the TextList."""
        total_count = 0
        temp = self.head
        while temp:
            total_count += temp.counter
            temp = temp.WordNode_next
        return total_count

    def howManyDifferentWords(self):
        """Returns the total count of unique words in the TextList."""
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.WordNode_next
        return length
    
    def mostFrequentWord(self):
        """Returns the most frequent word in the TextList."""
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
        """Returns the total count of words that start with specific letter in the TextList."""
        counter = 0
        temp    = self.head
        while temp:
            if temp.String_word[0] == letter:
                counter += temp.counter
            temp = temp.WordNode_next
        return counter
    
    def mostFrequentStartingLetter(self):
        """Returns the most frequent starting letter among words."""
        return self.rec_freq_start_letter(self.head)
        

    def rec_freq_start_letter(self,node,max_int = 0,max_letter = None):
        """Recursive function that operates 'mostFrequentStartingLetter'."""
        if not node:
            return max_letter
        
        temp_letter = node.String_word[0]
        temp_amount = self.howManyStarting(node.String_word[0])
        if temp_amount > max_int:
            max_int = temp_amount
            max_letter = temp_letter
        return self.rec_freq_start_letter(node.WordNode_next,max_int,max_letter)
        
  
l = TextList('anything you can do i can do better do')
l.addToData('zb')
print(l)
print(f'How many words: {l.howManyWords()}')
print(f'How many different words: {l.howManyDifferentWords()}')
print(f'Most frequent word: {l.mostFrequentWord()}')
print(f'How many starting: {l.howManyStarting("c")}')
print(f'Most frequent starting letter: {l.mostFrequentStartingLetter()}')
 
