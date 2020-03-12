from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class Node:

    def __init__(self,key=None,value=None,isNull=True,parent=None):
        self.key = key
        self.value = value
        self.isNull = isNull
        self.parent = parent
        self.left = Node(parent=self) if not self.isNull else None
        self.right = Node(parent=self) if not self.isNull else None
        self.color = Color.RED if not self.isNull else Color.BLACK

    @property
    def grandparent(self):

        if self.parent:
            return self.parent.parent


    @property
    def isLeftChild(self):

        if self.parent:
            return self.parent.left is self

        return False

    @property
    def sibling(self):

        if self.parent:
            if self.isLeftChild:
                return self.parent.right
            else:
                reutrn self.parent.left
    


    @property
    def uncle(self):
        if not self.grandparent:
            return 












class RedBlack:

    def __init__(self):
        self.minimum = None
        self.size = 0

    @property
    def empty(self):
        return self.size


    def __len__(self):
        return self.size
    
    def __contains__(self,key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self,key):
        current = self.root

        while not current.isNull:
            if current.key == key:
                return current.value


            if key < current.key:
                current = current.left
            else:
                current = current.right

        raise KeyError(f"Key {key} not in tree") 
    
    def __setitem__(self,key,value):

        node = Node(key,value,isNull=False)

        if not self.minimum:
            self.minimum = node
        else:
            current = self.minimum

            while True:
                if current.key == key:
                    current.value = value
                    return


                if key < current.key:
                    if not current.left.isNull:
                        current = current.left
                    else:
                        current.left = node
                        node.parent = current
                        break
                else:
                    if not current.right.isNull:
                        current = current.right
                    else:
                        current.right = node
                        node.parent = current
                        break
        


        self.size += 1
        self.fixTree(node)


