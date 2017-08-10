from collections import Counter

def countWord(filename, word_a):
    counts = {}
    words_list = []

    with open(filename, 'r') as f:
        for line in f:
            for word in line.split(' '):
                words_list.append(word)

    counts = Counter(words_list)
    return counts[word_a]
