from collections import deque



class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"





def get_values_at_certain_height(root,height):
    
    queue =deque()
    
    queue.append(root)
    root.height = 1

    
    values = []
    while queue:
        current_node = queue.popleft()

        if current_node.height == height:
            values.append(current_node.value)
        elif current_node.height > height:
            break


        if current_node.left:
            current_node.left.height = current_node.height + 1
            queue.append(current_node.left)

        if current_node.right:
            current_node.right.height = current_node.height + 1
            queue.append(current_node.right)

    
    return values




if __name__ == "__main__":
    

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(7)


    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6


    print(get_values_at_certain_height(n1,3))


