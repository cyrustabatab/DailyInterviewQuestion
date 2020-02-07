


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return f"Node({self.value})"


def count_unival_trees(root):
    return count_unival_helper(root)[0]


def count_unival_helper(root):

    if not root:
        return 0,True

    

    left_count,is_left_unival = count_unival_helper(root.left)

    right_count,is_right_unival = count_unival_helper(root.right)

    
    if is_left_unival and is_right_unival:

        if root.left and root.value != root.left.value:
            return left_count + right_count,False

        if root.right and root.value != root.right.value:
            return left_count + right_count,False

        return 1 + left_count + right_count,True

    return left_count + right_count,False



