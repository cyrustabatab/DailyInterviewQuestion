import hashlib
import unittest


class Trie:
    END_SYMBOL = "*"
    def __init__(self):
        self.root = {}

    def add(self,word):

        current = self.root

        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]

        current[Trie.END_SYMBOL] = True

    def __contains__(self,word):

        current = self.root

        for c in word:
            if c not in current:
                return False
            current = current[c]

        return Trie.END_SYMBOL in current
    
    def autocomplete(self,partial_word):
        current = self.word
        words = []
        for c in partial_word:
            if c not in current:
                break
            current = current[c]
        else:
            self.getWordsFrom(current,list(partial_word),words)
        
        return words

    def delete(self,word):
        current = self.root
        for c in word:
            if c not in current:
                return
            current = current[c]

        if Trie.END_SYMBOL not in current:
            return

        del current[Trie.END_SYMBOL]

        if len(current) >= 1:
            return

        self._removeLastNodeWithMultipleChildren(word)
    
    def _removeLastNodeWithMultipleChildren(self,word):

        current = self.root
        lastNodeWithMultipleChildren = None
        childToBreak = None

        for i,c in enumerate(word[:-1]):
            if c not in current:
                return

            current = current[c]

            hasMultipleChildren = False
            count = 0
            for child in current:
                if child == Trie.END_SYMBOL:
                    hasMultipleChildren = True
                    break

                count += 1
                if count == 2:
                    hasMultipleChildren = True
                    break


            if hasMultipleChildren:
                lastNodeWithMultipleChildren = current
                childToBreak = word[i + 1]



        if lastNodeWithMultipleChildren:
            del lastNodeWithMultipleChildren[childToBreak]
        else:
            del self.root[word[0]]






class BloomFilter:

    def __init__(self,a=1000,k=3):
        self.a = [None] * a
        self.hash_algorithms = [hashlib.md5,hashlib.sha1,hashlib.sha256,hashlib.sha384,hashlib.sha512] 

        self.hash_functions = [self._get_hash_function(f) for f in self.hash_algorithms[:k]]
    

    def _get_hash_function(self,f):

        def hash_function(value):

            v = f(value.encode('utf-8')).hexdigest()
            return int(v,16)

        return hash_function





class BIT:

    def __init__(self,nums):

        self.a = [0] * (len(nums) + 1)

        for i,num in enumerate(nums):
            self.update(i + 1,num)


    def update(self,index,num):

        while index < len(self.a):
            self.a[index] += num
            index += index & -index


    def query(self,index):
        total = 0

        while index > 0:
            total += self.a[index]
            index -= index & -index

    
    def range_query(self,a,b):
        return self.query(b) - self.query(a - 1)


class Node:

    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.next = self.prev = None

    def __repr__(self):
        return f"Node({self.key},{self.value})"

class DLL:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    @property
    def empty(self):
        return self.head.next is self.tail

    def set_head_to(self,node):
        if node is self.head or node is self.tail:
            return

        if self.head.next is node:
            return

        if node.next:
            node.next.prev = node.prev
            node.prev.next = node.next

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove_tail(self):
        if self.empty:
            return

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

class LRU:

    def __init__(self,capacity=3):
        self.capacity = capacity
        self.current_size = 0
        self.cache = {}
        self.ll = DLL()
    
    def most_recent(self):
        if not self.empty:
            return self.ll.head.next.value
    @property
    def empty(self):
        return self.current_size == 0

    def __setitem__(self,key,value):
        if key not in self.cache:
            if self.current_size == self.capacity:
                self._remove_least_recent()
            else:
                self.current_size += 1


            self.cache[key] = Node(key,value)
        else:
            self._replace(key,value)

        self._set_most_recent(self.cache[key])
    
    def __getitem__(self,key):
        if key in self.cache:
            value = self.cache[key].value
            self._set_most_recent(self.cache[key])
            return value

        raise KeyError(f"Key {key} not found")

    def _set_most_recent(self,node):
        self.ll.set_head_to(node)
    
    def _remove_least_recent(self):
        key_to_remove = self.ll.tail.prev.key
        del self.cache[key_to_remove]
        self.ll.remove_tail()

    def _replace(self,key,value):
        if key in self.cache:
            self.cache[key] = value


