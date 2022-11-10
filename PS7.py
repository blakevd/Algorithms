# Blake Van Dyken
import sys
from math import sqrt
#import cProfile

# gets all the edges in the given graph
def get_edges(graph):
    # (u, v, dist), ...
    edges = []
    for u in graph:
        for v, dist in graph[u]:
             if u < v: # don't waste time on other half of graph since it is undirected
                edges.append((u, v, dist))
                
    return edges

# gets all safe edges in graph
def get_safe_edges(graph, comps):
    total_comps = max(comps.values()) + 1
    # maintain a list of each comps of the best edge we find
    # (u, v, distance), ...
    best_edge = [(-1, -1, sys.maxsize) for _ in range(total_comps)]
    
    # loop through all edges
    for u, v, dist in get_edges(graph):
        Cu = comps[u]
        Cv = comps[v]
        
        if Cu == Cv: continue # this edge is useless in same comp
        
        if dist < best_edge[Cu][2]:
            best_edge[Cu] = (u, v, dist)
        
        if dist < best_edge[Cv][2]:
            best_edge[Cv] = (u, v, dist)
       
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
    # F = ((x,y) : (x, y), dist), ...)
    F = dict()
    for u in graph:
        add_edge(F, u, set())

    # stop looping when F is a tree
    while len(get_edges(F)) < (n - 1):
        comps = find_components(F)
        safe = get_safe_edges(graph, comps)
        # add our safe edges to F
        for u, v, dist in safe:
            if u < v:
                if not (v, dist) in F[u]:
                    add_edge(F, u, (v, dist))
                if not (u, dist) in F[v]:
                    add_edge(F, v, (u, dist))

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
    n, e, p = sys.stdin.readline().split(' ')
    graph = dict() # create empty graph
    vertices = [] # keep track of ith vertice pos 
    ignore = [] # edges to have 0 weight stored as ((x, y), (x2,y2))
    
    # set up graph from vertice inputs
    for i in range(int(n)):
        x, y = sys.stdin.readline().split(' ')
        vertices.append((float(x), float(y)))
    
    # get p input and add edges to graph
    for i in range(int(p)):
        a, b = sys.stdin.readline().split(' ') 
        # correct the indexing to start at 0
        ignore.append((vertices[int(a)-1], vertices[int(b)-1]))
  
    # connect the first e values given in input
    if int(e) > 1: # ignore base case, it will become its own single component anyway
        for i in range(int(e)-1):
            ignore.append((vertices[i], vertices[i+1]))

    # only add distances that are short to graph to make it faster
    # create a connected graph by connecting all to first vertice
    for u in vertices:
        for v in vertices:
            if u < v:
                if (u, v) in ignore or (v, u) in ignore:
                    add_edge(graph, u, (v, 0))
                    add_edge(graph, v, (u, 0))
                else:
                    dist = sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
                    add_edge(graph, u, (v, dist))
                    add_edge(graph, v, (u, dist))
           
    return graph

def main():
    G = input() 
    MST = boruvka(G)
    rope = 0
    
    for s in MST.values():
        if s != set():
            for edge in s:
                rope += edge[1]

    return str(rope/2)

#cProfile.run('main()')
sys.stdout.write(main())