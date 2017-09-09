def countWord(filepath, word):
    with open(filepath, "r") as file_txt:
        count = 0
        lines = file_txt.readlines()
        for line in lines:
            line = line.split(' ')
#             print line
            for wrd in line:
#                 wrd = wrd.split(',')
#                 print wrd
                if (wrd == word):
                    count +=1
        return count
