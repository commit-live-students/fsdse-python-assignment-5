def countWord(filepath,word):
    file1=open(filepath,"r")
    count = 0;
    line=file1.readline()
    while (line != ""):
        words = line.split()
        for i in words:
            if i == word:
                count += 1
        line=file1.readline()


    file1.close()
    return count
