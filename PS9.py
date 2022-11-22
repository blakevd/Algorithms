# Blake Van Dyken
from sys import stdin, stdout
from math import sqrt

# For APSP
def FloydWarshall(graph, pos):
    dist = [[float('inf') for v in range(len(graph))] for u in range(len(graph))] # 2D array to store distances
    total = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = sqrt( (pos[u][0] - pos[v][0])**2 + (pos[u][1] - pos[v][1])**2 )

    for r in range(len(graph)):
        for u in graph:
            for v in graph:
                tense = dist[u][r] + dist[r][v]
                if dist[u][v] > tense:
                    dist[u][v] = tense
                    total += tense
                    
    return total

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
    
    # make list of roads that are not in graph
    extra = [] # list of edges we will try adding
    for i in range(n):
        for j in range(n):
            if i < j:
                if i not in graph[j]: # check that its ont in graph
                   extra.append((i, j))

    return graph, pos, extra

def main():
    graph, pos, extra = input()
   
    # if we have no extra edges to try in the graph
    if len(extra) == 0:
        dist = FloydWarshall(graph, pos)
        total = 0
        for i in range(len(dist)):
            for j in range(len(dist)):
                if i < j:
                   # print(i, j, dist[i][j])
                    total += dist[i][j]

        return total
    # otherwise try adding extra intersection and find APSP
    min = float('inf')
    for u, v in extra:
        graph[u].add(v)
        graph[v].add(u)

        dist = FloydWarshall(graph, pos)
        total = 0
        for i in range(len(dist)):
            for j in range(len(dist)):
                if i < j:
                   # print(i, j, dist[i][j])
                    total += dist[i][j]
                    if total > min:
                        break
            if total > min:
                break
        if total < min:
            min = total
        graph[u].remove(v)
        graph[v].remove(u)

    return min

def main2():
    graph, pos, extra = input()
    min = float('inf')

    if len(extra) == 0:
        return FloydWarshall(graph, pos)

    for u, v in extra:
        graph[u].add(v)
        graph[v].add(u)

        total = FloydWarshall(graph, pos)
        if total < min:
            min = total
        graph[u].remove(v)
        graph[v].remove(u)

    return min

stdout.write(str(main2()))