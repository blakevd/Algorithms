# Blake Van Dyken

import sys

def findShortestPath(n, k, art, memory):
    # check base cases
    
    #

def main():
    NINF = -float("inf")
    # get input
    input = sys.stdin.readline().split(" ")
    n, k = (int)(input[0]), (int)(input[1])

    row, col = n, 2
    art = [[NINF for i in range(row)] for j in range(col)]
    
    # read each line and make it into the gallery
    for row in range(n+1):
        first, second = sys.stdin.readline().split(" ")
        if(row != n):
            art[0][row] = first
            art[1][row] = second

    # setup 3D array for dynamic prog
    memory = [[[0 for x in range(row)] for xx in range(k)] for xxx in range(3)]
    return findShortestPath(n, k, art, memory)

sys.stdout.write((str)(main()))