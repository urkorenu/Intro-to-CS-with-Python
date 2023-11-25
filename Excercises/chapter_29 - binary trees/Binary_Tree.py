class Tnode():
    def __init__(self, key : int, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.key) + ': ' + str(self.data)
    
class BinarySearchTree():
    def __init__(self, tree = None) -> None:
        self.root = None
        if tree != None:
            for key,data in tree:
                self.insert(key, data)

# //////////// Set Methods /////////////
    def insert(self, key : int, data) -> None:
        if self.root == None:
            self.root = Tnode(key,data)
        self._insert_node(self.root, key, data)


    def _insert_node(self, node : Tnode, key : int, data) -> None:
        if key == node.key:
            node.data = data
        elif node.key > key:
            if node.left == None:
                node.left = Tnode(key,data)
                return
            self._insert_node(node.left, key, data)
        else:
            if node.right == None:
                node.right = Tnode(key,data)
                return
            self._insert_node(node.right, key, data)
        return
    
# ///////// Get Methods /////////

    def lookup(self,key : int):
        return self._lookup_node(self.root,key)
    
    def _lookup_node(self, node : Tnode ,key):
        if node == None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._lookup_node(node.left, key)
        return self._lookup_node(node.right, key)
   
    def minimum(self) -> int:
        return self._minimum_node(self.root, self.root.key)

    def _minimum_node(self, node : Tnode, key : int) -> int:
        if node == None:
            return key
        a = self._minimum_node(node.left,node.key) 
        b = self._minimum_node(node.right,node.key)
        if a>b:
            return b
        return a
    
    def depth(self) -> int:
        return self._depth_rec(self.root, -1)
    
    def _depth_rec(self, node : Tnode, length : int) -> int:
        if node == None:
            return length
        length += 1
        a = self._depth_rec(node.left, node.key)
        b = self._depth_rec(node.right, node.key)
        if a>b:
            return b
        return a

    def maximum(self) -> int:
        return self._maximum_node(self.root, self.root.key)
    
    def _maximum_node(self, node : Tnode, key : int) -> int:
        if node == None:
            return key
        a = self._maximum_node(node.left,node.key) 
        b = self._maximum_node(node.right,node.key)
        if b>a:
            return b
        return a
    
    def __len__(self) -> int:
        return self._len_rec(self.root)
        

    def _len_rec(self, node : Tnode) -> int:
        if node == None:
            return 0
        return 1 + self._len_rec(node.left) + self._len_rec(node.right)

    def inorder(self):
        self._inorder_rec(self.root)
        print()

    def _inorder_rec(self, node: Tnode):
        if node == None:
            return
        self._inorder_rec(node.left)
        print(node.key, end=' ')
        self._inorder_rec(node.right)

    def postorder(self):
        self._postorder_rec(self.root)
        print()

    def _postorder_rec(self, node: Tnode):
        if node == None:
            return
        self._postorder_rec(node.right)
        print(node.key, end=' ')
        self._postorder_rec(node.left)

    def print_by_level(self):
        depth = self.depth()
        for level in range(depth+1):
            print(f'level {level} :', end = ' ')
            self._print_level(self.root, level)
            print()

    def _print_level(self, node : Tnode , level : int):
        if node == None:
            return
        if level == 0:
            print(node.key, end = ' ')
        else:
            self._print_level(node.left, level -1)
            self._print_level(node.right, level -1)

bs = BinarySearchTree()
bs.insert(3,'a')
bs.insert(5,'b')
bs.insert(6,'b')
bs.insert(2,'c')
bs.insert(4,'d')
bs.print_by_level()
# print(bs.lookup(4))
print(f'min : {bs.minimum()}')
print(f'depth: {bs.depth()}')
print(f'max: {bs.maximum()}')
bd = BinarySearchTree([(2,'a'), (1,'b')])
print(f'len : {len(bd)}')
bs.inorder()
bs.postorder()

    