






class BTreeNode:


    def __init__(self,t,leaf=True):
        self.t = t #minimum degree property of tree
        self.keys = [None] * (2 * t -1) #at most 2t -1 keys
        self.children = [None] * (2 * t) # must have at least t children,
        self.num_keys = 0
        self.leaf = leaf
    
    def search(self,key):

        i = 0
        while i < self.num_keys and key > self.keys[i]:
            i += 1

        if i < self.num_keys and self.keys[i]] == key:
            return self
        
        
        if self.leaf:
            return None  


        return self.search(self.children[i],key)
    
    def traverse(self):
        
        i = 0
        
        while i < self.num_keys:
            if not self.leaf:
                self.traverse(self.children[i])
            
            print(self.a[i],end=' ')
            i += 1

                
        if not self.leaf: 
            self.children[i].traverse()
    
    def splitChild(self,i,node):

        new_node = BTreeNode(self.t)
        
        # move last t - 1 keys
        for i in range(0,self.t - 1):
            new_node.keys[i] = node.keys[i + self.t]

        #move last t children

        for i in range(0,self.t):
            new_node.children[i] = node.chidren[i + self.t]


        node.num_keys = t - 1 #adjust new_node to have correct number of keys


        #shift keys from i to end
        for j in range(self.num_keys - 1,i -1,-1):
            self.keys[j + 1] = self.keys[j]


        #shift children from i + 1 to end
        for i in range(self.num_keys + 1,i,-1):
            self.children[j + 1] = self.children[j]


        self.children[i + 1] = new_node
        self.keys[i] = new_node.keys[self.t - 1] # get median key and add it to parent
        
        self.num_keys += 1


    
    def insertNonFull(self,key):
        
        i = 0
        
        if self.leaf:

            i = self.num_keys - 1

            while i >= 0 and key < self.keys[i]: 
                i -= 1

            self.keys[i + 1] = key
            self.num_keys += 1
        else:

            i = self.num_keys - 1

            while i >= 0 and key < self.keys[i]:
                i -= 1

            if self.children[i + 1].num_keys == 2 * self.t - 1: #if child to traverse next is full, split child
                self.splitChild(i + 1,self.children[i + 1])
            

            if key < self.keys[i + 1]:
                i += 1


            self.children[i + 1].insertNonFull(key)


            



            

        







class BTree:


    def __init__(self,t):
        self.t = t #minimum_degree
        self.size = 0 #num keys
        self.root = None

    def __len__(self):
        return self.size
    
    
    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self,key):
        if self.root:
            value =  self.root.search(key)
            if value:
                return value
        
        raise KeyError(f"Key {key} does not exist in tree")

    
    def add(self,key):

        if not self.root:
            self.root = BTreeNode(self.t)
            self.root.key[0] = key
            self.root.num_keys = 1
        else:
        
            if self.root.num_keys == 2 * self.t - 1: # if root is full
                new_node = BTreeNode(self.t)

                new_node.children[0] = self.root

                new_node.splitChild(0,self.root) #split 0th child which is self.root

                if new_node.keys[0] < key:
                    i += 1
                new_node.children[i].insertNonFull(key)
            else:
                self.root.insertNonFull(key)








            




















