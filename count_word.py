def countWord(filepath, word):
    k = 0
    with open(filepath) as f:
        for line in f:
            words = line.split()
            for i in words:
                if i == word:
                    k += 1
    return k
