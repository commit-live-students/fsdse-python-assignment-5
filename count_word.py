import re
def countWord(path,word):
    f = open(path,'r')

    match = re.findall(word,f.read())
    #print match
    occurance_count = len(match)
    return occurance_count


#path = './files/testfile.txt'
#word = 'dummy'
#countWord(path,word)
