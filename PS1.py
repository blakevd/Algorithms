# Blake Van Dyken
# 8/30/22
# PS1

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
    result = []
    
    for i in (array/5):
        mof = (array[5*i-4] + array[5*i-3] + array[5*i-2] + array[5*i-2] + array[5*i-1])/5
        result.append(mof)
    
    # put all extra values into an array of 5 
    extra = len(array) % 5
    if (extra != 0):
        result.append(0) # add inf to median
        
    return result

# finds kth biggest thing in array
# mom select
def mom_select(array, k):
    # base cases
    if (len(array) <= 25):
        print('poo')
    #elif () # if all medians are the same
    
    else:
        median_of_five = len(array) / 5
        median_of_five_list = []
        for i in m:
            median_of_five_list.append()
        # find pivot using mom
        pivot = 1
        
        # partition based on pivot
        new_pivot = partition(array, pivot)
        
        # recurse into either less or greater based on value at pivot
        if (k < )
    
def test():
    small = [3, 1, 2, 0]
    big = [5, 12, 7, 19, 100, 45, 63]
    
    print('testing partition')
    print(partition(small, 1))
    print(partition(big, 3))
    
    print('testing median of five')
    
    
test()