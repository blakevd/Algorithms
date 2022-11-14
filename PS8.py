from sys import stdin, stdout
from queue import PriorityQueue

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

def initSSSP(graph, size):
    dist = [float('inf') for _ in range(size)]
    pred = [None for _ in range(size)]

    dist[0] = 0
    return dist, pred


# change all edge weights to be negative and then we will find longest path
# follows non negative dijkstras structure
def dijkstra(graph, size, start, end):
    q = PriorityQueue()
    dist, pred = initSSSP(graph, size)
    print('init dist = ', dist)
    # load priority queue
    for v in graph:
        q.put( (v, dist[v]) )

    while not q.empty():
        next = q.get() # get next min item in pq
        u = next[0]
        print('dist = ', next)
        for edge in graph[u]:
                v = edge[0]
                uv_dist = edge[1]
                if pred[v] != u:
                    # tense => dist(u) + w(u->v) < dist(v)
                    tense = dist[u] + uv_dist
                    print('u:',dist[u], 'v:',uv_dist)
                    if dist[v] > tense: # if it is tense
                        dist[v] = tense # relax it
                        pred[v] = u
                        q.put( (v, dist[v]) )
    
    return dist

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
        weight = float(f) # make weight negative for dijktras longest path
        # add undirected edge to adjacency list
        add_edge(graph, key, (value, weight))
        add_edge(graph, value, (key, weight))

    return graph, int(m), int(n)

def main():
    G, m, n = input()
    dist = dijkstra(G, m, 0, n-1)

    return dist

stdout.write(str(main()))