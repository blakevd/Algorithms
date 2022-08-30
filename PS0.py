# Blake Van Dyken
# 8/30/22
# PS0

def main():
    numWords, numLetters = input().split(" ") # get n, k
    words = []
    
    for word in range(int(numWords)):
        # sort the word alphabetically then add it to the list
        words.append("".join(sorted(input())))
        
    print(findNonAnagrams(words, int(numWords))) # print # of non anagrams
    
# compare sorted list of words to figure out anagrams 
def findNonAnagrams(words, numWords): 
    not_anagrams = 0
    
    for word in range(numWords - 1): # loop through list
        if (words[word] != words[word + 1]): # check if next item is anagram
            not_anagrams += 1       
                
    return not_anagrams
    
if __name__ == "__main__":
    main()
    