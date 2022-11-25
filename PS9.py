# Blake Van Dyken
from sys import stdin, stdout
from math import sqrt

# For APSP
def FloydWarshall(graph, pos, min):
    dist = [[float('inf') for v in range(len(graph))] for u in range(len(graph))] # 2D array to store distances

    for u in graph:
        for v in graph[u]:
            dist[u][v] = sqrt( (pos[u][0] - pos[v][0])**2 + (pos[u][1] - pos[v][1])**2 )

    for r in range(len(graph)):
        for u in graph:
            for v in graph:
                tense = dist[u][r] + dist[r][v]
                if dist[u][v] > tense:
                    dist[u][v] = tense
                    
    return dist

# no duplicate roads or intersections
def input():
    # vertices
    n = int(stdin.readline())
    graph = dict() # adjacency list
    pos = [] # list of pos ([vertex] = pos = (x, y))
    
    for i in range(n):
        x, y = stdin.readline().split(' ')
        x = int(x)
        y = int(y)
        
        graph[i] = set() # add empty set to graph
        pos.append((x, y)) # store unique coords in list
    
    # connections/edges
    m = int(stdin.readline())
    for i in range(m):
        a, b = stdin.readline().split(' ')
        a = int(a)
        b = int(b)
        
        # append edges to adj list
        graph[a].add(b)
        graph[b].add(a)

    return graph, pos

def commute(dist, min):
    total = 0
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i < j:
                total += dist[i][j]
                if total > min:
                    return total

    return total

def small(graph, pos):
    # otherwise try adding extra intersection and find APSP
    dist = FloydWarshall(graph, pos)
    min = commute(dist, float('inf'))
    for u in range(len(graph)):
        for v in range(len(graph)):
            # get min distance edge in u
            if u < v and u not in graph[v]:
                graph[u].add(v)
                graph[v].add(u)
                dist = FloydWarshall(graph, pos)
                total = commute(dist, min)
                if total < min:
                    min = total
                graph[u].remove(v)
                graph[v].remove(u)
    
    return min

def big(graph, pos):
    # otherwise try adding extra intersection and find APSP
    dist = FloydWarshall(graph, pos)
    min = commute(dist, float('inf'))

    dm = float('inf')
    x, y = -1, -1
    for u in range(len(graph)):
        for v in range(len(graph)):
            # get min distance edge in u
            if u < v and u not in graph[v]:
                d = sqrt( (pos[u][0] - pos[v][0])**2 + (pos[u][1] - pos[v][1])**2 )
                if d < dm:
                    dm = d
                    x, y = u, v
        # try adding smallest edge if we found one
        if dm != float('inf'):
            graph[x].add(y)
            graph[y].add(x)
            dist = FloydWarshall(graph, pos)
            total = commute(dist, min)
            if total < min:
                min = total
            graph[x].remove(y)
            graph[y].remove(x)
    
    return min

def main():
    graph, pos = input()
    if len(graph) > 65:
        return big(graph, pos)
    else:
        return small(graph, pos)

stdout.write(str(main()))