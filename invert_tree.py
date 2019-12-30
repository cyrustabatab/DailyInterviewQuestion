from collections import deque
import hashlib


class BloomFilter:

    def __init__(self,a=1000,k=3):
        self.a = [False] * a
        self.hash_algorithms = [hashlib.sha1,hashlib.sha256,hashlib.sha384,hashlib.sha512,hashlib.md5]
        self.hash_functions = [self._get_hash_function(f) for f in self.hash_algorithms[:k]]
    

    def _get_hash_function(self,f):
        def hash_function(value):

            value = f(str(value).encode('utf-8')).hexdigest()
            return int(value,16) % len(self.a)
        

        return hash_function

    
    def add(self,value):

        for f in self.hash_functions:
            self.a[f(value)] = True


    def __contains__(self):
        return all(f(value) for f in self.hash_functions)





class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"



def preorder(node):
    if not node:
        return

    print(node.value,end=' ')
    preorder(node.left)
    preorder(node.right)



def invert_tree(root):

    queue = deque()

    queue.append(root)

    while queue:
        current = queue.popleft()

        current.left,current.right = current.right,current.left

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    


if __name__ == "__main__":
    

    n1 = Node('a')
    n2 = Node('b')
    n3 = Node('c')
    n4 = Node('d')
    n5 = Node('e')
    n6 = Node('f')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6

    preorder(n1)
    print()
    invert_tree(n1)

    preorder(n1)
    print()






