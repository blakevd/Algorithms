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

# change all edge weights to be negative and then we will find longest path
# follows non negative dijkstras structure
def dijkstra(graph, start):
    q = PriorityQueue()
    # initSSSP
    dist = []
    # load priority queue
    for v in graph:
        dist.append(-float('inf'))
        q.put( (v, dist[v]) )

    while q.qsize() != 0:
        # get next minheap item in pq
        next = q.get()
        u, u_dist = next[0], next[1] 
        
        for v, uv_dist in graph[u]:
            if v != u: # check not going back to predecessor
                # tense => dist(u) + w(u->v) < dist(v) 
                tense = u_dist * uv_dist       
                if u == start: # we are at first edge so don't multiply by 0
                    tense = uv_dist
                if tense > dist[v]: # check if tense
                    dist[v] = tense # relax
                    # decrease key
                    q.put( (v, dist[v]) )
    
    return dist

# take input and store as graph as defined in problem
def input():
    n, m = stdin.readline().split(' ')
    graph = dict()

    for i in range( int(n) ):
        add_edge(graph, i, set())
    
    for _ in range( int(m) ):
        # 2<=x<=10000
        # 1<=y<=15000
        x, y, f = stdin.readline().split(' ')
        
        # make weight negative for dijktras longest path
        key = int(x)
        value = int(y)
        weight = float(f) # 0 <= f <= 1
        
        # add undirected edge to adjacency list
        add_edge(graph, key, (value, weight))
        add_edge(graph, value, (key, weight))

    return graph, int(n), int(m)

def main():
    G, n, m = input()
    dist = dijkstra(G, 0)
    stdout.write(str(dist[-1]))

main()