# Blake Van Dyken
# 8/30/22
# PS1

import numpy as np

def partition(array, pivot_i):
    lesser = []
    greater = []
    pivot = array[pivot_i]
    
    for i in array:
        if (i < pivot):
            lesser.append(i)
        elif (i > pivot):
            greater.append(i)
        
    new_array = lesser + [pivot] + greater
    return new_array, len(lesser) # len of lesser array is where pivot is

# pass in array and find medians for an array with 5 elements
def medianOfFive(array):  
    array.sort() # sort 5 items for fast way to solve it
    return array[2] # return 3thd item or second index is our middle element

# finds kth biggest thing in array
# mom select
def mom_select(array, k):
    # base cases
    if (len(array) <= 25):
        array.sort()
        return array[(int)(len(array)/2)]
    #elif () # if all medians are the same
    else:
        m = (int)(len(array) / 5)
        median_of_five_list = []
        for i in range(m):
            median_of_five_list.append(medianOfFive(array[ (i+1 * 5 - 5) : (i+1 * 5) ]))
            
        # find pivot using mof
        mom_pivot = mom_select(array[:m], m/2)
        
        # partition based on pivot
        arr, r = partition(array, mom_pivot)
        
        # recurse into either less or greater based on value at pivot
        if (k < r):
            return mom_select(array[0:r-1], k)
        elif (k > r):
            return mom_select(array[r+1:], k-r)

        return mom_pivot
    
def test():
    small = [3, 1, 2, 0]
    big = [5, 12, 7, 19, 100, 45, 63]
    five = [1, 2, 3, 4, 5]
    bigger = [16,48,13,24,39,24,39,35,40,48,17,48,41,11,32,21,19,19,9,10,41,30,12,18,38,45,36,24,26,42] #np.random.randint(50, size=30)
    
    print('testing partition')
    print(partition(small, 1))
    print(partition(big, 3))
    
    print('testing median of five')
    print(medianOfFive(five))
    
    print('mom select')
    print(mom_select(bigger, 1))
    
test()