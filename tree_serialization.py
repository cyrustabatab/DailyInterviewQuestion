

l

def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash =0
    same = True
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False
        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash *x + ord(s2[i])

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1

    

class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(selelf):

        return f"Node({self.value})"



def serialize(root):


    if not root:
        return '#'

    s = str(root.value)
    s +=  ' ' + serialize(root.left)
    s += ' '  + serialize(root.right)

    return s 


def deserialize(data):
    
    def helper():
        value = next(values)
        if value == '#':
            return None
        node = Node(int(value))
        node.left = helper()
        node.right = helper()
        return node
    
    values = iter(data.split())
    return node







if __name__ == "__main__":
    
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n7 = Node(7)

    n1.left = n3
    n1.right = n4
    n3.left = n2
    n3.right = n5
    n4.right = n7


    print(serialize(n1))
