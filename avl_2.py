

class Node:

    def __init__(self,key,value,parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = self.right = None
        self.balanceFactor = 0

    def __repr__(self):
        return f"Node({self.key},{self.value})"


class AVL:


    def __init__(self):
        self.root= None
        self.size = 0

    def __len__(self):
        return self.size


    def __setitem__(self,key,value):
        if not self.root:
            self.root = Node(key,value)
        else:
            current = self.root
            

            while True:
                if current.key == key:
                    current.value = value
                    return



                if key < current.key:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(key,value,current)
                        self.updateBalancesAfterAddition(current.left)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(key,value,current)
                        self.updateBalancesAfterAddition(current.right)
                        break
        

        self.size += 1
    

    def __contains__(self,key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True


    def __getitem__(self,key):

        current = self.root

        while True:
            if current.key == key:
                return current.value


            if key < current.key:
                current = current.left
            else:
                current = current.right


        raise KeyError(f"Key {key} not found")
    
    
    def rotateRight(self,node):
        new_root = node.left

        assert new_root

        node.left = new_root.right

        if new_root.right:
            new_root.right.parent = node

        new_root.parent = node.parent
        if node.parent:
            if node.parent.left is node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        else:
            self.root = new_root


        node.parent =new_root
        new_root.right = node









    def rotateLeft(self,node):
        new_root = node.right

        assert new_root

        node.right = new_root.left

        if new_root.left:
            new_root.right.parent = node

        new_root.parent = node.parent

        if node.parent:
            if node.parent.left is node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        else:
            self.root = new_root

        node.parent = new_root
        new_root.left = node
    

    def rebalance(self,node):
        pass

    def updateBalancesAfterAddition(self,node): 

        if not -1 <= node.balanceFactor <= 1:
            self.rebalance(node)
            return
        

        if node.parent:
            if node.parent.left is node:
                node.parent.balanceFactor += 1
            else:
                node.parent.balanceFactor -= 1


            if node.parent.balanceFactor != 0:
                self.updateBalancesAfterAddition(node.parent)












