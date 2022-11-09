# Blake Van Dyken
import sys

# try adding new thing to the set in the graph
def addVertex(graph, k, v):
    if (v == set()):
        graph[k] = set()
    else:
        try:  
            graph[k].add(v)
        except KeyError:
            graph[k] = {v}

def input():
    # start reading input
    N, M = list(map(int, sys.stdin.readline().split(" ")))
    ingredients = list(map(int, sys.stdin.readline().split(" ")))
    
    # create empty graph
    graph = dict()
    for i in range(N): # set up vertices that point to nothing
        addVertex(graph, i, set())
    
    for i in range(M): # add edges
        line = list(map(int, sys.stdin.readline().split(" ")))
        # edge = (Vertex Index, WEIGHT)
        edge = (line[1], line[2])
        addVertex(graph, line[0], edge)
        
        
    return graph, ingredients

# DFS and append post visit
def DFS(v, graph, marked, order):
    marked[v] = True
    
    for edge in graph[v]:
        if marked[edge[0]] is False:
            DFS(edge[0], graph, marked, order)
            
    order.append(v)

# return post order of topological sort
def topSort(graph):
    marked = [False for i in range(len(graph))]
    order = []
    for v in range(len(graph)):
        if marked[v] is False:
            DFS(v, graph, marked, order)
            
    return order

def buyIngredients(ingredients, graph, order):
    result = ingredients.copy()
    for v in order: # Memoized Order
        if graph[v] != set(): # not a vertex with no edges
            for edge in graph[v]: # look through its edges
                result[v] += result[edge[0]] * edge[1]
                #print("ith = ", result[v] * edge[1])
            
    return result
            
def main():
    g, ingredients = input()
    order = topSort(g)
    bought = buyIngredients(ingredients, g, order)
    
    # convert answer to a string
    return ' '.join(map(str, bought))

sys.stdout.write((str)(main()))