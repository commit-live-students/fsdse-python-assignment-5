def countWord(filepath,word):
    file = open(filepath)
    textWord = None
    count = 0
    while(textWord != ""):
        textWord = file.readline()
        if (word in textWord):
            count += 1

    return count






countWord('./files/testfile.txt', 'Lorem')
