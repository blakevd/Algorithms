# Blake Van Dyken
# 8/30/22
# PS0
import sys
 
# compare sorted list of words to figure out anagrams 
def findNonAnagrams(list, numWords): 
    non_anagrams = 0
    for n in list:
        if(list[n] == 1):
            non_anagrams += 1
            
    return non_anagrams
        

# get n, k
numWords, numLetters = sys.stdin.readline().split(" ") # get n, k
list = dict()

# loop through input
for word in range(int(numWords)):
    # sort the word alphabetically then add it to the list
    w = "".join(sorted(sys.stdin.readline()))
    if (list.get(w) != None):
        list[w] = list[w] + 1
    else:
        list[w] = 1

sys.stdout.write(str(findNonAnagrams(list, int(numWords)))) # print # of non anagrams