# Blake Van Dyken

import sys

def findShortestPath(n, k, art, memory):
    # check edge cases
    if(k == 0): # sum of everything
        total = 0
        for col in range(2):
            for row in range(n):
                total += art[row][col]
        return total
    elif(k == n): # either sum of left or right side
        left = 0
        right = 0
        for row in range(n):
            left += art[row][0]
            right += art[row][1]

        return max(left, right)
    # setup first values
    # art[row][col]
    # k = 0 actual, 1 = neither, ...
    # memory[r][k][blocked col] for blocked col, 0 = neither, 1 = left, 2 = right

    memory[0][0][0] = art[0][0] + art[0][1] # neither are blocked so its the sum
    memory[0][1][1] = art[0][0] # right is blocked, so it = right
    memory[0][1][2] = art[0][1] # left is blocked, so it = left
   
    # loop through array
    for row in range(n-1): # skip first element we already did
        row = row + 1
        for block in range(k+1): # make room for last k
            if(memory[row-1][block] is -float("inf")):
                continue # skip useless steps
            if(max(memory[row-1][block]) >= 0):
                memory[row][block][0] = art[row][0] + art[row][1] + max(memory[row-1][block]) # base case
                #print("either: ", art[row][0] + art[row][1] + max(memory[row-1][block]))
            if(block != 0): # max between current and the left and the right blocks
                maxOfNoneAndRight = max(memory[row-1][block-1][0], memory[row-1][block-1][1])
                memory[row][block][1] = art[row][1] + maxOfNoneAndRight

                maxOfNoneAndLeft = max(memory[row-1][block-1][0], memory[row-1][block-1][2])
                memory[row][block][2] = art[row][0] + maxOfNoneAndLeft
                #print("noR: ",maxOfNoneAndRight)
                #print("noL: ", maxOfNoneAndLeft)

    return max(memory[n-1][block]) # ans in last row      


def main():
    NINF = -float("inf")
    # get input
    input = sys.stdin.readline().split(" ")
    n, k = (int)(input[0]), (int)(input[1])

    row, col = n, 2
    art = [[NINF for i in range(col)] for j in range(row)]
    
    # read each line and make it into the gallery
    for row in range(n+1):
        first, second = sys.stdin.readline().split(" ")
        if(row != n):
            art[row][0] = (int)(first)
            art[row][1] = (int)(second)

    # setup 3D array for dynamic prog
    # k+1 so we have room for when we are out of places to block
    memory = [[[NINF for x in range(3)] for xx in range(k+1)] for xxx in range(row)]
    return findShortestPath(n, k, art, memory)

sys.stdout.write((str)(main()))