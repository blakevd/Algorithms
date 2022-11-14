from sys import stdin, stdout

# adds vertex to graph
# dict and set will have no duplicates
def add_edge(graph, k, v):
    if (v == set()):
        graph[k] = set()
    else:
        try:  
            graph[k].add(v)
        except KeyError:
            graph[k] = {v}

def initSSSP(s):
    return

# change all edge weights to be negative and then we will find longest path
def dijkstra(s):
    return

# take input and store as graph as defined in problem
def input():
    n, m = stdin.readline().split(' ')
    graph = dict()

    for _ in range( int(m) ):
        # 2<=x<=10000
        # 1<=y<=15000
        x, y, f = stdin.readline().split(' ')
        key = int(x)
        value = int(y)
        # 0 <= f <= 1
        weight = -float(f) # make weight negative for dijktras longest path
        # add undirected edge to adjacency list
        add_edge(graph, key, (value, weight))
        add_edge(graph, value, (key, weight))

    return graph

def main():
    G = input()

    return str(G)

stdout.write(main())