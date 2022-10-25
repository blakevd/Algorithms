import sys
sys.setrecursionlimit(1500) # make more room on stack for recursion

def input():
    firstLine = (sys.stdin.readline().split(" "))
    width, height = (int)(firstLine[0]), (int)(firstLine[1])
    map = [[-1 for i in range(width)] for j in range(height-2)] # height-2 to ignore lines
    
    # create 2D array from our input
    ignoreFirstLine = sys.stdin.readline()
    for h in range(height-2): # this ignores last line and frist one
        line = sys.stdin.readline()
        for w in range(width):
            map[h][w] = line[w]
    # we ignore last  line here
    ignoreLastLine = sys.stdin.readline()
    
    return map, width, height-2

# try adding new thing to the set in the graph
def updateGraphPair(graph, key, value):
    v = Vertex(value)
    try:
        graph[key].add(v)
    except KeyError:
        graph[key] = {v}
        

# create graph from 2D array
def createGraph(map, width, height):
    graph = dict()
    
    for h in range(height):
        for w in range(width):
            if map[h][w] != '#' and map[h][w] != 'T': # not a wall or a trap
                # check below char technically h+1 goes down in 2d array
                if h+1 < height:
                    updateGraphPair(graph, map[h][w], map[h+1][w])
                # check below char
                if h-1 >= 0:
                    updateGraphPair(graph, map[h][w], map[h-1][w])
                # check right side of char
                if w+1 < width:
                    updateGraphPair(graph, map[h][w], map[h][w+1])
                # check left side of char
                if w-1 >= 0:
                    updateGraphPair(graph, map[h][w], map[h][w+1])
                    
                
    return graph
                
            

def main():
    # get input
    map, width, height = input()
    graph = createGraph(map, width, height)
    
    return graph

sys.stdout.write((str)(main()))