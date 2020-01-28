


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None
    

    def __repr__(self):
        return f"Node({self.value})"


def find_deepest_node(node,current_height,max_height,max_node):

    if not node:
        return

    if not node.left and not node.right:
        if current_height > max_height[0]:
            max_height[0] = current_height
            max_node[0] = node
        return


    find_deepest_node(node.left,current_height + 1,max_height,max_node)
    find_deepest_node(node.right,current_height + 1,max_height,max_node)



def deepest(node):

    if node and not node.left and not node.right:
        return (node,0) 


    if not node.left: #if no left node, deepest is on right
        return increment_depth(deepest(node.right))
    elif not node.right: 
        return increment_depth(deepest(node.left))


    return increment_depth(max(deepest(node.left),deepest(node.right),key=lambda x:x[1]))
    



def increment_depth(node_tuple):
    node,depth = node_tuple

    return (node,depth + 1)






