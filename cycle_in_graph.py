from enum import Enum

class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

class Node:

    def __init__(self,_id):
        self._id = _id
        self.neighbors = {}
        self.state = State.UNVISITED

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
    
    def __iter__(self):
        return iter(self.node_list.values())

    def __getitem__(self,_id):
        return self.node_list.get(_id)

    def __repr__(self):
        g = ''

        for node in self:
            g += f"{node.id}: "
            g += ','.join(str(neighbor.id) for neighbor in node.get_neighbors()) + '\n'

        return g

def dfs_visit(node,parent):
    #no need for parent state node  

    node.state = State.VISITING

    for neighbor in node.get_neighbors():
        if neighbor.state == State.UNVISITED:
            if dfs_visit(neighbor,node):
                return True
        #for undirctre
        if neighbor is not parent and neighbor.state == State.VISITING:
            return True

    node.state = State.VISITED
    return False




def has_cycle_undirected(g):
    
    for node in g:
        if node.state == State.UNVISITED:
            if dfs_visit(node,None):
                return Tru






