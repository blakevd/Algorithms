# Blake Van Dyken
from sys import stdin, stdout

# no duplicate roads or intersections
def input():
    graph = dict()
    locations = []
    # vertices
    n = int(stdin.readline())
    for i in range(n):
        x, y = stdin.readline().split(' ')
        x = int(x)
        y = int(y)
        
        locations[i] = (x, y)
        graph[i] = [] # store unique coord as a vertice to empty adjacency list
    
    # connections/edges
    m = int(stdin.readline())
    for i in range(m):
        a, b = stdin.readline().split(' ')
        b = int(x)
        y = int(y)
    return graph, locations

def main():
    return

print(input())
#stdout.write(str(main()))