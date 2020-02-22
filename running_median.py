



def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])

    if same:
        return True

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter__to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter__to_remove)) * x + ord(letter_to_add)
        if current_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def largest_bst(root):
    max_size = [0]
    max_node = [None]
    largest_bst_helper(root,max_size,max_node)

def largest_bst_helper(node,max_size,max_node):

    if not node:
        return (0,float("inf"),float("-inf")) #size,min value,max value
    
    left = largest_bst_helper(node.left,max_size,max_node)
    right = largest_bst_helper(node.right,max_size,max_node)

    if node.value > left[2] and node.value < right[1]:
        size = 1 + left[0] + right[0]
        if size > max_size[0]:
            max_size[0] = size
            max_node[0] = node
        return (size,min(node.value,left[1]),max(node.value,right[2]))
    else:
        return (left[0] + right[0],float("-inf"),float("inf"))
    





class Heap:

    def __init__(self,max_heap=False):
        self.a  = [None]
        if max_heap:
            self.comparator = lambda x,y: x > y
        else:
            self.comparator = lambda x,y: x < y
    
    def min_or_max(self):
        try:
            return self.a[1]
        except:
            raise ValueError("Empty Heap")
    def __len__(self):
        return self.size

    @property
    def size(self):
        return len(self.a) - 1
    
    
    def add(self,number):
        self.a.append(number)
        self.swim()
    
    def sink(self):
        i = 1 

        while i * 2 <= self.size:
            j = i * 2

            if j + 1 <= self.size and self.comparator(self.a[j + 1],self.a[j]):
                j += 1

            if self.comparator(self.a[j],self.a[i]):
                self._swap(i,j)
                i = j
            else:
                return

    def remove(self):
        try:
            value = self.a[1]
        except IndexError:
            raise ValueError("Empty Heap")
        
        self._swap(1,self.size)
        del self.a[self.size]

        self.sink()

        return value

    def swim(self):
        i = self.size

        while i // 2 >= 1 and self.comparator(self.a[i],self.a[i//2]):
            self._swap(i,i//2)
            i //= 2


    def _swap(self,i,j):
        self.a[i],self.a[j] =self.a[j],self.a[i]


def get_median(min_heap,max_heap):

    min_length = len(min_heap)
    max_length = len(max_heap)


    if (min_length + max_length) % 2 == 0:
        median = (min_heap.min_or_max() + max_heap.min_or_max()) / 2
    else:
        if min_length > max_length:
            median = min_heap.min_or_max()
        else:
            median = max_heap.min_or_max()


    return median

def add(min_heap,max_heap,num):
    if not min_heap and not max_heap:
        max_heap.add(num)
        return


    median = get_median(min_heap,max_heap)

    if num <= median:
        max_heap.add(num)
    else:
        min_heap.add(num)



def rebalance(min_heap,max_heap):

    min_length = len(min_heap)
    max_length = len(max_heap)

    if max_length > min_length + 1:
        value = max_heap.remove()
        min_heap.add(value)
    elif min_length > max_length + 1:
        value = min_heap.remove()
        max_heap.add(value)



def running_median(stream):

    min_heap = Heap()
    max_heap = Heap(max_heap=True)

    for num in stream:
        add(min_heap,max_heap,num)
        rebalance(min_heap,max_heap)
        print(get_median(min_heap,max_heap))

