def countWord(filepath,word):
    lines = open(filepath,'r') # open file to read
    counter = 0

    for line in lines:
        words = line.split()
        for i in words:
            if (word == i):
                counter += 1
            else:
                counter += 0

    return counter

print countWord('/home/vinod-boga/Workspace/code/005-count-word/files/testfile.txt','dummy')
