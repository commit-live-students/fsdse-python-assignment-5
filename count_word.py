def countWord(fname,word):
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if(i == word):
                    count=count+1
    return count


print(countWord('/home/pramodbhalerao/Workspace/code/fsdse-python-assignment-5/files/testfile.txt','dummy'))
