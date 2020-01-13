

class Node:


    def __init__(self,value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


# 1->2->3->4->5

def remove_kth_from_end(ll,k):

    slow = fast = ll

    for _ in range(k):
        fast = fast.next

    previous = None 
    while fast:
        previous = slow
        slow = slow.next
        fast = fast.next
    
    if not previous:

        ll = slow.next
    else:
        previous.next = slow.next
    return ll


def display(ll):

    if not ll:
        return
    
    print(ll.value,end=('->' if ll.next else '\n'))
    display(ll.next)

if __name__ == "__main__":
    

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    display(n1)

    n1 = remove_kth_from_end(n1,5)

    display(n1)



