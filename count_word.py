def countWord(filepath, word):
    f = open(filepath,'r')
    para = f.read()
    words = para.split()
    c = 0
    for i in words:
        if i == word:
            c += 1
    return c

path = "./files/testfile.txt"
word = "Lorem"
countWord(path,word)