def check_overlap(r1,r2):
    

    r1_left_x,r1_right_x,r1_bottom_y,r1_top_y = r1
    r2_left_x,r2_right_x,r2_bottom_y,r2_top_y = r2
    if (r2_left_x <= r1_left_x <= r2_right_x and r2_bottom_y <= r1_bottom_y <= r2_top_y) or \
            (r1_left_x <= r2_right_x  <= r1_right_x and r1_bottom_y <= r2_bottom_y <= r1_top_y):
                return True
    
    return False

def find_rectangular_overlap(r1,r2):

    r1_left_x,r1_right_x = r1['left_x'],r1['left_x'] + r1['width']
    r1_bottom_y,r1_top_y = r1['bottom_y'],r1['bottom_y'] + r1['height']

    r2_left_x,r2_right_x = r2['left_x'],r2['left_x'] + r2['width']
    r2_bottom_y,r2_top_y = r2['bottom_y'],r2['bottom_y'] + r2['height']

    r1_coordinates = (r1_left_x,r1_right_x,r1_bottom_y,r1_top_y)    
    r2_coordinates = (r2_left_x,r2_right_x,r2_bottom_y,r2_top_y)
    new_left_x = new_bottom_y = new_width = new_height =  None
    if check_overlap(r1_coordinates,r2_coordinates) or \
            check_overlap(r2_coordinates,r1_coordinates):
        new_left_x = max(r1_left_x,r2_left_x)
        new_width = min(r2_right_x,r1_right_x) - new_left_x
             
        new_bottom_y = max(r1_bottom_y,r2_bottom_y)
        new_height = min(r1_top_y,r2_top_y) - new_bottom_y

        if new_width <=  0 or new_height <= 0:
            new_width = new_height = new_left_x = new_bottom_y = None

    return {"left_x": new_left_x,"bottom_y": new_bottom_y,"width": new_width,"height": new_height}


    



    
if __name__ == "__main__":
    class Test(unittest.TestCase):

        def test_overlap_along_both_axes(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 1,
                'width': 6,
                'height': 3,
            }
            rect2 = {
                'left_x': 5,
                'bottom_y': 2,
                'width': 3,
                'height': 6,
            }
            expected = {
                'left_x': 5,
                'bottom_y': 2,
                'width': 2,
                'height': 2,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)


        def test_one_rectangle_inside_another(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 1,
                'width': 6,
                'height': 6,
            }
            rect2 = {
                'left_x': 3,
                'bottom_y': 3,
                'width': 2,
                'height': 2,
            }
            expected = {
                'left_x': 3,
                'bottom_y': 3,
                'width': 2,
                'height': 2,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)

        def test_both_rectangles_the_same(self):
            rect1 = {
                'left_x': 2,
                'bottom_y': 2,
                'width': 4,
                'height': 4,
            }
            rect2 = {
                'left_x': 2,
                'bottom_y': 2,
                'width': 4,
                'height': 4,
            }
            expected = {
                'left_x': 2,
                'bottom_y': 2,
                'width': 4,
                'height': 4,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)

        def test_touch_on_horizontal_edge(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 2,
                'width': 3,
                'height': 4,
            }
            rect2 = {
                'left_x': 2,
                'bottom_y': 6,
                'width': 2,
                'height': 2,
            }
            expected = {
                'left_x': None,
                'bottom_y': None,
                'width': None,
                'height': None,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)

        def test_touch_on_vertical_edge(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 2,
                'width': 3,
                'height': 4,
            }
            rect2 = {
                'left_x': 4,
                'bottom_y': 3,
                'width': 2,
                'height': 2,
            }
            expected = {
                'left_x': None,
                'bottom_y': None,
                'width': None,
                'height': None,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)

        def test_touch_at_a_corner(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 1,
                'width': 2,
                'height': 2,
            }
            rect2 = {
                'left_x': 3,
                'bottom_y': 3,
                'width': 2,
                'height': 2,
            }
            expected = {
                'left_x': None,
                'bottom_y': None,
                'width': None,
                'height': None,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)

        def test_no_overlap(self):
            rect1 = {
                'left_x': 1,
                'bottom_y': 1,
                'width': 2,
                'height': 2,
            }
            rect2 = {
                'left_x': 4,
                'bottom_y': 6,
                'width': 3,
                'height': 6,
            }
            expected = {
                'left_x': None,
                'bottom_y': None,
                'width': None,
                'height': None,
            }
            actual = find_rectangular_overlap(rect1, rect2)
            self.assertEqual(actual, expected)


    unittest.main(verbosity=2)

        
        
        

        

        


        
        



