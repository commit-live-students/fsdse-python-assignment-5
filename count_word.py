def countWord(filepath,word):
    file=open("./files/testfile.txt","r")

    wordcount={}

    for i in file.read().split():
        if i not in wordcount:
            wordcount[i] = 1
        else:
            wordcount[i]+= 1
    return wordcount[word]
