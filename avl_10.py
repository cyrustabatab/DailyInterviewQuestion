


def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53

    for i in range(len(s2),len(s1)):
        if same 

class Node:


    def __init__(self,key,value,parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = self.right = None


    def __repr__(self):
        return f"Node({self.id})"



class AVL:

    def __init__(self):
        self.root = None
        self.size = 0


    @property
    def empty(self):
        return self.size == 0

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
                        current.left = Node(key,value,parent=current)
                        self.updateBalancesAfterAddition(current.left)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(key,value,parent=current)
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

        while current:
            if current.key == key:
                return current.value


            if key < current.key:
                current = current.left
            else:
                current = current.right
        

        raise KeyError(f"Key {key} not in tree")

    
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


        new_root.right = node
        node.parent = new_root

        
        node.balanceFactor =node.balanceFactor -1 - max(new_root.balanceFactor,0)
        new_root.balanceFactor = new_root.balanceFactor - 1 + min(node.balanceFactor,0)




    def rotateLeft(self,node):
        new_root = node.right

        assert new_root

        node.right = new_root.left

        if new_root.left:
            new_root.left.parent = node

        new_root.parent = node.parent

        if node.parent:
            if node.parent.left is node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        else:
            self.root = new_root


        new_root.left = node

        node.parent = new_root

        node.balanceFactor = node.balanceFator + 1 - min(new_root.balanceFactor,0)
        new_root.balanceFactor = new_root.balanceFactor  + 1+ max(node.balanceFactor,0)





    def updateBalancesAfterDeletion(self,node):
        if node.balanceFactor in (-1,1):
            return


        if not -1 <= node.balanceFactor <= 1:
            stopAfterRebalancing = False

            if node.balanceFactor > 0:
                if node.left.balanceFactor == 0:
                    stopAfterRebalancing = True
            else:
                if node.right.balanceFactor == 0:
                    stopAfterRebalancing = True


            self.rebalance(node)

            if stopAfterRebalancing:
                return


        if node.parent:
            if node.parent.left is node:
                node.parent.balanceFactor -= 1
            else:
                node.parent.balanceFactor += 1


            self.updateBalancesAfterDeletion(node.parent)

    

    def rebalance(self,node):

        if node.balanceFactor > 0:
            if node.left.balanceFactor < 0:
                self.rotateLeft(node.left)
            self.rotateRight(node)
        else:
            if node.right.balanceFactor > 0:
                self.rotateRight(node.right)
            self.rotateLeft(node)
    

    def __delitem__(self,key):
        self._delete(self.root,key)
    

    def _delete(self,node,key):

        current = node

        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                if current.left and current.right:
                    current.key,current.value = self._getMinValueFrom(node.right)
                    self._delete(current.right,current.key)
                elif current.parent is None:
                    if current.left:
                        current.key,current.value,current.balanceFactor = current.left.key,current.left.value,current.left.balanceFactor
                        
                        current.right = current.left.right

                        if current.right:
                            current.right.parent = current

                        current.left = current.left.left

                        if current.left:
                            current.left.parent = current
                    elif current.right:
                        current.key,current.value,current.balanceFactor = current.right.key,current.right.value,current.right.balanceFactor

                        current.left = current.right.left

                        if current.left:
                            current.left.parent = current

                        current.right = current.right.right

                        if current.right:
                            current.right.parent = current
                    else:
                        self.root = None
                elif current.parent.left is current:
                    current.parent.left = current.left if current.left else current.right

                    if current.left:
                        current.left.parent = current.parent
                    elif current.right:
                        current.right.parent = current.parent


                    current.parent.balanceFactor -= 1
                    self.updateBalancesAfterDeletion(current.parent)
                elif current.parent.right is current:
                    current.parent.right = current.left if current.left else current.right


                    if current.left:
                        current.left.parent = current.parent
                    elif current.right:
                        current.right.parent = current.parent


                    current.parent.balanceFactor += 1
                    self.updateBalancesAfterDeletion(current.parent)




    
    def _getMinValueFrom(self,node):
        if not node.left:
            return node.key,node.value

        return self._getMinValueFrom(node.left)

