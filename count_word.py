import sys
import os

def countWord(filePath , keyWord):
    count = 0
    wordCount = {}
    file = open(filePath,"r+")
    for word in file.read().split():
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    print wordCount
    for key in wordCount.keys():
        #print ("%s %s " %(key , wordCount[key]))
        if(key == keyWord):
            print key
            count = wordCount[key]
        
    file.close()
    return count

print countWord('./files/testfile.txt','the')
