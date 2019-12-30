



class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def find_floor_ceiling(root,key):

    floor = float('-inf')
    ceiling = float('inf')

    current = root

    while current:
        if key == current.value:
            return key,key
        if key > current.value:
            floor =current.value
            current =current.right
        else:
            ceiling = current.value
            current = current.left


    return floor,ceiling



if __name__ == "__main__":
    

    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(find_floor_ceiling(root,5))
