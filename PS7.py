# Blake Van Dyken
from sys import stdin, stdout, maxsize
from math import sqrt

# gets all the edges in the given graph
def get_edges(graph):
    # (u, v, dist), ...
    return [(u, v[0], v[1]) for u in graph for v in graph[u] if u < v[0]]

# gets all safe edges in graph
def get_safe_edges(graph, comps, total_comps):
    # get safe edges
    best_edge = [(-1, -1, maxsize) for _ in range(total_comps)]
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
            
    return comp, count + 1

# boruvkas method for MST
def boruvka(graph):
    n = len(graph)
    # F = ((x,y) : (x, y), dist), ...)
    F = dict()
    for u in graph:
        add_edge(F, u, set())
        
    # stop looping when F is a tree
    while len(get_edges(F)) < (n - 1):
        comps, max_comps = find_components(F)
        # maintain a list of each comps of the best edge we find
        # (u, v, distance), ...
        safe = get_safe_edges(graph, comps, max_comps)
        
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
def read_input():
    # read first line of input
    n, e, p = stdin.readline().split(' ')
    graph = dict() # create empty graph
    
    # set up graph from vertice inputs
    for _ in range(int(n)):
        x, y = stdin.readline().split(' ')
        add_edge(graph, (float(x), float(y)), set())
    
    d = list(graph.keys())
    # get p input and add edges to graph
    for i in range(int(p)):
        a, b = stdin.readline().split(' ')
        add_edge(graph, d[int(a)-1], (d[int(b)-1], 0))
        add_edge(graph, d[int(b)-1], (d[int(a)-1], 0))
  
    # connect the first e values given in input
    if int(e) > 1: # ignore base case, it will become its own single component anyway
        for i in range(int(e)-1):
            dist = 0
            add_edge(graph, d[i], (d[i+1], dist))
            add_edge(graph, d[i+1], (d[i], dist))
    
    for u in graph:
        for v in graph:
            if u < v:
                dist = sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
                add_edge(graph, u, (v, dist))
                add_edge(graph, v, (u, dist))
       
    return graph

def main():
    G = read_input() 
    MST = boruvka(G)
    rope = 0
    
    for s in MST.values():
        if s != set():
            for edge in s:
                rope += edge[1]
    return str(rope/2)

stdout.write(main())