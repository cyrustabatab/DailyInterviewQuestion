

class Node:

    def __init__(self,_id,key,predecessor):
        self.id = _id
        self.key = key
        self.predecessor = predecessor
        self.next = self.prev = None
        self.child = self.parent = None
        self.degree = 0
        self.marked = False

    def __repr__(self):
        return f"Node({self.id},{self.key})"

class FibonacciHeap:

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
        if isinstance(heap,FibonacciHeap):
            if heap.empty:
                return

            if self.empty:
                self.minimum = heap.minimum
                self.size = heap.size
                return


            temp = heap.minimum.prev
            heap.minimum.prev = self.minimum
            self.minimum.next.prev = temp
            temp.next = self.minimum.next
            self.minimum.next = heap.minimum

            if heap.minimum.key < self.minimum.key:
                self.minimum = heap.minimm

            self.size += heap.size
    
    def add(self,_id,key,predecessor):
        node = Node(_id)
        self.map[_id] = node

        if not self.minimum:
            self.minimum = node
            node.next = node
            node.prev = node
        else:

            node.prev = self.minimum.prev
            node.next = self.minimum
            self.minimum.prev.next = node
            self.minimum.prev = node


        self.size += 1


    def remove_min(self):

        if self.minimum:
            value = self.minimum
            del self.map[value.id]


            current = self.minimum.child
            first = True

            while current is not self.minimum.child or first:
                if first:
                    first = False
                temp = current.next
                current.prev = self.minimum.prev
                current.next = self.minimum
                self.minimum.prev.next = current
                self.minimum.prev = current
                current = temp



            self.minimum.prev.next = self.minimum.next
            self.minimum.next.prev = self.minimum.prev

            if self.minimum.next is self.minimum:
                self.minimum = None
            else:
                self.minimum = self.minimum.next
                self._consolidate()

            self.size -= 1
            return value
    

    def _consolidate(self):


        degrees = [None] * (int(math.log(self.size)) + 1)


        nodes = []

        current = self.minimum
        first = True

        while current is not self.minimum or first:
            if first:
                first = False
            temp = current.next
            nodes.append(current)
            current = temp



        for node in nodes:
            x = node
            x_degree = x.degree

            while degrees[x_degree]:
                y = degrees[x_degree]

                if y.key < x.key:
                    x,y = y,x

                self._link(y,x)

                x_degree += 1
            

            degrees[x_degree] = x


        self.minimum = None


        for node in nodes:
            if node:
                if not self.minimum:
                    self.minimum = node
                    node.next =node
                    node.prev = node
                else:
                    node.prev = self.minimum.prev
                    node.next = self.minimum
                    self.minimum.prev.next = node
                    self.minimum.prev =node

                    if node.key < self.minimum.key:
                        self.minimum = node



    

    def _link(self,y,x):

        y.prev.next = y.next
        y.next.prev = y.prev

        if not x.child:
            x.child = y
            y.next = y
            y.prev = y
        else:
            y.prev = x.child.prev
            y.next = x.child
            x.child.prev.next = y
            x.child.prev = y


        y.parent = x
        y.marked = False
        x.degree += 1


    
    def decrease_key(self,_id,key,predecessor=None):

        if _id in self.map:

            node = self.map[_id]

            if key >= node.key:
                return

            node.key = key
            node.predecessor = predecessor


            if node.parent and node.key < node.parent.key:
                self.cut(node,node.parent)
                self.cascading_cut(node.parent)
            

            if node.key < self.minimum.key:
                self.minimum = node

    def cut(self,x,y):

        x.prev.next = x.next
        x.next.prev = x.prev

        if y.child is x:
            if x.next is x:
                y.child = None
            else:
                y.child  = x.next

        x.prev = self.minimum.prev
        x.next = self.minimum
        self.minimum.prev.next = x
        self.minimum.prev = x
        x.parent = None
        x.marked = False



    def cascading_cut(self,y):
        z = y.parent

        if z:
            if not y.marked:
                y.marked = True
            else:
                self.cut(y,z)
                self.cascading_cut(z)


    
    def delete(self,_id):
        if _id in self.map:
            self.decrease_key(_id,float("-inf"))
            self.remove_min()



