# Blake Van Dyken
# 8/30/22
# PS0
import sys
 
# compare sorted list of words to figure out anagrams 
def findNonAnagrams(words, numWords): 
    not_anagrams = 0
    
    for word in range(numWords - 1): # loop through list
        for otherWord in range(word, numWords - 1): # loop word against other words
            if (words[word] != words[otherWord]): # check if next item is anagram
                not_anagrams += 1    

    return not_anagrams

# get n, k
numWords, numLetters = sys.stdin.readline().split(" ") # get n, k
words = []

for word in range(int(numWords)):
    # sort the word alphabetically then add it to the list
    words.append("".join(sorted(sys.stdin.readline()))) # get word from stdin
print(words)
sys.stdout.write(str(findNonAnagrams(words, int(numWords)))) # print # of non anagrams
