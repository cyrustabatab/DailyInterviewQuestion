
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"

def get_length(ll):

    if not ll:
        return 0

    return 1 + get_length(ll.next)

def ll_intersection(l1,l2):

    length_1 = get_length(l1)
    length_2 = get_length(l2)
    
    larger,smaller =(l1,l2) if length_1 >= length_2 else (l2,l1)

    for _ in range(abs(length_2 - length_1)):
        larger = larger.next


    while larger is not smaller:
        larger = larger.next
        smaller = smaller.next

    return larger

if __name__ == "__main__":
    
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n6 = Node(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    n6.next = n3
    n3.next = n4



    print(ll_intersection(n1,n6))
