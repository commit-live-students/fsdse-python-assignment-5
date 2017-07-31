
def countWord(filepath,testWord):
    #fp = open(filepath,"r")
    wordDict = {}
    #for line in fp.readlines():
    with open(filepath,"r") as file:
        for line in file:
            print line
            for word in line.split(" "):
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
            #print wordDict[testWord]
    return wordDict[testWord]
countWord("files/testfile.txt","Lorem")
