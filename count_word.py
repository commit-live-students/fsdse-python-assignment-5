filepath='/home/RupaliHangekar/Workspace/code/fsdse-python-assignment-5/files/testfile.txt'
word = 'Ipsum'

def countWord(filepath,word):
    count = 0;
    for line in open (filepath, 'r'):
        #print line
        #print line.split()
        for x in line.split():
            if x==word:
                count += 1
    return count

output = countWord(filepath,word)
print output
