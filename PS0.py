# Blake Van Dyken
# 8/30/22
# PS0
import sys
 
# compare sorted dict of words to figure out anagrams 
def findNonAnagrams(dict): 
    non_anagrams = 0
    # count occurnces that we stored in dictionary
    for key in dict:
        if(dict[key] == 1):
            non_anagrams += 1
            
    return non_anagrams
        

# get num words, num of letters
numWords, numLetters = sys.stdin.readline().split(" ") # get n, k
dict = dict()

# loop through input
for word in range(int(numWords)):
    # sort the word alphabetically then add it to the dict with the num of occurences
    input = "".join(sorted(sys.stdin.readline()))
    if (dict.get(input) != None):
        dict[input] = dict[input] + 1
    else:
        dict[input] = 1

sys.stdout.write(str(findNonAnagrams(dict))) # print # of non anagrams