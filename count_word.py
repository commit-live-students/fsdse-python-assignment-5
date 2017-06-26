def countWord(input_file,word):
    word_count = 0
    doc = open(input_file,'r')
    for line in doc:
        if word in line:
            word_count+=1
    return word_count
