def countWord(filename,word):
    count = 0
    f = open(filename,'r')
    for line in f:
        if word in line:
            count+=1
    f.close()
    return count

# countWord("testfile.txt","industry")
# Output : 2
