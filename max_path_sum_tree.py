


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"




def max_path_sum_tree(root):

    current_path_sum = 0
    max_path_sum = float("-inf")


    max_path_helper(root,current_path_sum,max_path_sum)

    return max_path_sum


def max_path_helper(node,current_path_sum,max_path_sum):

    if not node:
        return

    current_path_sum += node.value 
    if not node.left and not node.right:
        if current_path_sum > max_path_sum:
            max_path_sum = current_path_sum


    max_path_helper(node.left,current_path_sum,max_path_sum)
    max_path_helper(node.right,current_path_sum,max_path_sum)







