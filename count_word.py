import re
def countWord(file,string):
    f = open(file,'r')
    if not f:
        return False
    match = re.findall(string,f.read())
    #print match
    return len(match)
print countWord('files/testfile.txt','Lorem')
