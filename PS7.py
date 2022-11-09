# Blake Van Dyken
import sys
sys.setrecursionlimit(10000)
import math

# helper expression to get dist between two vertices
distance = lambda v1, v2 : math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)

# gets all the edges in the given graph
def get_edges(graph):
    # (u, v, dist), ...
    edges = []
    for u in graph:
        for v in graph[u]:
            if u < v[0]: # don't waste time on other half of graph since it is undirected
                edges.append((u, v[0], v[1]))
                
    return edges

# gets all safe edges in graph
def get_safe_edges(graph, comps):
    total_comps = max(comps.values()) + 1
    
    # maintain a list of each comps of the best edge we find
    # (u, v, distance), ...
    best_edge = [(None, None, sys.maxsize) for _ in range(total_comps)]

    # loop through all edges
    for u, v, dist in get_edges(graph):
        if comps[u] == comps[v]: continue # this edge is useless in same comp
        
        if dist < best_edge[comps[u]][2]:
            best_edge[comps[u]] = (u, v, dist)
        
        if dist < best_edge[comps[v]][2]:
            best_edge[comps[v]] = (u, v, dist)
       
    return best_edge
       
# returns a dict of components in graph => (x, y) : component #
def find_components(graph):
    comp = dict()
    count = -1
    
    for u in graph: # empty comp 
        comp[u] = None
    
    def dfs(u):
        if comp[u] == None:
            comp[u] = count
            for v in graph[u]:
                dfs(v[0]) # get (x, y) ignore dist
    
    for u in graph:
        if comp[u] == None:
            count += 1
            dfs(u)
    
    return comp

# boruvkas method for MST
def boruvka(graph):
    n = len(graph)
    rope = 0
    # F = ((x,y) : (x, y), dist), ...)
    F = dict()
    for u in graph:
        add_edge(F, u, set())

    # stop looping when F is a tree
    while len(get_edges(F)) < (n - 1) / 2:
        comps = find_components(F)
        safe = get_safe_edges(graph, comps)
        
        # add our safe edges to F
        for u, v, dist in safe:
            add_edge(F, u, (v, dist))
        
    return F

# adds vertex to graph
# dict and set do not allow duplicates
def add_edge(graph, k, v):
    if (v == set()):
        graph[k] = set()
    else:
        try:  
            graph[k].add(v)
        except KeyError:
            graph[k] = {v}

# takes in input and returns a graph based on requirements for assignment
# coords/pos is unique
# graph = (pos=(x, y)) : (pos=(x, y), dist)
def input():
    # read first line of input
    n, e, p = list(map(int, sys.stdin.readline().split(' ')))
    
    graph = dict() # create empty graph
    vertices = [] # keep track of ith vertice pos 
    ignore = [] # edges to have 0 weight stored as ((x, y), (x2,y2))
    
    # set up graph from vertice inputs
    for i in range(n):
        x, y = list(map(float, sys.stdin.readline().split(' ')))
        key = ((x, y))
        vertices.append(key)
    
    # get p input and add edges to graph
    for i in range(p):
        a, b = list(map(int, sys.stdin.readline().split(' ')))
        
        # correct the indexing to start at 0
        u = vertices[a-1]
        v = vertices[b-1]
        ignore.append((u, v))
        
    # connect the first e values given in input
    if e > 1: # ignore base case, it will become its own single component anyway
        walkable = []
        for i in range(e):
            walkable.append(vertices[i]) # add in order of input given
        # connect them to eachother, does not matter how they connect they all have weight 0
        for i in range(len(walkable) - 1):
            u = walkable[i]
            v = walkable[i+1] # 0 distance
            
            ignore.append((u, v))
    
    # connect all vertices to eachother
    # only add distances that are short to graph to make it faster
    for u in vertices:
        for v  in vertices:
            if u < v: # only go through half its undirected
                if (u, v) in ignore: # give them 0 weight
                    add_edge(graph, u, (v, 0))
                    add_edge(graph, v, (u, 0))
                else:
                    dist = distance(u, v)
                    add_edge(graph, u, (v, dist))
                    add_edge(graph, v, (u, dist))
           
    return graph

# human readable graph
def print_graph(G):
    sum = 0
    for u in G:
        for v in G[u]:
            print(u, ' connects to ', v[0], ' with w=', v[1])
            sum += len(G[u])
    print(sum)      
    

def main():
    G = input()
    MST = boruvka(G)
    rope = 0
    

    return MST

sys.stdout.write((str)(main()))