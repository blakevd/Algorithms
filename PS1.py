# Blake Van Dyken
# 8/30/22
# PS1

from statistics import median
import sys

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
def medianOfFive(array, array_of_indexes):  
    lista, listi = zip(*sorted(zip(array, array_of_indexes)))
    return listi[2]  # return 3rd index of our sorted couple

# finds kth biggest thing in array
# mom select
def mom_select(array, k):
    # base cases
    if (len(array) <= 25): # brute force      
        lst = array
        lst.sort()
        return lst[(int)(len(lst)/2)]
    else:
        m = (int)(len(array) / 5) - 1
        median_of_five_list = []
        
        for i in range(m+1):
            i=i+1
            indexes = [5*i-5, 5*i-4, 5*i-3, 5*i-2, 5*i-1]
            five_array = array[ ((5*i) - 5) : (5*i)]
            median_of_five_list.append(medianOfFive(five_array, indexes))
        
        # find pivot using mof
        mom_pivot = mom_select(median_of_five_list[:m], m/2)
        
        # partition based on pivot
        arr, r = partition(array, mom_pivot)
        
        # recurse into either less or greater based on value at pivot
        if (k < r):
            return mom_select(array[:r-1], k)
        elif (k > r):
            return mom_select(array[r+1:], k-r)

        return mom_pivot # maybe not -1


def test2():
    input_participants = sys.stdin.readline()
    input_ids = sys.stdin.readline()
    input_skills = sys.stdin.readline()
    
    # take in input
    ids = list(map(int, input_ids.split(" ")))
    skills = list(map(int, input_skills.split(" ")))
    
    orig_ids = ids.copy()
    orig_skills = skills.copy()
    
    # check if all medians are the same
    arr, piv = partition(skills, 1)
    if(len(arr) == 1):
        ids.sort()
        return median(ids)
    else:
        piv = mom_select(skills, len(ids)/2)
        arr, val = partition(skills, piv)
        
        i = arr.index(val)
        L = 0
        for x in arr[:i]:
            L += x
        R = 0
        
        for y in arr[i+1:]:
            R += y

        if (R > L):
            return orig_ids[orig_skills.index(mom_select(arr[i+1:], 1))]
        else:
            return orig_ids[orig_skills.index(mom_select(arr[:i], 1))]

def main():
    # working?
    input_participants = sys.stdin.readline()
    input_ids = sys.stdin.readline()
    input_skills = sys.stdin.readline()
    
    # take in input
    ids = list(map(int, input_ids.split(" ")))
    skills = list(map(int, input_skills.split(" ")))
    
    # sort ids to skills
    sorted_ids, sorted_skills = zip(*sorted(zip(ids, skills)))
    
    w = sum(sorted_skills)/2
    for n in range(len(sorted_skills)-1):
        rsum = 0
        if (sorted_skills[n] != len(sorted_skills)-1):
            for r in sorted_skills[sorted_ids[n]:]:
                rsum += r
        
        lsum = 0     
        if (sorted_skills[n] != 0):  
            for l in sorted_skills[:sorted_ids[n]-1]:
                lsum += l
        
        if (lsum <= w and rsum <= w):
            return sorted_ids[n]
    
    return sorted_ids[0]
            
print(main())