# Blake Van Dyken
import sys
sys.setrecursionlimit(10000)
import math

# helper expression to get dist between two vertices
distance = lambda v1, v2 : math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)

# helper to print out graph
def print_graph(graph):
    edges = get_edges(graph)
    print(sum(dist for _,_,dist in edges))
    for u, v, dist in sorted(edges):
        print(u, v)

# gets all the edges in the given graph
def get_edges(graph):
    edges = []
    for u in range(len(graph)):
        for v, dist in graph[u]:
            if u < v: # don't waste time on other half of graph since it is undirected
                edges.append((u, v, dist))
                
    return edges

# add safe edge to a graph
def add_safe_edges(F, safe):
    for u, v, dist in safe:
        if not (v, dist) in F[u]:
            F[u].append((v, dist))
        if not (u, dist) in F[v]:
            F[v].append((u, dist))

# gets all safe edges in graph
def get_safe_edges(graph, comps):
    total_comps = max(comps) + 1
    
    # maintain a list of each comps of the best edge we find
    #(u, v, distance)
    best_edge = [(-1, -1, sys.maxsize) for _ in range(total_comps)]
    
    # loop through all edges
    for u, v, dist in get_edges(graph):
        if comps[u] == comps[v]: continue # this edge is useless
        
        if dist < best_edge[u][2]:
            best_edge[comps[u]] = (u, v, dist)
        
        if dist < best_edge[v][2]:
            best_edge[comps[v]] = (u, v, dist)
       
    return best_edge

# returns a list of components in graph
def find_components(graph):
    comp = [None for _ in graph]
    count = -1
    
    def dfs(u):
        if comp[u] == None:
            comp[u] = count
            for v, _ in graph[u]:
                dfs(v)
    
    for u in range(len(graph)):
        if comp[u] == None:
            count += 1
            dfs(u)
    return comp

# boruvkas method for MST
def boruvka(graph):
    n = len(graph)
    
    # F is non wieghted 
    # F = ((V_index, x, y), ...)
    F = [[] for _ in range(n)]
    
    # stop looping when F is a tree
    while get_edges(F) < n - 1:
        comps = find_components(F)
        
        safe = get_safe_edges(graph, comps)
        
        add_safe_edges(F, safe)
        
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
# graph = (ith, pos=(x, y)) : (ith, pos(x, y), dist)
def input():
    n, e, p = list(map(int, sys.stdin.readline().split(' ')))
    
    graph = dict() # create empty graph
    # get all vertice positions
    for i in range(n):
        x, y = list(map(int, sys.stdin.readline().split(' ')))
        add_edge(graph, )
    
    for i in range(p):
        v1, v2 = list(map(int, sys.stdout.readline().split(' ')))
        

def main():
    return

sys.stdout.write((str)(main()))