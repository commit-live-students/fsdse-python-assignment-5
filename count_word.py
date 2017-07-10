def countWord(input_file,word):
    wordcount = 0
    doc = open(input_file,'r')
    for line in doc:
        if word in line:
            wordcount+=1
    return wordcount
