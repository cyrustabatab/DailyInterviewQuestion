

def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])

    if same:
        return 0

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1


class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


def partition(ll,value):
    
    temp = Node(value)
    temp.next = ll

    current = ll
    boundary = temp
    while current:
        if current.value < value:
            boundary = boundary.next
            current.value,boundary.value = boundary.value,current.value

        current = current.next

    temp.value,boundary.value = boundary.value,temp.value

    return temp.next


def reverse_k(ll,k):

    current = ll
    new_head = None
    previous_end = None
    current_head  = ll
    end = False
    while current:
        print (current)
        count = 1
        previous = None 
        next_end = current
        while count <= k:
            temp =current.next
            current.next = previous
            previous = current
            
            if not temp:
                end = True
                break
            count += 1
            current= temp
        if not previous_end:
            new_head = previous
        else:
            previous_end.next = previous
        
        previous_end =  next_end
        if end:
            break




    
    return new_head


def shift(ll,k):
    previous = None
    slow = fast = ll

    for _ in range(k):
        fast = fast.next
    
    end = None
    while fast:
        previous = slow
        slow =slow.next 
        if not fast.next:
            end = fast
        fast = fast.next

    previous.next = None

    new_head = slow
    end.next = ll

    return new_head









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

    n1 = shift(n1,2)

    display(n1)
