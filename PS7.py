# Blake Van Dyken
import sys
sys.setrecursionlimit(10000)
import math

distance = lambda v1, v2 : math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)

# helper to print out graph
def print_graph(G):
    edges = get_edges(G)
    print(sum(dist for _,_,dist in edges))
    for u, v, dist in sorted(edges):
        print(u, v)

# gets all the edges in the given graph
def get_edges(G):
    edges = []
    for u in range(len(G)):
        for v, dist in G[u]:
            if u < v: # don't waste time on other half of graph since it is undirected
                edges.append((u, v, dist))
                
    return edges

# gets all safe edges in graph
def get_safe_edges(G, comps):
    total_comps = max(comps) + 1
    
    # maintain a list of each comps of the best edge we find
    #(u, v, distance)
    best_edge = [(-1, -1, sys.maxsize) for _ in range(total_comps)]
    
    # loop through all edges
    for u, v, dist in get_edges(G):
        if comps[u] == comps[v]: continue # this edge is useless
        
        if dist < best_edge[u][2]:
            best_edge[comps[u]] = (u, v, dist)
        
        if dist < best_edge[v][2]:
            best_edge[comps[v]] = (u, v, dist)
       
    return best_edge

# returns a list of components in G
def find_components(G):
    comp = [None for _ in G]
    count = -1
    
    def dfs(u):
        if comp[u] == None:
            comp[u] = count
            for v, _ in G[u]:
                dfs(v)
    
    for u in range(len(G)):
        if comp[u] == None:
            count += 1
            dfs(u)         
    return comp

# add safe edge to a graph
def add_safe_edges(F, safe):
    for u, v, dist in safe:
        if not (v, dist) in F[u]:
            F[u].append((v, dist))
        if not (u, dist) in F[v]:
            F[v].append((u, dist))

def boruvka(G):
    n = len(G)
    
    # F is non wieghted 
    # F = ((V_index, x, y), ...)
    F = [[] for _ in range(n)]
    
    # stop looping when F is a tree
    while get_edges(F) < n - 1:
        comps = find_components(F)
        
        safe = get_safe_edges(G, comps)
        
        add_safe_edges(F, safe)
        
    return F

# takes in input and returns a graph based on requirements for assignment
def input():
    

def main():
    v1 = (1, 2)
    v2 = (0 ,0)
    return distance(v1, v2)

sys.stdout.write((str)(main()))