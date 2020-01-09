




def m_coloring(graph,m):
    
    colors = {i: 0 for i in range(len(graph))}
    
    
    vertices = [v for v in range(len(graph))]
    index = 0
    m_coloring_helper(graph,colors,vertices,index)

def is_valid(graph,colors,vertex,color):

    for i,edge in enumerate(graph[vertex]):
        if i != vertex and edge != 0:
            if colors[i] == color:
                return False


    return True


def m_coloring_helper(graph,colors,vertices,index):
    if index == len(vertices):
        print(colors)
        return

    vertex = vertices[index]

    for color in range(m):

        if is_valid(colors,vertex,color):
            colors[vertex] = color

            m_coloring_helper(graph,colors,vertices,index)

            colors[vertex] = None









def m_coloring_helper(graph,colors):
    pass
    




def num_ways_recursive(n,m):

    if n == 1 or m == 1:
        return 1

    return num_ways_recursive(n -1,m) + num_ways_recursive(n,m -1)


def num_ways(n,m):

    grid = [[1 if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]


    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            grid[i][j] += (grid[i -1][j] + grid[i][j -1])
    

    return grid[-1][-1]
    


def paths_to_traverse_grid(n,m):
    path = [(0,0)]
     
    start_row = start_col = 0
    find_paths_helper(0,0,n - 1,m -1,path)


def find_paths_helper(current_row,current_col,rows,cols,path):
    if current_row == rows and current_col == cols:
        print(path)
        return

    
    for neighbor_row,neighbor_col in ((current_row + 1,current_col),(current_row,current_col + 1)):
        if neighbor_row <= rows and neighbor_col <= cols:
            path.append((neighbor_row,neighbor_col))

            find_paths_helper(neighbor_row,neighbor_col,rows,cols,path)

            path.pop()










if __name__ == "__main__":
    

    paths_to_traverse_grid(3,3)




