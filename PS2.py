# Blake Van Dyken
import sys

NINF = -float("inf")

def climb(totalHeight, n, memory, distances):
    for i in range(n): # loop through rows
        for h in range(totalHeight + 1): # loop through column
            
            if(i == 0): # fill first column appropriately
                if (h == 0):
                    memory[i][h] = 0
                else: # fill with -INF
                    memory[i][h] = NINF

            elif(i == n-1): # we are in last column
                result = memory[n-1][distances[n-1]]
                if (result != NINF): # i = n - 1 is not INF
                    return result
                
            else: # fill in between columns
                nextDist = distances[i-1] # next distance we need to go up and down
                
                # set values to where they are in mem unless they are out of bounds
                up, down = NINF, NINF # takes care of out of bounds case
                if(h + nextDist <= totalHeight):
                    up = memory[i - 1][h + nextDist]
                if(h - nextDist >= 0):
                    down = memory[i - 1][h - nextDist]
                
                if(down > up):
                    memory[i][h] = h
                elif(down < up and down is not NINF):
                    memory[i][h] = down
                elif(down < up and down is NINF):
                    memory[i][h] = up
                else:
                    memory[i][h] = NINF # ???

    return 100000 # it is impossible


def main():
    n = (int)(sys.stdin.readline()) # get size of dist input
    distances = list(map(int, sys.stdin.readline().split(" "))) # get dist
    totalHeight = sum(distances)

    # create 2D array for memoization/dynamic programming
    memory = [ [0]*(totalHeight+1) ]*n
    
    return climb(totalHeight, n, memory, distances)

sys.stdout.write((str)(main()))