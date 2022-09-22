# Blake Van Dykenmemory[h][i]
import sys

NINF = -float("inf")

def climb(totalHeight, n, memory, distances):
    for i in range(n): # loop through rows
        for h in range(totalHeight): # loop through column
            if(i == 0): # fill first column appropriately
                if (h == 0):
                    memory[h][i] = 0
            else: # fill in between columns and last col
                nextDist = distances[i-1] # next distance we need to go up and down
                # set values to where they are in mem unless they are out of bounds
                up, down = NINF, NINF # takes care of out of bounds case
                if(h + nextDist <= totalHeight):
                    up = memory[h + nextDist][i - 1]
                if(h - nextDist >= 0):
                    down = memory[h - nextDist][i - 1]
                
                if(down > up):
                    memory[h][i] = h
                elif(down < up and down is not NINF):
                    memory[h][i] = down
                elif(down < up and down is NINF):
                    memory[h][i] = up
                else:
                    memory[h][i] = NINF # ???

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