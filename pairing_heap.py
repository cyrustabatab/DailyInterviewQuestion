


class BIT:

    def __init__(self,nums):
        self.a = [0] * (len(nums) + 1)
        
        for i,num in enumerate(nums):
            self.update(i + 1,num)

    def update(self,index,num):

        while index < len(self.a):
            self.a[index] +=num
            index += index & -index


    def query(self,index):
        total = 0

        while index > 0:
            total += self.a[index]
            index -= index & -index

        return total

    def range_query(self,a,b):
        return self.query(b) - self.query(a - 1)


def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current__hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])
    
    if same:
        return 0
    

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)

        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1

class Node:

    def __init__(self,_id,key,predecessor):
        self.id = _id
        self.key = key
        self.predecessor = predecessor
        self.prev= self.next = None
        self.child = None
    

    def add_child(self,node):

        node.next = self.child
        if self.child:
            self.child.prev = node

        node.previous = self
        self.child = node

        




class PairingHeap:


    def __init__(self):
        self.minimum = None
        self.map = {}
        self.size = 0


    @property
    def empty(self):
        return self.size == 0


    def __len__(self):
        return self.size
    
    
    def merge(self,heap):
        if isinstance(heap,PairingHeap):
            if heap.empty:
                return

            if self.empty:
                self.minimum = heap.minimum
                self.size = heap.size
                return

            if heap.minimum.key < self.minimum.key:
                heap.minimum.add_child(self.minimum)
                self.minimum = heap.minimum
            else:
                self.minimum.add_child(heap.minimum)

            self.size += heap.size



    def add(self,_id,key,predecessor):
        node = Node(_id,key,predecessor)
        self.map[_id] = node
        self.size += 1
        
        if node.key < self.minimum.key:
            node.add_child(self.minimum)
            self.minimum = node
        else:
            self.minimum.add_child(node)

    
    def two_pass(self,node):


        stack = []

        current = node

        while current:
            current.prev = None
            if not current.next:  
                stack.append(current)
                break
            tempe = current.next.next
            current.prev = None
            current.next.prev = None
            current.next.next = None

            if current.key <= current.next.key:
                current.add_child(current)
                current.next = None
                stack.append(current)
            else:
                current.next.add_child(current)
                stack.append(current.next)
        
            current = temp

        if not stack:
            return

        current = stack.pop()
        while stack:
            previous = stack.pop()
            if current.key <= previous.key:
                current.add_child(previous)
            else:
                previous.add_child(current);
                current = previous

        return current


    
    def remove_min(self):
        if not self.empty:
            value = self.minimum
            new_root = self.two_pass(self.minimum.child)
            self.size -= 1
            self.root = new_root

            return value
    

    def decrease_key(self,_id,key,predecessor):
        if _id in self.map:
            node = self.map[_id]

            if key >= node.key:
                return

            node.key = key
            node.predecessor = predecessor
            if node is self.root: 
                return

            if node.previous:
                if node.previous.child is node:
                    node.previous.child = node.next
                else:
                    node.previous.next = node.next

            if node.next:
                node.next.prev = node.prev


            if node.key < self.minimum.key:
                node.add_child(self.minimum)
                self.minimum = node
            else:
                self.minimum = node
    

    def remove(self,_id):
        if _id in self.map:
        
            if node.previous:
                if node.previous.child is node:
                    node.previous.child = node.next
                else:
                    node.previous.next = node.next

            if node.next:
                node.next.prev = node.prev

            new_root = self.two_pass(node.child)

            if new_root:
                if new_root.key < self.minimum.key:
                    new_root.add_child(self.minimum)
                    self.minimum = new_root
                else:
                    self.minimum.add_child(new_root)




