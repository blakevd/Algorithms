# Blake Van Dyken

from math import sqrt
import sys

def input():
    # get input for problem
    sizes = list(map(int, sys.stdin.readline().split(" ")))
    N = list(map(int, sys.stdin.readline().split(" ")))
    M = list(map(int, sys.stdin.readline().split(" ")))
    K = list(map(int, sys.stdin.readline().split(" ")))
    
    return sizes, N, M, K

def main():
    sizes, plots, circleHouses, squareHouses = input()
    
    # combine M and K
    houses = circleHouses
    for v in squareHouses:
        houses.append(v/sqrt(2))
    
    # sort plots and houses to be in order
    houses.sort(reverse=True) # sort from largest to smallest
    plots.sort() # sort smallest to largest

    # greedy
    # go through largest hosue and smallest plot and fill
    filled = []

    for p in range(len(plots)):
        for h in range(len(houses)):
            if(houses[h] < plots[p] and houses[h] not in filled):
                filled.append(houses[h])
                break
        
    return len(filled)

sys.stdout.write((str)(main()))