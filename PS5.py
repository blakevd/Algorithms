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
def updateGraphPair(graph, k, v):
    try:
        graph[k].add(v)
    except KeyError:
        graph[k] = {v}

# helper to check if char is not a wall
def checkValidSpace(c):
    return c != '#'

# create graph from 2D array
# remember we are ignoring/dont have start and end walls in array
def createGraph(map, width, height):
    graph = dict()
    player_pos = -1
    for h in range(height):
        for w in range(width):
            if checkValidSpace(map[h][w]): # not a wall
                # check for player pos
                if (map[h][w] == 'P'):
                    player_pos = (h,w)
                # values are tuples of the index the Vertex is in the 2d array
                # check below char technically h+1 goes down in 2d array
                if h+1 < height and checkValidSpace(map[h+1][w]):
                    updateGraphPair(graph, (h,w), (h+1,w))
                # check below char
                if h-1 >= 0 and checkValidSpace(map[h-1][w]):
                    updateGraphPair(graph, (h,w), (h-1,w))
                # check right side of char
                if w+1 < width and checkValidSpace(map[h][w+1]):
                    updateGraphPair(graph, (h,w), (h,w+1))
                # check left side of char
                if w-1 >= 0 and checkValidSpace(map[h][w-1]):
                    updateGraphPair(graph, (h,w), (h,w-1))
                  
    return graph, player_pos          

def isGold(v):
    return v == 'G'

def main():
    # get input
    map, width, height = input()
    # make graph
    graph, player_pos = createGraph(map, width, height)
    
    # whatever first search
    total_gold = 0
    bag = [player_pos] # bag of things to look through
    visited = [] # list of marked vertexes
    while len(bag) != 0:
        vertex = bag.pop()
        if vertex not in visited:
            visited.append(vertex)
            # check if we pick up gold
            if (isGold(map[vertex[0]][vertex[1]])):
                total_gold += 1
                
            # recurse into children
            for child in graph:
                bag.append(child)
    
    return total_gold

sys.stdout.write((str)(main()))