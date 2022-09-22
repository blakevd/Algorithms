# Blake Van Dyken
import sys

NINF = -float("inf")

def climb(totalHeight, n, memory, distances):
    if (n <= 1):
        return 100000
    elif(n == 2):
        if (distances[0] == distances[1]):
            return distances[0]
        return 100000
    
    for i in range(n): # loop through rows
        for h in range(totalHeight + 1): # loop through column
            if(i == 0): # fill first column appropriately
                if (h == 0):
                    memory[0][0] = 0
            elif(i == n-1): # we are in last column
                result = memory[n-1][distances[n-1]]
                if (result != NINF): # i = n - 1 is not INF
                    return result
            else: # fill in between columns
                nextDist = distances[i-1] # next distance we need to go up and down
                
                # set values to where they are in mem unless they are out of bounds
                up, down = NINF, NINF # takes care of out of bounds case
                if(h + nextDist <= totalHeight):
                    up = (memory[i - 1][h + nextDist])
                if(h - nextDist >= 0):
                    down = (memory[i - 1][h - nextDist])
                
                if (down is not NINF and up is not NINF): # neither INF
                    memory[i][h] = min(down, up)
                elif(down is not NINF and up is NINF): # up is INF
                    memory[i][h] = h
                elif(down is NINF and up is not NINF): # down is inf
                    memory[i][h] = up

    return 100000 # it is impossible


def main():
    n = (int)(sys.stdin.readline()) # get size of dist input
    distances = list(map(int, sys.stdin.readline().split(" "))) # get dist
    totalHeight = sum(distances)

    # create 2D array for memoization/dynamic programming
    memory = [ [NINF]*(totalHeight+1) ]*n
    
    return climb(totalHeight, n, memory, distances)

sys.stdout.write((str)(main()))