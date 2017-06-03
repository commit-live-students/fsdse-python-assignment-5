

def countWord(filepath='files/testfile.txt', word='dummy'):
    f = open(filepath)
    cnt = 0
    for line in f:
        if word in line:
            cnt+=1
    return cnt

print countWord('files/testfile.txt','Lorem')
