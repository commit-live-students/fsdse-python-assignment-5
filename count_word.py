def countWord(pth,target):
    cnt = 0
    f = open(pth,"r")
    for line in f:
        if target in line:
            cnt+=1
    return cnt


countWord('files/testfile.txt','Lorem')
