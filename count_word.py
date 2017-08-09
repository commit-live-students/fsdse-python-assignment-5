def countWord(fpath, word):
    count = 0
    with open(fpath, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if i == word:
                    count += 1
        return count
