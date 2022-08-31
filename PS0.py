# Blake Van Dyken
# 8/30/22
# PS0
import sys
 
# compare sorted list of words to figure out anagrams 
def findNonAnagrams(words, numWords): 
    anagrams = []
    for word in range(numWords): # loop through list
        for otherWord in range(word+1, numWords): # loop word against other words
            if (words[word] == words[otherWord]): # check if next item is anagram
                # add to list of anagrams if it is not in it
                if(not word in anagrams):
                    anagrams.append(word)
                if(not otherWord in anagrams):
                    anagrams.append(otherWord)

    return numWords - len(anagrams) # return total non anagrams

# get n, k
numWords, numLetters = sys.stdin.readline().split(" ") # get n, k
words = []

# loop through input
for word in range(int(numWords)):
    # sort the word alphabetically then add it to the list
    words.append("".join(sorted(sys.stdin.readline()))) # get word from stdin

sys.stdout.write(str(findNonAnagrams(words, int(numWords)))) # print # of non anagrams