def countWord(fname,word):
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                lower_case = i.replace(".","")
                if(lower_case == word):
                    count=count+1
    return count

# countWord('testfile.txt','dummy')
