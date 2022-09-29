# Blake Van Dyken

import sys

def main():
    NINF = -float("inf")
    # get input
    input = sys.stdin.readline().split(" ")
    n, k = (int)(input[0]), (int)(input[1])

    row, col = 2, n
    art = [[NINF for i in range(col)] for j in range(row)]

    for row in range(n+1):
        first, second = sys.stdin.readline().split(" ")
        if(row != n):
            art[0][row] = first
            art[1][row] = second

    return art

sys.stdout.write((str)(main()))