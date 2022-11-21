# Blake Van Dyken
from sys import stdin, stdout
from math import sqrt

# no duplicate roads or intersections
def input():
    # vertices
    n = int(stdin.readline())
    graph = [[None for col in range(n)] for row in range(n)] # 2D array for storage of position VxV
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
        graph[a][b] = (sqrt( (pos[b][0] - pos[a][0])**2 + (pos[b][1] - pos[a][1])**2 ))
    return graph

def main():
    return

print(input())
#stdout.write(str(main()))