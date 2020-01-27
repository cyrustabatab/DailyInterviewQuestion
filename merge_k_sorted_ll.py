import heapq


class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __repr__(self):

        current = self

        ll = ''
        while current:
            ll += f"{current.value}" + ("->" if current.next else '')

        return ll


def merge(lists): #(O(kn * logn)
    
    heap = [(l.value,i) for i,l in enumerate(lists)] #O(k)
    heapq.heapify(heap)

    new_head = None 
    previous = None
    while heap:
        current_minimum,i = heapq.heappop(heap)

        if previous is None:
            new_head = lists[i]
        else:
            previous.next = lists[i]
        
        previous = lists[i]
        lists[i] = lists[i].next
        if lists[i]:
            heapq.heappush(heap,(lists[i].value,i))

    return new_head


def display(ll):
    current = ll
    
    while current:
        print(current.value,end=('->' if current.next else '\n'))
        current = current.next

if __name__ == "__main__":
    
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    
    n1.next = n2
    n2.next= n3

    n4 = Node(2)
    n5 = Node(4)
    n6 = Node(6)

    n4.next = n5
    n5.next = n6


    display(n1)

    display(n4)
    
    lists = [n1,n4]
    head = merge(lists)

    display(head)


    








    
















