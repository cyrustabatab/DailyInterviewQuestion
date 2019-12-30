

class Node:


    def __init__(self,value):
        self.value = value
        self.next = None


    def __repr__(self):
        return f"Node({self.id})"

def reverse_ll_2(ll,previous=None):
    
    temp = ll.next
    ll.next= previous
     
    if not temp:
        return ll
    else:
        return reverse_ll_2(temp,ll)




def reverse_ll(ll):

    previous = None
    current = ll


    while True:
        temp = current.next
        current.next = previous
        previous = current
        if not temp:
            break
        current = temp

    
    return current


def display(ll):

    current = ll

    while current:
        print(current.value,end=('->' if current.next else '\n'))
        current = current.next

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

    head = reverse_ll_2(n1)

    display(head)



