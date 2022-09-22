# Blake Van Dykenmemory[h][i]
import sys

NINF = -float("inf")

def climb(totalHeight, n, memory, distances):
    if(n == 0 or totalHeight == 0):
        return 0
    
    for i in range(n): # loop through rows
        for h in range(totalHeight): # loop through column
            if(i == 0): # fill first column appropriately
                if (h == 0):
                    memory[h][i] = 0
            else: # fill in between columns and last col
                nextDist = distances[i-1] # next distance we need to go up and down

                # set values to where they are in mem unless they are out of bounds
                if(h - nextDist >= 0): # will ignore out of bounds case
                    down = memory[h - nextDist][i - 1]
                    if(down is not NINF): # ignore if it is inf
                        if(down >= h):
                            memory[h][i] = down
                            #print("1chose: ",down,"over: ",h)
                        else:
                            memory[h][i] = h
                            #print("2chose: ",h,"over: ",down)
                    
                if(h + nextDist <= totalHeight):
                    up = memory[h + nextDist][i - 1]
                    if(up is not NINF):
                        if(memory[h][i] is not NINF):
                            #print("4chose: ",min(up, memory[h][i]),"over: ",max(up, memory[h][i]))
                            memory[h][i] = min(up, memory[h][i]) # choose min between itsekf and down 
                        else:
                            #print("4chose: ",up,"over: ",memory[h][i])
                            memory[h][i] = max(h, up)

            if(i == n-1 and memory[h][i] is not NINF):
                result = memory[h][i]
                if (result != NINF and h - distances[i] == 0): # i = n - 1 is not INF
                    return result
    
    return 100000 # it is impossible


def main():
    n = (int)(sys.stdin.readline()) # get size of dist input
    distances = list(map(int, sys.stdin.readline().split(" "))) # get dist
    totalHeight = sum(distances)

    # create 2D array for memoization/dynamic programming
    col, row = n, totalHeight+1
    memory = [[NINF for i in range(col)] for j in range(row)]
    
    return climb(totalHeight, n, memory, distances)

sys.stdout.write((str)(main()))