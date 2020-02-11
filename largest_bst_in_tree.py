


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None


    def __repr__(self):
        return f"Node({self.value})"



def is_bst(root,minValue=float("-inf"),maxValue=float("inf")):
    if not root:
        return True

    if not minValue <= root <= maxValue:
        return False

    return is_bst(root.left,minValue=minValue,maxValue=root.value) and is_bst(root.right,maxValue=maxValue,minValue=root.value)


#def largest_bst_helper(root,max_size,max_root):
#    if root is None:
#        return (0,float('inf'),float('-inf')) #size,min_key,max_key
#
#    left = largest_bst_helper(root.left,max_size)
#    right = largest_bst_helper(root.right,max_size)
#
#    if root.key > left[2] and root.key < right[1]:
#        size = leaf[0] + right[0] + 1
#        if size > max_size[0]:
#            max_size[0] = size
#            max_root[0] = root
#        
#        return (size,min(root.key,left[1]),max(root.key,right[2]))
#    else:
#        return (0,float("-inf"),float('inf'))

    





def largest_bst_subtree(root):

    def largest_bst_helper(root,max_size,max_node):
        if root is None:
            return (0,float('inf'),float('-inf')) #size,min_key,max_key

        left = largest_bst_helper(root.left,max_size,max_node)
        right = largest_bst_helper(root.right,max_size,max_node)

        if root.value > left[2] and root.value < right[1]:
            size = left[0] + right[0] + 1
            if size > max_size[0]:
                max_size[0] = size
                max_node[0] = root
            
            return (size,min(root.value,left[1]),max(root.value,right[2]))
        else:
            return (0,float("-inf"),float('inf'))

    max_size = [0]
    max_node = [None]
    largest_bst_helper(root,max_size,max_node)

    return max_size[0],max_node[0]


def branch_sum(root,sums,current_sum):
    if not root:
        return

    current_sum += root.value

    if not root.left and not root.right:
        sums.append(current_sum)
        return

    branch_sum(root.left,sums,current_sum)
    branch_sum(root.right,sums,current_sum)




if __name__ == "__main__":
    
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.right = n10


    sums = []
    current_sum = 0
    branch_sum(n1,sums,current_sum)

    print(sums)




