import csv, itertools

file_path = "files/testfile.txt"
string = "Lorem"

def countWord(file_name,word):
        cnt = 0
        f = open(file_name)
        for w in f.read().split():
            if w==word:
                cnt +=1
        return cnt


print countWord(file_path, string)
