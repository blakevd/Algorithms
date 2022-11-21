# Blake Van Dyken
from sys import stdin, stdout
from math import sqrt

# no duplicate roads or intersections
def input():
    # vertices
    n = int(stdin.readline())
    graph = [[float('inf') for col in range(n)] for row in range(n)] # 2D array for storage of position VxV
    pos = []
    for i in range(n):
        x, y = stdin.readline().split(' ')
        x = int(x)
        y = int(y)
        
        pos.append((x, y)) # store unique coords in list
    
    # connections/edges
    m = int(stdin.readline())
    for i in range(m):
        a, b = stdin.readline().split(' ')
        a = int(a)
        b = int(b)
        
        # append distance to 2D array
        dist = sqrt( (pos[b][0] - pos[a][0])**2 + (pos[b][1] - pos[a][1])**2 )
        graph[a][b] = (dist)
        graph[b][a] = (dist)
    
    # add another road that is the shortest
    min = float('inf')
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if i != j:
                if graph[i][j] == float('inf') or graph[i][j] == float('inf'): # not already a path we have made
                    dist = sqrt( (pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2 )
                    if dist < min:
                        min = dist
                        x, y = i, j
    
    graph[x][y] = min
    return graph

def main():
    return

print(input())
#stdout.write(str(main()))