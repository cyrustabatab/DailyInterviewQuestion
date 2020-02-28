from enum import Enum
from collections import defaultdict


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2



class Node:


    def __init__(self,_id):
        self._id = _id
        self.neighbors = {}

    @property
    def id(self):
        return self._id

    def get_neighbors(self):
        return self.neighbors.keys()

    def add_neighbor(self,node,weight=0):
        self.neighbors[node] = weight

    def get_weight(self,node):
        return self.neighbors.get(node)

    def __repr__(self):
        return f"Node({self.id})"


class Graph:

    def __init__(self,directed=False):
        self.directed = directed
        self.node_list = {}
        self._edges = 0

    @property
    def num_edges(self):
        return self._edges

    @property
    def num_vertices(self):
        return len(self.node_list)

    @property
    def vertices(self):
        return self.node_list.keys()

    def add_vertex(self,_id):
        if _id not in self.node_list:
            node = Node(_id)
            self.node_list[_id] = node

    def add_edge(self,n1,n2,weight=0):
        if n1 not in self.node_list:
            self.add_vertex(n1)

        if n2 not in self.node_list:
            self.add_vertex(n2)

        self.node_list[n1].add_neighbor(self.node_list[n2],weight)

        if not self.directed:
            self.node_list[n2].add_neighbor(self.node_list[n1],weight)

        self._edges += 1
    
    def __repr__(self):
        g = ''

        for node in self:
            g += f"{node.id}: "
            g += ','.join(str(neighbor.id) for neighbor in node.get_neighbors()) + '\n'
        return g


def dfs_visit(node,parent):

    node.state = State.VISITING

    for neighbor in node.get_neighbors():
        if neighbor.state == State.UNVISITED:
            if dfs_visit(neighbor,node):
                return True

        if neighbor.state == State.VISITING and node is not parent:
            return True

    neighbor.state = State.VISITED
    return False


def cycle_detection(g):

    for node in g:
        if node.state == State.UNVISITED:
            if dfs_visit(node,None):
                return True


    return False



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

    return -1


def dfs_visit(graph,visited,current_word,start_word,length):


    if length == 1:
        if start_word[0] == current_word[-1]:
            return True
        else:
            return False
    
    visited.add(current_word)

    for neighbor in graph[current_word[-1]]:
        if neighbor not in visited:
            if dfs_visit(graph,visited,neighbor,start_word,length -1):
                return True


    visited.remove(current_word)

    return False
        
def circle_chained_words(words):

    graph = defaultdict(list)

    for word in words:
        graph[word[0]].append(word)


    visited = set() 
    return dfs_visit(graph,visited,words[0],words[0],len(words))

    
if __name__ == "__main__":
    

    words = ["steal","lac","cyrus","nac","cinnamon"]
    words_2 = ["eggs","cyrus","james"]


            
    print(circle_chained_words(words_2))



