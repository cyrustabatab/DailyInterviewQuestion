

class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def validate_bst(root):

    return validate_bst_helper(root) > -1

def validate_bst_helper(node,minValue=float("-inf"),maxValue=float('inf')):
    if not node:
        return True


    if not minValue < node.value <= maxValue:
        return False

    
    left = validate_bst_helper(node.left,minValue=minValue,maxValue=node.value)

    return left and validate_bst_helper(node.right,minValue=node.value,maxValue=maxValue)


