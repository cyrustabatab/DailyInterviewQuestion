



class Node:


    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"





def fullBinaryTree(node):

    if not node:
        return


    left = fullBinaryTree(node.left)
    right = fullBinaryTree(node.right)

    if (left and right) or (not left and not right):
        
        node.left = left
        node.right = right
        return node


    if left:
        return left

    if right:
        return right




