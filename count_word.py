import re
def countWord(filename, word):
    f = open(filename, "r").read()
    return len(re.findall(word, f))
