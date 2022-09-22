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
                
                if(h - nextDist >= 0): # going up ?
                    prev = memory[i - 1][h - nextDist]
                    curr = memory[i][h]
                    
                    if (prev is not NINF):
                        if(curr == NINF):
                            if (prev >= h):
                                curr = prev
                            else:
                                curr = h
                        else:
                            curr = min(prev, curr)
                if(h + nextDist <= totalHeight):
                    prev = memory[i - 1][h + nextDist]
                    curr = memory[i][h]
                    
                    
                    
                

    return 100000 # it is impossible


def main():
    n = (int)(sys.stdin.readline()) # get size of dist input
    distances = list(map(int, sys.stdin.readline().split(" "))) # get dist
    totalHeight = sum(distances)

    # create 2D array for memoization/dynamic programming
    # memory = [ [NINF]*(totalHeight+1) ]*n causes mem error dont use it
    memory = []
    for x in range(n):
        temp = []
        for y in range(totalHeight+1):
            temp.append(NINF)
        memory.append(temp)
        
    print(memory) 
    return climb(totalHeight, n, memory, distances)

sys.stdout.write((str)(main()))