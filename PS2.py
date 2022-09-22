# Blake Van Dyken
import sys

NINF = -float("inf")

def climb(totalHeight, n, memory, distances):
    for i in range(n): # loop through rows
        for h in range(totalHeight + 1): # loop through column
            
            if(i == 0): # fill first column appropriately
                if (h == 0):
                    memory[i][h] = 0
                else: # fill with -NINF
                    memory[i][h] = NINF

            elif(i == n-1): # we are in last column

                if (memory[i][distances[i]] != NINF): # i = n - 1 is not INF
                    return i + 1
            else: # fill in between columns
                nextDist = distances[i-1] # curr distance we need to go
                val1, val2 = NINF, NINF # default to NINF

                # check if precious values are in a valid spot in array
                if (not h - nextDist >= 0 and h + nextDist <= totalHeight): # make sure we are inside memory
                    if(memory[i - 1][h + nextDist]):
                    val1 = NINF
                    val2 = h + nextDist
                elif(h - nextDist >= 0 and not h + nextDist <= totalHeight):
                    val1 = h - nextDist
                    val2 = NINF
                else:
                    val1 = h - nextDist
                    val2 = h + nextDist

                # now compare previous two values and pick the better one
                if(val1 == NINF and val2 != NINF): # val1 is a #
                    memory[i][h] = val2
                elif(val1 != NINF and val2 == NINF): # val2 is a #
                    memory[i][h] = val1
                elif(val1 != NINF and val2 != NINF): # both a #
                    memory[i][h] = min(val1, val2)
                else: # they are the same either both INF or both a #
                    memory[i][h] = val1

    return 100000 # it is impossible


def main():
    n = (int)(sys.stdin.readline()) # get size of dist input
    distances = list(map(int, sys.stdin.readline().split(" "))) # get dist
    totalHeight = sum(distances)

    # create 2D array for memoryoization/dynamic programming
    memory = [ [0]*(totalHeight+1)]*n
    
    answer = climb(totalHeight, n, memory, distances)
    print(memory)
    return 1

sys.stdout.write((str)(main()))