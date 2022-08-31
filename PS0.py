# Blake Van Dyken
# 8/30/22
# PS0
import sys
 
# compare sorted list of words to figure out anagrams 
def findNonAnagrams(words, numWords): 
    anagrams = 0
    for word in range(numWords - 1): # loop through list
        for otherWord in range(word+1, numWords): # loop word against other words
            if (words[word] == words[otherWord]): # check if next item is anagram
                anagrams += 1

    # multiply anagrams by 2 because each anagram is a pair
    return numWords - (anagrams*2) # return total non anagrams

# get n, k
numWords, numLetters = sys.stdin.readline().split(" ") # get n, k
words = []

# loop through input
for word in range(int(numWords)):
    # sort the word alphabetically then add it to the list
    words.append("".join(sorted(sys.stdin.readline()))) # get word from stdin

sys.stdout.write(str(findNonAnagrams(words, int(numWords)))) # print # of non anagrams