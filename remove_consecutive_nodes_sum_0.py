
class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"



def remove_consecutive_nodes_sum_0(ll):

    

    previous = None
    current = ll
    while current:
        second = current
        s = 0 #sum

        while second:
            s += second.value
            if s == 0:
                break
            second = second.next

        if second:
            print(second)
            if not previous:
                ll = second.next
            else:
                previous.next = second.next

            current = second.next
        else:
            previous = current
            current = current.next

    return ll 




def display(ll):
    if not ll:
        return
    print(ll.value,end=('->' if ll.next else '\n'))

    display(ll.next)


if __name__ == "__main__":
    

    n1 = Node(10)
    n2 = Node(-10)
    n3 = Node(-3)
    n4 = Node(-3)
    n5 = Node(1)
    n6 = Node(4)
    n7 = Node(-4)

    n1.next = n2
    n2.next= n3
    n3.next= n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    display(n1)

    n1 = remove_consecutive_nodes_sum_0(n1)

    display(n1)
    





