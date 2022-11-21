# Blake Van Dyken
from sys import stdin, stdout
from math import sqrt

# For APSP
def FloydWarshall(graph, pos):
    dist = [[float('inf') for v in range(len(graph))] for u in range(len(graph))] # 2D array to store distances
    
    for u in graph:
        for v in graph[u]:
            dist[u][v] = sqrt( (pos[u][0] - pos[v][0])**2 + (pos[u][1] - pos[v][1])**2 )

    for r in range(len(graph)):
        for u in graph:
            for v in graph:
                tense = dist[u][r] + dist[r][v]
                #print('u to v:  ',u, r, 'dist ', dist[u][r], dist[u][r], tense)
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
    
    # add another road that is the shortest road
    min = float('inf')
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = sqrt( (pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2 )
                if dist < min:
                    if j not in graph[i] or i not in graph[j]:
                        min = dist
                        x, y = i, j
                        
    print('min',min,x,y)
    graph[x].add(y)
    graph[y].add(x)

    return graph, pos

def main():
    graph, pos = input()
    dist = FloydWarshall(graph, pos)
    
    total = 0
    
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i != j:
                total += dist[i][j]
    
    return total/2

stdout.write(str(main()))