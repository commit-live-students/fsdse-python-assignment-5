def countWord(filename,word):
    count = 0
    word_occurance = open(filename,'r')
    for line in word_occurance:
        if word in line:
            count+=1
    word_occurance.close()
    return count
