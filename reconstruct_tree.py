

def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53


class Node:

    def __init__(self,value):
        self.value = value
        self.left = self.right = None


def _preorder(root):
    
    if not root:
        return
    print(root.value,end=' ')
    _preorder(root.left)
    _preorder(root.right)

def _inorder(root):
    if not root:
        return

    _inorder(root.left)
    print(root.value,end=' ')
    _inorder(root.right)



def reconstruct(inorder,preorder):

    value_to_index = {num:i for i,num in enumerate(inorder)}

    return reconstruct_helper(inorder,0,len(inorder) -1,preorder,0,len(preorder) - 1,value_to_index)


def reconstruct_helper(inorder,in_low,in_high,preorder,pre_low,pre_high,value_to_index):
    if in_low > in_high:
        return None
    if in_low == in_high:
        return Node(inorder[in_low])


    root_value = preorder[pre_low]

    root = Node(root_value)


    root_index = value_to_index[root_value]

    root.left = reconstruct_helper(inorder,in_low,root_index - 1,preorder,pre_low + 1,pre_low + (root_index - in_low),value_to_index)
    root.right = reconstruct_helper(inorder,root_index + 1,in_high,preorder,pre_low + (root_index - in_low) +1,pre_high,value_to_index)


    return root


if __name__ == "__main__":
    
    inorder = [1,2,3,4,5,6,7]
    preorder = [4,2,1,3,6,5,7]
    
    root = reconstruct(inorder,preorder)

    _inorder(root)
    print()
    _preorder(root)

