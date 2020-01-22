

class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Node({self.key},{self.value})"

class BTreeNode:

    def __init__(self,t,leaf=True):
        self.t = t
        self.leaf = leaf
        self.keys = [None] * (2 * t - 1)
        self.children = [None] * (2 * t)
        self.num_keys = 0
    
    def search(self,key):

        i = 0
        
        while i < len(self.num_keys) and key > self.keys[i]:
            i += 1

        if i < len(self.num_keys) and key == self.keys[i]:
            return self

        return self.children[i].search(key)

    def traverse(self):


        for i in range(self.num_keys):
            
            if not self.leaf:
                self.children[i].traverse()

            print(self.keys[i])
        

        if not self.leaf:
            self.children[self.num_keys].traverse()
    
    def insertNonFull(self,key):

        if not self.leaf: # if its not a leaf
            i = self.num_keys - 1

            while i >= 0 and key < self.keys[i]:
                i -= 1

            
            if self.children[i + 1].num_keys == 2 * self.t - 1:
                self.splitChild(i + 1,self.children[i + 1])

            if key > self.keys[i + 1]:
                i += 1

            self.children[i + 1].insertNonFull(key)
        else:
            i = self.num_keys - 1

            while i >= 0 and key < self.keys[i]:
                self.keys[i +1] = self.keys[i]

            self.keys[i +1] = key
            self.num_keys += 1


    
    def splitChild(self,index,node):
        new_node = Node(self.t,node.leaf)
    
        # move last t - 1 keys to this node
        for i in range(self.t - 1):
            new_node.keys[i] = node.keys[i + self.t]

        new_node.num_keys = self.t - 1
        #move last t children to this node
        if not node.leaf:
            for i in range(self.t):
                new_node.keys[i] = node.keys[i + self.t]
        

        for i in range(self.num_keys,i - 1,-1):
            self.keys[i + 1] = self.keys[i]

        for i in range(self.num_keys + 1,i,-1):
            self.children[i +1] = self.children[i]

        self.keys[i] = node.keys[self.t - 1]
        self.num_keys += 1
        self.children[i +1] = new_node









class BTree:


    def __init__(self,t):
        self.root = None
        self.t = t
        self.size = 0

    def __len__(self):
        return self.size
    

    def search(self,key):

        if self.root:
            self.root.search(key)

    
    def traverse(self):

        if self.root:
            self.root.traverse()

    
    def add(self,key):
        if not self.root: #if empty just create b tree and set key to first element
            self.root = BTreeNode(self,t)
            self.root.keys[0] = key
        else:
            if self.root.num_keys == 2 * t - 1: # if root is full
                new_node = Node(self.t,leaf=False) #create new node
                new_node.children[0] = self.root #this new node will be new root so set 0th child to be previous root
                new_node.splitChild(0,self.root) #split 0th child which is self.root
                

                self.root = new_node

                i = 0
                if key > new_node.keys[0]:
                    i += 1

                self.children[i].insertNonFull(key)
            else:
                self.root.insertNonFull(key)


