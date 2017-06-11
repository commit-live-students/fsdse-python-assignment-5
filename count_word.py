
def countWord(filepath,testWord):
    fp = open(filepath,"r")
    wordDict = {}
    for line in fp.readlines():
        print line
        for word in line.split(" "):
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
    return wordDict[testWord]
#countWord("files/testfile.txt","Lorem")
