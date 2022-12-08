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

def traverse(graph):
    min = maxsize
    # loop through all possible graphs
    n = len(graph)
    for i in range(n):
        for j in range(permutations(n-i)):
            print(i, 'j: ', j)


def main():
    g = input()
    return None

stdout.write(str(main()))