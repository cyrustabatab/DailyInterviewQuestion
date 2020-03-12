

class Node:

    def __init__(self,tree=None):
        self.tree = tree
        self.next = None
    
    @property
    def order(self):
        if self.tree:
            return self.tree.order


    @property
    def key(self):
        if self.tree:
            return self.tree.key


class LL:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.minimum = None
    
    def _add_front(self,node):

        node.next = self.head.next
        if not node.next:
            self.tail = node
        
        self.head.next = self.tail
    
    def _set_minimum(self):

        minimum = float("inf")
        min_node = None
        current = self.head.next

        while current:
            if current.key < minimum:
                minimum = current
                min_node = current

        
        self.minimum = min_node

    def union(self):
        current,previous = self.head.next,None
        
        minimum = float("inf")
        min_node = None
        while current and current.next:
            if current.key < minimum:
                minimum = current.key
                min_node= current
            if current.order != current.next.order:
                previous= current
                current = current.next
            else:
                if current.next.next and current.order == current.next.next.order:
                    previous = current
                    current = current.next
                elif current.key <= current.next.key:
                    current.tree.add_child(current.next.tree)
                    #current.next.tree = None
                    current.next = current.next.next
                else:
                    current.next.tree.add_child(current.tree)
                    previous.next = current.next
                    current = current.next


        

        self.minimum = current if current and current.key < minimum else min_node

    def merge(self,ll):

        current_1,current_2 = self.head.next,ll.head.next
        new_ll = LL()
        while current_1 or current_2:
            if not current_2 or (current_1 and current_1.order <= current_2.order):
                temp = current_1.next
                new_ll._add_front(current_1)
                current_1 = temp
            else:
                temp = current_2.next
                new_ll._add_front(current_2)
                current_2 = temp


        self.head,self.tail = new_ll.head,new_ll.tail

        self.union()
    
    def _add_end(self,node):

        self.tail.next =node
        self.tail = node

    def remove_min(self):

        if self.minimum:

            current = self.minimum.tree.left_most_child
            new_ll = LL()
            while current:
                temp = current.next
                current.parent = None
                new_ll._add_end(current)
                current = temp


            current = self.head
            while current.next is not self.minimum:
                current = current.next

            current.next = current.next.next
            
            if current is self.head:
                self.head,self.tail = new_ll.head,new_ll.tail
                return
            self.merge(new_ll)

    def add(self,tree):

        node = Node(tree)
        self._add_front(node)
        self.merge()

class BinomialTree:

    def __init__(self,_id,key,predecessor):
        self.id = _id
        self.key = key
        self.predecessor = predecessor
        self.left_most_child = self.right_sibling = None
        self.parent = None
        self.order = 0
    
    def add_child(self,tree):
        tree.right_sibling = self.left_most_child
        self.left_most_child = tree
        tree.parent = self
        self.order += 1

    def __repr__(self):
        return f"BinomialTree({self.id},{self.key})"


class BinomialHeap:

    def __init__(self):
        self.ll = LL()
        self.map = {}
        self.size = 0
    
    @property
    def empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
    

    def merge(self,heap):
        if isinstance(heap,BinomialHeap):
            if heap.empty:
                return

            if self.empty:
                self.ll = heap.ll
                #heap.ll = None
                self.size = heap.size
                return
            

            self.ll.merge(heap.ll)
            self.size += heap.size

    def add(self,_id,key,predecessor):
        tree = BinomialTree(_id,key,predecessor)
        self.map[_id] = tree

        self.ll.add(tree)
        self.size += 1

    def remove_min(self):
        if not self.empty:
            value = self.ll.minimum
            self.ll._remove_min()
            self.size -= 1

            return value

    
    def decrease_key(self,_id,key,predecessor=None):
        if _id in self.map:
            tree = self.map[_id]

            if key >= tree.key:
                return

            tree.key = key
            tree.predecessor= predecessor 

            current = tree

            while current.parent and current.key < current.parent.key:
                current.id,current.parent.id = current.parent.id,current.id
                current.key,current.parent.key = current.parent.key,current.key
                current.predecessor,current.parent.predecessor = current.parent.predecessor,current.predecessor
                self.map[current.parent.id] = current.parent
                self.map[current.id] = current
                current = current.parent


            self.ll._set_minimum()

    
    def delete(self,_id):
        self.decrease_key(_id,float("-inf"))
        self.remove_min()



