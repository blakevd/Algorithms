# Blake Van Dyken
from sys import stdin, stdout, maxsize
from itertools import permutations

def input():
    n = int(stdin.readline()) # @ ,= n <= 25
    # create adj matrix
    graph = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        line = list(map(int, stdin.readline().split(' ')))
        for j in range(len(line)):
            graph[i][j] = (line[j])

    return graph

# lol made by the AI kinda cool
def traverse(graph):
    n = len(graph)
    perm = list(permutations(range(n))) # all possible combinations
    
    min = maxsize
    
    for p in perm:
        dist = 0
        for i in range(n):
            vertex = (i + 1) % n
            dist += graph[p[i]][p[vertex]]
            
        if dist < min:
            min = dist
            
    return min

def main():
    g = input()
    return traverse(g)

stdout.write(str(main()))