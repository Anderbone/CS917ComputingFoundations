
# We can detect anagrams by counting amount of each type of character - we don't care about order
# Can then use a map to look them up

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def countLetters(word):
    frequency = {}

    for i in range(0,len(word)):
        count = frequency.get(word[i].lower())

        if(count is not None):
            frequency[word[i].lower()] = count + 1
        else:
            frequency[word[i].lower()] = 1
    return frequency

def buildKey(freqDict):
    tupleString = ""
    for i in letters:
        result = freqDict.get(i)
        if(result is not None):
            tupleString = tupleString + "," + str(result)
        else:
            tupleString = tupleString + ",0"
    return tupleString

# This is a simple example of mapping based on letter counts
def buildAnagrams():
    anagramDict = {}

    with open('linux.words','r') as f:
        for word in f:
            word = word.lower().strip()
            key = buildKey(countLetters(word))
            if(anagramDict.get(key) is None):
                anagramDict[key] = [word]
            else:
                anagramDict[key].append(word)

    return anagramDict

def findAnagrams(anagrams,word):
    key = buildKey(countLetters(word.strip()))
    return anagrams.get(key)

anagrams = buildAnagrams()
print (findAnagrams(anagrams,'silent'))
print (findAnagrams(anagrams,'dance'))
print (findAnagrams(anagrams,'rancor'))
print (findAnagrams(anagrams,'unable'))
